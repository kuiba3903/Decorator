import time


def calculate_time(func):
    def wrapper(*args):
        t1 = time.time()
        st = func(*args)
        t2 = time.time()
        print("total time:", t2-t1)
        print(st)
        return st
    return wrapper


@calculate_time
def sort_array(k):
    print("传入参数是:", k)
    time.sleep(2)
    return "睡眠2秒"


if __name__ == "__main__":
    st = sort_array(5)
    print(st)
