
def log(func):
    print("this a function")
    print('call %s():' % func.__name__)
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print('2015-3-25')


now()