class person():
    def __init__(self,name,id_number,post):
        self.name=name
        self.id_number=id_number
        self.post=post
    def display(self):
        print(self.name)
        print(self.id_number)
class employee(person):
    def __init__(self, name, id_number, salary, post):
        self.salary=salary
        self.post=post
        super().__init__(name, id_number, post)
a=employee("Samul gurnald",874763,10000,"Manager")
a.display()