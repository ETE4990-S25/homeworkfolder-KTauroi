import asyncio
import time
import math


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