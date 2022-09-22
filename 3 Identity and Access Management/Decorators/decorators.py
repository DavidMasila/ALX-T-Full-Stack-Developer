from functools import wraps

# #closures recap

# def outer_function(msg):

#     def inner_function():
#         print(msg)

#     #returning inner function not executed
#     return inner_function

# hi_func = outer_function("Hi there")
# hi_func()
# bye_func = outer_function("Bye")
# bye_func()

# #decorators

# def decorator_function(original_function):

#     def wrapper_function(*args, **kwargs):
#         print("Wrapper executed this before {}".format(
#             original_function.__name__))
#         return original_function(*args, **kwargs)

#     return wrapper_function

# @decorator_function
# def display():
#     print("Display function run \n")
#     #same as writing display = decorator_function(display)
# display()

# @decorator_function
# def display_info(name,age):
#     print("display_ran with arguments {} {} \n".format(name,age))

# display_info("masila",49)

# # classes as decorators

# class decorator_class():

#     #takes the functional style decorator function
#     def __init__(self, original_function):
#         self.original_function = original_function

#     #takes the functional style wrapper function
#     def __call__(self, *args, **kwargs):
#         print("Salamu za mbali")
#         return self.original_function(*args, **kwargs)

# @decorator_class
# def display(name,message):
#     print("Hellow {} {}".format(name, message))

# display("masila","kuja hapa")

#practical example for decorators
# logging details


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),
                        level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


# @my_logger
# def display(name, message):
#     print("Hellow {} {}".format(name, message))


# display("masila", "kuja hapa")

def my_timer(orig_func):
    import time 

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1 
        print('{} ran in {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

import time

@my_logger
@my_timer
def display(name, message):
    time.sleep(1)
    print("Hellow {} {}".format(name, message))

display("masila","python")