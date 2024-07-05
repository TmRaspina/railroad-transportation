from Employee import Employee

class User(Employee):

    
    
    global user_username
    user_username = []
    global user_email
    user_email = []
    global user_password
    user_password = []
    global info_user
    info_user = {} 
    global money
    money = []
    

    global buy_user_info
    buy_user_info = {}

    

    def __init__(self, name, email, username, password):
        self.user_name = name
        self.user_email = email
        self.user_username = username
        self.user_password = password
        
    def user_signup(self):
        if (self.user_username in user_username) and (self.user_email in user_email):
            print("Duplicate entry")
            my_input = input("Back to the user panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the start panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                return False
            elif my_input == 'yes':
                return True
        elif self.user_username in user_username:
            print("The username has been taken, please try another one")
            my_input = input("Back to the user panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the start panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                return False
            elif my_input == 'yes':
                return True
        elif self.user_email in user_email:
            print("your email address has been registered before")
            my_input = input("Back to the user panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the start panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                return False
            elif my_input == 'yes':
                return True
        else:
            user_username.append(self.user_username)
            user_email.append(self.user_email)
            user_password.append(self.user_password)
            money.append(0)
            info_user[self.user_username] = {"Name":self.user_name,"Username":self.user_username,"Email":self.user_email,"Password":self.user_password}
            return True
            
    def user_login(self,my_username,my_pass):
        self.username = my_username
        self.password = my_pass
        self.buy_panel()
        '''if self.username not in user_username:
            print("username does not exist")
            my_input = input("Back to the user panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the start panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.user_login()
            elif my_input == 'yes':
                return True
            
        else:
            if user_password[user_username.index(self.username)] == self.password:
                print("---------------------------------")
                print(f"Welcome dear {self.user_name}")
                self.buy_panel()
            else: 
                print("Incorrect password")
                my_input = input("Back to the user panel? yes/no: ")
                while my_input not in ['yes','no']:
                    print("Unspecified entry")
                    my_input = input("Back to the start panel? yes/no: ")
                print("---------------------------------")
                if my_input == 'no':
                    self.user_login()
                elif my_input == 'yes':
                    return True'''
    
    def buy_panel(self):
        print("1. Buying ticket\n2. Changing user info\n3. Wallet\n4. Exit")
        print("---------------------------------")
        self.option = input("Which option: ")
        if self.option == "1":
            self.buying_ticket()
        elif self.option == "2":
            self.user_information()
        elif self.option == "3":
            self.Wallet()
        elif self.option == "4":
            return
        else:
            print("Enter again")
            self.buy_panel()

    def buying_ticket(self):
        super().give_train_information()
        if len(self.train_information) != 0:
            header = self.train_information[0].keys()
            row = "{:<10}"*len(header)
            print(row.format(*header))
            print("--------------------------------------------------------------------------------")
            for emp in self.train_information:
                print(row.format(*emp.values()))
        else:
            print("There is no train")
        print("---------------------------------")
        if self.username in buy_user_info.keys():
            print("Bought")
            print(buy_user_info[self.username])
            print("---------------------------------")
        train = input("Train name: ")
        if train not in self.train_name_list:
            print("The train does not exist")
        else:
            info = self.train_information[self.train_name_list.index(train)] 
            if info["capacity"] == 0 :
                print("Full capacity")
            elif money[user_username.index(self.username)] < info["price"]:
                print("not enough money :)")
            else:
                try:
                    number = int(input("Number of ticket: "))
                except:
                    print("check that you are adding wrong input!")
                    self.buying_ticket()
                
                if number <= 0:
                    print("The input cannot be negative and zero")
                elif number > info["capacity"]:
                    print("Train capacity is full")
                else:
                    buy_user_info[self.username] = {"Train":train,"Reserve":number}
                    info["capacity"] = info["capacity"]-number
                    money[user_username.index(self.username)] -= (info["price"]*number)
        my_input = input("Back to the buy panel? yes/no: ")
        while my_input not in ['yes','no']:
            print("Unspecified entry")
            my_input = input("Back to the buying panel? yes/no: ")
        print("---------------------------------")
        if my_input == 'no':
            self.buying_ticket()
        elif my_input == 'yes':
            self.buy_panel()
    
    def user_information(self):
        if len(info_user[self.username]) != 0:
            header = info_user[self.username].keys()
            row = "{:<10}"*len(header)
            print(row.format(*header))
            print("---------------------------------------")
            print(row.format(*info_user[self.username].values()))
        print("---------------------------------")
        change = input("Which feature do you want to change? (Name/Username/Email/Password): ")
        if change == "Username":
            new_username = input("New Username: ")
            if new_username in user_username:
                print("username is exits :))\ntry again")
            else:
                user_username[user_username.index(self.username)] = new_username
                info_user[new_username] = info_user[self.username]
                del info_user[self.username]
                info = info_user[new_username]
                info["Username"] = new_username
                if self.username in buy_user_info.keys():
                    buy_user_info[new_username] = buy_user_info[self.username]
                    del buy_user_info[self.username]
                self.username = new_username
        elif change == "Email":
            new_email = input("New Email: ")
            while len(new_email.strip())==0:
                print("input cannot be empty try again")
                new_email = input("New Email: ")
            if new_email in user_email:
                print("email is exits :))\ntry again")
                self.user_information()
            else:
                information = info_user[self.username]
                user_email.remove(information["Email"]) 
                user_email.append(new_email)
                information["Email"] = new_email
        elif change == "Password":
            new_pass = input("New Password: ")
            while len(new_pass.strip())==0:
                print("input cannot be empty try again")
                new_pass = input("New Password: ")
            user_password[user_password.index(self.password)] = new_pass
            inform = info_user[self.username]
            inform["Password"] = new_pass
        elif change == "Name":
            new_name = input("New Name: ")
            while len(new_name.strip())==0:
                print("input cannot be empty try again")
                new_name = input("New Name: ")
            infor = info_user[self.username]
            infor["Name"] = new_name

        else:
            print("feature does not exist")
        my_input = input("Back to the buying panel? yes/no: ")
        while my_input not in ['yes','no']:
            print("Unspecified entry")
            my_input = input("Back to the buying panel? yes/no: ")
        print("---------------------------------")
        if my_input == 'no':
            self.user_information()
        elif my_input == 'yes': 
            self.buy_panel()
    
    def give_user_info(self):
        self.username_user = user_username
        self.password_user = user_password 
        return self.username_user,self.password_user

    def Wallet(self):
        my_input = input(f"your current balance is {money[user_username.index(self.username)]}\nDo you to add money?(yes,no): ")
        if my_input == "yes":
            try:
                pay = float(input("How much do you want to add?: "))
                while pay <= 0:
                    print("try again!")
                    pay = float(input("How much do you want to add?: "))
                money[user_username.index(self.username)] += pay
                print("added")
            except:
                print("Invalid input!")
                self.Wallet()
        elif my_input == "no":
            print("---------------------------------")
            self.buy_panel()
        else:
            print("try again")
            self.Wallet()
        if self.option == "3":
            my_input = input("Back to the buying panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the buying panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.Wallet()
            elif my_input == 'yes': 
                self.buy_panel()
            



         










            


                

        
    

                
                







