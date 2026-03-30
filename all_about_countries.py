class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most spoken languege in India")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washsington DC is the capital of the USA")
    def language(self):
        print("English is the most spoken languege in the USA")
    def type(self):
        print("The USA is a developed country")

obj_Ind=India()
obj_USA=USA()

for country in (obj_Ind,obj_USA):
    country.capital()
    country.language()
    country.type()