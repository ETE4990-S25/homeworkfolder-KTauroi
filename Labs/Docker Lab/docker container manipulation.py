import docker
from datetime import timedelta, datetime
import time
import freezegun

def start():
  client = docker.from_env()
  for container in client.containers.list(all=True):
    container.start()

def stop():    
  client = docker.from_env()
  for container in client.containers.list(all=True):
    container.stop()

def continuity():    
    client = docker.from_env()
    for container in client.containers.list(all=True):
        if {container.status} !='running':
            container.start()

def maintain():
    with freezegun.freeze_time() as frozen:
        for _ in range(5):
            frozen.tick(timedelta(hours=24))
            time.sleep(0.1)
    client = docker.from_env()
    for container in client.containers.list(all=True):
        container.stop()
        container.start()

start()
stop()
continuity()
stop()
maintain()