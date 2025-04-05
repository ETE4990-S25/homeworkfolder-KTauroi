from multiprocessing import Process, Queue
import threading
import time
import math
import asyncio

def is_prime(n):  #Determines Prime number
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_finder(start, step, end_time, q): #Function for finding/definign max prime adding time constraint
    n = start
    max_prime = 0
    while time.time() < end_time:
        if is_prime(n):
            max_prime = n  # Keep only the highest prime
        n += step
    q.put(max_prime)  # Only put one per process

def calculate_factorial_approximation(n): #I was excceeding the digit limit so I changed to a logarithmic format -_- SFEA
    if n == 0 or n == 1:
        return 0
    # Stirling's approximation for log(n!) for truncation purposes
    return 0.5 * math.log(2 * math.pi * n) + n * (math.log(n) - 1)

async def is_prime(n):
    """ Determines if the number is prime """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

async def prime_finder(start, step, end_time):
    """ Function to find the highest prime with a time limit """
    n = start
    max_prime = 0
    while time.time() < end_time:
        if await is_prime(n):  # Await the result of is_prime (makes it asynchronous)
            max_prime = n
        n += step
    return max_prime  # Return the highest prime found in this task

async def calculate_factorial_approximation(n):
    """ Stirling's approximation for factorial calculation """
    if n == 0 or n == 1:
        return 0
    return 0.5 * math.log(2 * math.pi * n) + n * (math.log(n) - 1)

async def main():
    num_task = 4 #number of concurrent task simiar to threads
    run_for_seconds = 10 #runtime
    end_time = time.time() + run_for_seconds

    tasks = []

    for i in range(num_task):
            task = asyncio.create_task(prime_finder(i + 1, num_task, end_time))
            tasks.append(task)
    
    primes = await asyncio.gather(*tasks)
    primes.sort()
    print(f"Max primes from each task: {primes}")
    print(f"Overall Max prime found: {primes[-1] if primes else 'None'}")
    print(f"Factorial Approximation: {await calculate_factorial_approximation(primes[-1])}\n")

asyncio.run(main())

if __name__ == '__main__':

    num_processes = 4 #Amount of processes
    run_for_seconds = 10 #time duration CIATTWFC
    end_time = time.time() + run_for_seconds
    queue = Queue() #Prevents mishaps SF
    processes = [] #list for the results later

    for i in range(num_processes): #Passing arguments for each process
        p = Process(target=prime_finder, args=(i + 1, num_processes, end_time, queue))
        processes.append(p) #Ass to list corresponding with process
        p.start()

    for p in processes:
        p.join() #BTTTEP

    primes = []  #records max prime each process found
    while not queue.empty():
        primes.append(queue.get())

    primes.sort() #Organizes the list of max primes found
    print(f"Max primes from each process: {primes}")
    print(f"Overall Max prime found: {primes[-1] if primes else 'None'}")
    print(f"Factorial Approximation: {calculate_factorial_approximation(primes[-1])}\n")

if __name__ == '__main__':
    num_threads = 4  #4 threads
    run_for_seconds = 10  #Time duration
    end_time = time.time() + run_for_seconds
    queue = Queue()  #Organizing
    threads = [] #recording max primes

    for i in range(num_threads):
        #New thread for each chunk of work
        t = threading.Thread(target=prime_finder, args=(i + 1, num_threads, end_time, queue))
        threads.append(t)
        t.start()  #Start thread

    for t in threads:
        t.join()  #Wait for all threads to finish

    primes = []  #List of max primes
    while not queue.empty():
        primes.append(queue.get())  #Collect results from the queue adding to primes list

    primes.sort()  #Sort max primes 
    print(f"Max primes from each thread: {primes}")
    print(f"Overall Max prime found: {primes[-1] if primes else 'None'}")
    print(f"Factorial Approximation: {calculate_factorial_approximation(primes[-1])}\n")