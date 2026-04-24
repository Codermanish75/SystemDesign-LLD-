from user import User
from userDatabase import User_Database

user_obj=User("Manish",24,"manish@gmail.com")
User_Database_obj=User_Database("mysql","manish","manish656")

user_obj.get_info()

User_Database_obj.save_to_database(user_obj)