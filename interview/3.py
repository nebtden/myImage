class One:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

class TestClass(One):
    a=1

test1 = TestClass()
test2 = TestClass()
print(test1.a,test2.a)

test1.a=3
print(test1.a,test2.a)