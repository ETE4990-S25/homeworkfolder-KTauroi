from __future__ import annotations

import json
import os
import queue
import sys
import threading
import time
from collections import Counter
from pathlib import Path
from typing import Callable, Dict, List

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

LOG_LEVELS: List[str] = ["INFO", "WARNING", "ERROR", "CRITICAL"]

###############################################################################
#                               Tail helpers                                  #
###############################################################################

def _safe_json_loads(line: str) -> Dict | None:
    """Return dict if `line` is valid JSON, else None (silently ignore)."""
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return None


class JSONFileTailer(threading.Thread):
    """Tail a single JSON‑log file in real time and push records to a queue."""

    def __init__(self, path: Path, out_q: "queue.Queue[dict]", *, poll: float = 0.4):
        super().__init__(daemon=True)
        self.path = path
        self.poll = poll
        self.out_q = out_q

    def run(self) -> None:
        with self.path.open("r", encoding="utf‑8") as f:
            # Start at end‑of‑file to avoid re‑processing existing lines
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line:
                    rec = _safe_json_loads(line)
                    if rec:
                        self.out_q.put(rec)
                else:
                    time.sleep(self.poll)

###############################################################################
#                        Real‑time summary printer                             #
###############################################################################
class SummaryPrinter(threading.Thread):
    """Print running counts and any new CRITICAL messages."""

    def __init__(self, in_q: "queue.Queue[dict]", *, poll: float = 0.2):
        super().__init__(daemon=True)
        self.in_q = in_q
        self.poll = poll
        self.counts = Counter({lvl: 0 for lvl in LOG_LEVELS})
        self.lock = threading.Lock()

    # ── public API ──────────────────────────────────────────────────────────
    def snapshot_counts(self) -> Dict[str, int]:
        with self.lock:
            return dict(self.counts)

    # ── thread main loop ───────────────────────────────────────────────────
    def run(self) -> None:
        while True:
            try:
                rec = self.in_q.get(timeout=self.poll)
            except queue.Empty:
                continue
            level = rec.get("levelname")
            if level in LOG_LEVELS:
                with self.lock:
                    self.counts[level] += 1
                if level == "CRITICAL":
                    # Print critical message immediately
                    msg = rec.get("message", "<no message>")
                    ts = rec.get("asctime", "<no time>")
                    print(f"\n!!! CRITICAL [{ts}] {msg}")
            # Periodically refresh summary (simple overwrite)
            self._print_summary()

    def _print_summary(self) -> None:
        summary = " | ".join(f"{lvl}: {self.counts[lvl]}" for lvl in LOG_LEVELS)
        # "\r" carriage return keeps output on one line; flush for immediacy
        print(f"\r[Counts] {summary}", end="", flush=True)

###############################################################################
#                              Live plotter                                   #
###############################################################################
class LiveBarPlot(threading.Thread):
    """Update a bar chart in real time based on the SummaryPrinter counts."""

    def __init__(self, summary: SummaryPrinter, interval_ms: int = 800):
        super().__init__(daemon=True)
        self.summary = summary
        self.interval_ms = interval_ms

    def run(self) -> None:
        # Create figure in this (daemon) thread – works fine with Agg/Qt backends
        plt.ion()  # interactive mode
        self.fig, self.ax = plt.subplots()
        self.bars = self.ax.bar(LOG_LEVELS, [0] * len(LOG_LEVELS))
        self.ax.set_ylim(0, 1)  # will auto‑scale later
        self.ax.set_ylabel("Count")
        self.ax.set_title("Live Log‑Level Distribution")

        def _update(_frame):
            counts = self.summary.snapshot_counts()
            max_val = max(counts.values()) or 1
            self.ax.set_ylim(0, max_val * 1.1)
            for bar, lvl in zip(self.bars, LOG_LEVELS):
                bar.set_height(counts[lvl])
            return self.bars

        # FuncAnimation handles redraws at the given interval.
        self.anim = FuncAnimation(self.fig, _update, interval=self.interval_ms)
        plt.show(block=True)  # keep the thread alive until window closed

###############################################################################
#                                   main                                      #
###############################################################################

def main(paths: List[str]):
    if not paths:
        print("Usage: python log_monitor.py <log1.json> [log2.json …]", file=sys.stderr)
        sys.exit(1)

    # ── shared queue between tailers and summary printer ───────────────────
    record_q: "queue.Queue[dict]" = queue.Queue()

    # ── start file tailers ─────────────────────────────────────────────────
    tailers = [JSONFileTailer(Path(p), record_q) for p in paths]
    for t in tailers:
        t.start()
        print(f"Tailing {t.path} …")

    # ── summary printer ────────────────────────────────────────────────────
    summary = SummaryPrinter(record_q)
    summary.start()

    # ── live plot ──────────────────────────────────────────────────────────
    plotter = LiveBarPlot(summary)
    plotter.start()

    # ── keep the main thread alive; daemon threads will exit with it ───────
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping log monitor – goodbye!")


if __name__ == "__main__":
    main(sys.argv[1:])