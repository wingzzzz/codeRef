import time
import functools


def my_map(func, *iterables):
    return (func(*args) for args in zip(*iterables))


def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}耗时：{end - start:0.4f}')
        return result

    return inner


@timer
def my_func():
    time.sleep(2)


def main():
    # 测试 my_map
    l1 = [3, 4, 5, 6]
    l2 = [8, 4, 2]
    gen = my_map(lambda a, b: a + b, l1, l2)
    print(gen)
    print(list(gen))

    # 测试timer
    my_func()


if __name__ == '__main__':
    main()
