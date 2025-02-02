import time


def log(filename=None):
    '''логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки'''
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                log_message = f"{func.__name__} OK\n"
                due = end_time - start_time
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                # end_time = time.time()
                log_message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                raise e

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


my_function(4, 2)


@log(filename="")
def my_function(x, y):
    return x / y

my_function(6, 3)
