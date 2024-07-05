from Admin import Admin
from Employee import Employee
from User import User


login_user = []
login_pass = []

def Start_Panel():
    print("1. Admin\n2. Train employee\n3. Normal user\n4. Exit!")
    print("---------------------------------")
    print("Which option?:", end=" ")
    global my_digit_start
    my_digit_start = input()
    if my_digit_start not in ["1","2","3","4"]:
        print("Enter again")
        Start_Panel()

def User_panel():
    print("User Panel")
    print("1- Sign up\n2- Sign in \n3- Exit the user panel")
    print("---------------------------------")
    choice = input("Enter your choice: ")
    return choice

print("Welcome!")                            
Start_Panel()
while my_digit_start != "4":
    if my_digit_start == "1":
        print("Enter username and password")
        username_admin = input("Username: ")
        pass_admin = input("Password: ")
        print("---------------------------------")
        admin = Admin(username_admin,pass_admin)
        return_login = admin.check_admin_login()
        while return_login == False:
            username_admin = input("Username: ")
            pass_admin = input("Password: ")
            print("---------------------------------")
            admin = Admin(username_admin,pass_admin)
            return_login = admin.check_admin_login()
        Start_Panel()
    
    elif my_digit_start == "2":
        print("Enter username and password")
        emp_username = input("Username: ")
        emp_pass = input("Password: ")
        print("---------------------------------")
        employee = Employee(emp_username,emp_pass)
        emp_login = employee.employee_login()
        while emp_login == False:
            emp_username = input("Username: ")
            emp_pass = input("Password: ")
            print("---------------------------------")
            employee = Employee(emp_username,emp_pass)
            emp_login = employee.employee_login()
        Start_Panel()
    
    elif my_digit_start == "3":
        print("Welcome =)")
        choice = User_panel()
        while choice != "3":
            if choice == "1":
                name = input("Enter your name: ")
                while len(name.strip())==0:
                    print("input cannot be empty")
                    name = input("Enter your name: ")
                email = input("Enter your email: ")
                while len(email.strip())==0:
                    print("input cannot be empty")
                    email = input("Enter your email: ")
                username = input("Enter username: ")
                while len(username.strip())==0:
                    print("input cannot be empty")
                    username = input("Enter your username: ")
                password = input("Enter password: ")
                while len(password.strip())==0:
                    print("input cannot be empty")
                    password = input("Enter your username: ")
                user = User(name,email,username,password)
                print("---------------------------------")
                while user.user_signup() == False:
                    name = input("Enter your name: ")
                    while len(name.strip())==0:
                        print("input cannot be empty")
                        name = input("Enter your name: ")
                    email = input("Enter your email: ")
                    while len(email.strip())==0:
                        print("input cannot be empty")
                        email = input("Enter your email: ")
                    username = input("Enter username: ")
                    while len(username.strip())==0:
                        print("input cannot be empty")
                        username = input("Enter your username: ")
                    password = input("Enter password: ")
                    while len(password.strip())==0:
                        print("input cannot be empty")
                        password = input("Enter your username: ")
                    user = User(name,email,username,password)

                login_user,login_pass = user.give_user_info()
                choice = User_panel()
            elif choice == "2":
                my_input = "no"
                while my_input == "no":
                    print("Enter username and password")
                    login_username = input("Username: ")
                    login_password = input("Password: ")
                    if login_username not in login_user:
                        print("username does not exist")
                        my_input = input("Back to the user panel? yes/no: ")
                        while my_input not in ['yes','no']:
                            print("Unspecified entry")
                            my_input = input("Back to the start panel? yes/no: ")
                        print("---------------------------------")     
                    else:
                        if login_pass[login_user.index(login_username)] == login_password:
                            print("---------------------------------")
                            print(f"Welcome dear {login_username}")
                            user.user_login(login_username,login_password)
                            my_input = "yes"
                        else: 
                            print("Incorrect password")
                            my_input = input("Back to the user panel? yes/no: ")
                            while my_input not in ['yes','no']:
                                print("Unspecified entry")
                                my_input = input("Back to the start panel? yes/no: ")
                            print("---------------------------------")
                choice = User_panel() 
            else:
                print("Enter again")
                choice = User_panel()
        Start_Panel()
print("Goodbye :(( ")

        
        


  






