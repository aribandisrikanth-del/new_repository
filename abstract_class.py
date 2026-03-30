from abc import ABC,abstractmethod
class hello():
    def print(self,y):
        print("passed value:",y)
    @abstractmethod
    def task(self):
        print("we are in a abstract class")
class test_class(hello):
    def task(self):
        print("we are inside a test class")

test_obj=test_class()
test_obj.task()
test_obj.print(100)