import redis
import time

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
redis_client.flushdb()

def fibonacci(n):
    cached_result = redis_client.get(str(n))
    if cached_result:
        return int(cached_result)
    result = n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
    redis_client.set(str(n), str(result))
    return result

def measure_fibonacci(n):
    start = time.time()
    [fibonacci(i) for i in range(n)]
    return time.time() - start

n = 10000
print(f"Перший прохід: {measure_fibonacci(n):.6f}s")
print(f"Другий прохід: {measure_fibonacci(n):.6f}s")
fib = fibonacci(n)
len_fib = len(str(fib))
print(f"Число номер {n}:")
print(f"{fib}")
print(f"Кількість цифр:{len_fib}")
