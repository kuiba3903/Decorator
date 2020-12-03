import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        count = func(*args, **kwargs)
        t2 = time.time()
        print(t2 - t1)
        return count
    return wrapper


def is_prime(n):
    if n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

@calculate_time
def prime(num):
    count = 0
    for i in range(2, num):
        if is_prime(i):
            print(i)
            count += 1
        else:
            pass
    return count


total_count = prime(1000)
print("1000以内的素数数量为:", total_count)