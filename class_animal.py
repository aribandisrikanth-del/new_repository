from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i can slither")
class dog(animal):
    def move(self):
        print("i can walk on four legs")
class lion(animal):
    def move(self):
        print("i can walk on four legs")
r=human()
r.move()

k=snake()
k.move()

r=dog()
r.move()

k=lion()
k.move()
