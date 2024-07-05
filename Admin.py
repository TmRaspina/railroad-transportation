import sys
class Admin:


    global Emp_user_list 
    Emp_user_list = []
    global Emp_email_list 
    Emp_email_list = []
    global Emp_info_list 
    Emp_info_list = []
    global Emp_password_list
    Emp_password_list = []


    def __init__(self,username,password):
        self.Username_Admin = username
        self.Pass_Admin = password
    
    def give_emp_list(self):
        self.Emp_user_list = Emp_user_list
        self.Emp_password_list = Emp_password_list
         
    def check_admin_login(self):
        if self.Username_Admin == "Arshiya" and self.Pass_Admin == "1379":
            print("Admin successfully logged in =)))")
            self.management_panel()
        else:
            print("The input is wrong :((")
            my_input = input("Back to the start panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the start panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                print("Enter username and password")
                return False
            elif my_input == 'yes':
                return True
   
    def management_panel(self):
        print("1. Add train employee\n2. Remove train employee\n3. List of employees\n4. Exit!")
        print("---------------------------------")
        my_gozineh = input("Which option?: ")
        if  my_gozineh == "1":
            self.add_train_employee()
        elif my_gozineh == "2":
            self.del_train_employee()
        elif my_gozineh == "3":
            self.give_emp_info_list()
        elif my_gozineh == "4":
            return None
        else:
            print("Enter again")
            self.management_panel()
            
    def add_train_employee(self):
        self.Emp_username = input("Employee username: ")
        while (len(self.Emp_username.strip())==0):
            print("The input cannot be empty try again")
            self.Emp_username = input("Employee username: ")
        self.Emp_email = input("Employee email: ")
        while (len(self.Emp_email.strip())==0):
            print("The input cannot be empty try again")
            self.Emp_email = input("Employee email: ")
        self.Emp_name = input("Employee name: ")
        while (len(self.Emp_name.strip())==0):
            print("The input cannot be empty try again")
            self.Emp_name = input("Employee name: ")
        self.Emp_family = input("Employee family: ")
        while (len(self.Emp_family.strip())==0):
            print("The input cannot be empty try again")
            self.Emp_family = input("Employee family: ")
        self.Emp_pass = input("Employee password: ")
        while (len(self.Emp_pass.strip())==0):
            print("The input cannot be empty try again")
            self.Emp_pass = input("Employee password: ")
        else:
            if self.check_existence_emp():
                self.dict_info = dict(Name= self.Emp_name, Family= self.Emp_family, Email= self.Emp_email, Username= self.Emp_username, password= self.Emp_pass)
                Emp_user_list.append(self.Emp_username)
                Emp_email_list.append(self.Emp_email)
                Emp_password_list.append(self.Emp_pass)
                Emp_info_list.append(self.dict_info)

                my_input = input("Back to the management panel? yes/no: ")
                while my_input not in ['yes','no']:
                    print("Unspecified entry")
                    my_input = input("Back to the management panel? yes/no: ")
                print("---------------------------------")
                if my_input == 'no':
                    self.add_train_employee()
                elif my_input == 'yes':
                    self.management_panel() 
    
    def check_existence_emp(self):
            if self.Emp_username in Emp_user_list and self.Emp_email in Emp_email_list:
                print("Duplicate entry")
            elif self.Emp_username in Emp_user_list:
                print("Duplicate username")
            elif self.Emp_email in Emp_email_list:
                print("Duplicate email")
            else: 
                return True
            if self.Emp_username in Emp_user_list or self.Emp_email in Emp_email_list:
                my_input = input("Back to the management panel? yes/no: ")
                while my_input not in ['yes','no']:
                    print("Unspecified entry")
                    my_input = input("Back to the management panel? yes/no: ")
                print("---------------------------------")
                if my_input == 'no':
                    self.add_train_employee()
                elif my_input == 'yes': 
                    self.management_panel()

    def del_train_employee(self):
        user = input("Enter employee username: ")
        if user not in Emp_user_list:
            print("The username does not exist")
        else:
            for Emp in Emp_info_list:
                if user == Emp["Username"]:
                    Emp_email_list.remove(Emp["Email"])
                    Emp_password_list.remove(Emp["password"])
                    Emp_user_list.remove(user)
                    Emp_info_list.remove(Emp)
                    print("The employee was deleted")
                    break
                    
        my_input = input("Back to the management panel? yes/no: ")
        while my_input not in ['yes','no']:
            print("Unspecified entry")
            my_input = input("Back to the management panel? yes/no: ")
        print("---------------------------------")
        if my_input == 'no':
            self.del_train_employee()
        elif my_input == 'yes':
            self.management_panel()
    
    def give_emp_info_list(self):
        if len(Emp_info_list) != 0:
            header = Emp_info_list[0].keys()
            row = "{:<10}"*len(header)
            print(row.format(*header))
            print("-------------------------------------------------")
            for emp in Emp_info_list:
                print(row.format(*emp.values()))
        else:
            print("There is no employee")
        print("---------------------------------")
        my_input = input("Back to the management panel? (yes): ")
        while my_input != "yes":
            print("Unspecified entry")
            my_input = input("Back to the management panel? (yes): ")
        print("---------------------------------")
        self.management_panel()
    




            
    