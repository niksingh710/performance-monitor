def performance(func):
    '''
    Info:   This library using a decorator that will tell you the amount of time took by your system to execute specific function,class etc.
    '''
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"\n:-: {func.__name__} --> {(t2-t1)*1000} ms\n")
        return result
    return wrapper


def performance_sec(func):
    '''
    Info:   This library using a decorator that will tell you the amount of time took by your system to execute specific function,class etc.
    '''
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"\n:-: {func.__name__} --> {(t2-t1)} sec\n")
        return result
    return wrapper


def performance_min(func):
    '''
    Info:   This library using a decorator that will tell you the amount of time took by your system to execute specific function,class etc.
    '''
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"\n:-: {func.__name__} --> {(t2-t1)/60} min\n")
        return result
    return wrapper


def performance_hr(func):
    '''
    Info:   This library using a decorator that will tell you the amount of time took by your system to execute specific function,class etc.
    '''
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"\n:-: {func.__name__} --> {((t2-t1)/60)/60} hr\n")
        return result
    return wrapper
