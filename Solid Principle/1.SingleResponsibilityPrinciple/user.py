class User:
    def __init__(self,name,age,email):
        self.name:str=name
        self.age:int=age
        self.email:str=email

    def get_info(self):
        print (f"Name of the user is {self.name} and emailID is {self.email}")
    
    def is_adult(self)->bool:
        return self.age>18
    