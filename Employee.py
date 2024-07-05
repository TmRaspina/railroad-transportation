from Admin import Admin
import random

class Employee(Admin):

    global line_name_list 
    line_name_list = []
    global line_info
    line_info = [] 

    global unique_train_id 
    unique_train_id = []
    global train_name 
    train_name = []
    global train_info
    train_info = []



    def __init__(self, username, password):
        self.emp_username = username
        self.emp_password = password
    
    def give_train_information(self):
        self.train_information = train_info
        self.train_name_list = train_name

    def employee_login(self):
        super().give_emp_list()
        if self.emp_username in self.Emp_user_list and self.Emp_password_list[self.Emp_user_list.index(self.emp_username)] == self.emp_password:
            self.train_employee_panel()
        else:
            print("failed to login")
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

    def train_employee_panel(self):
        print("1. Add line\n2. Update line information\n3. Delete line\n4. List of lines\n5. Add train\n6. Delete train\n7. List of trains\n8. Sign out of the user account")
        print("---------------------------------")
        self.my_gozineh = input("Which option?: ")
        if  self.my_gozineh == "1":
            self.add_line()
        elif self.my_gozineh == "2":
            self.update_line_info()
        elif self.my_gozineh == "3":
            self.delete_line()
        elif self.my_gozineh == "4":
            self.give_line_info()
        elif self.my_gozineh == "5":
            self.add_train()
        elif self.my_gozineh == "6":
            self.delete_train()
        elif self.my_gozineh == "7":
            self.give_train_info()
        elif self.my_gozineh == "8":
            return None
        else:
            print("Enter again")
            self.train_employee_panel()

    def add_line(self):
        self.line_name = input("Line name: ")
        while len(self.line_name.strip())==0:
            print("The input cannot be empty try again")
            self.line_name = input("Line name: ")
        if self.check_existence_line():
            self.origin_name = input("Origin name: ")
            while len(self.origin_name.strip())==0:
                print("The input cannot be empty try again")
                self.origin_name = input("Origin name: ")
            self.destination_name = input("Destination name: ")
            while len(self.destination_name.strip())==0 or self.destination_name==self.origin_name:
                if self.destination_name==self.origin_name:
                    print("The origin and destination cannot be the same")
                else:
                    print("The input cannot be empty try again")
                self.destination_name = input("Destination name: ")
            try:
                self.number_of_station = int(input("Number of station: "))
            except:
                print("check that you are adding wrong input!")
                my_input = input("Back to the employee panel? yes/no: ")
                while my_input not in ['yes','no']:
                    print("Unspecified entry")
                    my_input = input("Back to the employee panel? yes/no: ")
                print("---------------------------------")
                if my_input == 'no':
                    self.add_line()
                    return
                elif my_input == 'yes':
                    self.train_employee_panel()
                    return
 
            self.station_names = []
            for name in range(self.number_of_station):
                station_name = input(f"{name+1}. Station name: ")
                while len(station_name.strip())==0 or station_name in self.station_names:
                    print("The input cannot be empty or repetitius try again")
                    station_name = input(f"{name+1}. Station name: ")
                self.station_names.append(station_name)
            self.line_info = dict(Line_name=self.line_name, Origin_name=self.origin_name, Destination_name=self.destination_name, Number_of_station=self.number_of_station, Station_names=self.station_names)
            line_name_list.append(self.line_name)
            line_info.append(self.line_info)
            my_input = input("Back to the employee panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the employee panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.add_line()
            elif my_input == 'yes':
                self.train_employee_panel()
                return
        
    def check_existence_line(self):
        if self.line_name in line_name_list:
            print("Duplicate line name")
            my_input = input("Back to the employee panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the employee panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.add_line()
                return
            elif my_input == 'yes': 
                self.train_employee_panel() 
                return
        else:
            return True  
    
    def update_line_info(self):
        Line_name = input("Enter the line name: ")
        if Line_name not in line_name_list:
            print("line does not exist")
            my_input = input("Back to the employee panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the employee panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.update_line_info()
            elif my_input == 'yes': 
                self.train_employee_panel()
                return
        else:
            info = line_info[line_name_list.index(Line_name)]
            print("---------------------------------")
            print(f"Origin: {info["Origin_name"]}\nDestination: {info["Destination_name"]}\nNumber of station: {info["Number_of_station"]}\nStation: {info["Station_names"]}")
            print("---------------------------------")
            change = input("Which feature do you want to change? (Origin_name/Destination_name/Number_of_station/Station_names): ")
            if change in ["Origin_name","Destination_name","Number_of_station","Station_names"]:
                if change == 'Station_names':
                    add_sub = input("add station or subtract? (add,sub): ")
                    while add_sub not in ["sub","add"]:
                        print("Try again!")
                        add_sub = input("add station or subtract? (add,sub): ")
                    station = []
                    if add_sub == "add":
                        try:
                            i = int(input("how many stations do you wand added?: "))
                            print("---------------------------------")
                            while i <= 0:
                                print("The input cannot be zero and negative")
                                i = int(input("how many stations do you wand added?: "))
                                print("---------------------------------")
                        except:
                            print("---------------------------------")
                            print("check that you are adding wrong input!")
                            my_input = input("Back to the employee panel? yes/no: ")
                            while my_input not in ['yes','no']:
                                print("Unspecified entry")
                                my_input = input("Back to the employee panel? yes/no: ")
                            print("---------------------------------")
                            if my_input == 'no':
                                self.update_line_info()
                            elif my_input == 'yes': 
                                self.train_employee_panel()
                                return 
                        for name in range(i):
                            station_name = input(f"{name+1}. Station name: ")
                            while len(station_name.strip())==0 or station_name in info['Station_names'] or station_name in station:
                                print("The input cannot be empty or repetitius try again")
                                station_name = input(f"{name+1}. Station name: ")
                            station.append(station_name)
                        info[change].extend(station)
                        info["Number_of_station"] = len(info['Station_names'])
                    elif add_sub == "sub":
                        try:
                            i = int(input("how many stations do you wand subtracted?: "))
                            print("---------------------------------")
                            while i <= 0 or i > info["Number_of_station"]:
                                print("The input is wrong try again")
                                i = int(input("how many stations do you wand added?: "))
                                print("---------------------------------")
                        except:
                            print("---------------------------------")
                            print("check that you are adding wrong input!")
                            my_input = input("Back to the employee panel? yes/no: ")
                            while my_input not in ['yes','no']:
                                print("Unspecified entry")
                                my_input = input("Back to the employee panel? yes/no: ")
                            print("---------------------------------")
                            if my_input == 'no':
                                self.update_line_info()
                            elif my_input == 'yes': 
                                self.train_employee_panel()
                                return
                        for name in range(i):
                            station_name = input(f"{name+1}. Station name: ")
                            while len(station_name.strip())==0 or station_name not in info['Station_names']:
                                print("The input cannot be empty or unavailable")
                                station_name = input(f"{name+1}. Station name: ")
                            info['Station_names'].remove(station_name)
                        info["Number_of_station"] = len(info['Station_names'])
         
                elif change == "Number_of_station":
                    try:
                        new_info = int(input(f"Enter the new {change}: "))
                        while new_info < 0:
                            print("The input cannot be negative try again")
                            new_info = int(input(f"Enter the new {change}: "))
                        if new_info > info["Number_of_station"]:
                            print(f"{new_info-info["Number_of_station"]} station must be added")
                            new_name_station = []
                            for i in range(new_info-info["Number_of_station"]):
                                station_name = input(f"{i+1}. Station name: ")
                                while station_name in info["Station_names"] or len(station_name.strip())==0:
                                    print("The input cannot be empty or duplicate")
                                    station_name = input(f"{i+1}. Station name: ")
                                new_name_station.append(station_name)
                            info["Station_names"].extend(new_name_station)
                            info[change] = new_info  
                        elif new_info < info["Number_of_station"]:
                            print(f"{info["Number_of_station"]-new_info} station must be reduced")
                            new_name_station = []
                            for i in range(info["Number_of_station"]-new_info):
                                station_name = input(f"{i+1}. Station name: ")
                                while station_name not in info["Station_names"] or len(station_name.strip())==0:
                                    print("station does not exist")
                                    station_name = input(f"{i+1}. Station name: ")
                                new_name_station.append(station_name)
                            for name in new_name_station:
                                info["Station_names"].remove(name)
                            info[change] = new_info    
                    except:
                            print("---------------------------------")
                            print("check that you are adding wrong input!")
                            my_input = input("Back to the employee panel? yes/no: ")
                            while my_input not in ['yes','no']:
                                print("Unspecified entry")
                                my_input = input("Back to the employee panel? yes/no: ")
                            print("---------------------------------")
                            if my_input == 'no':
                                self.update_line_info()
                            elif my_input == 'yes': 
                                self.train_employee_panel()
                                return
                else: 
                    new_info = input(f"Enter the new {change}: ")
                    while len(new_info.strip())==0:
                        print("The input cannot be empty try again!")
                        new_info = input(f"Enter the new {change}: ")
                    info[change] = new_info
            else:
                print("feature does not exist")
            my_input = input("Back to the employee panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the employee panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.update_line_info()
            elif my_input == 'yes': 
                self.train_employee_panel()
                return

    def delete_line(self):
        Line_name = input("Enter the line name: ")
        if Line_name not in line_name_list:
            print("line does not exist")
        else:
            my_train_list = []
            for train in train_info:
                if train["line"]==Line_name:
                    my_train_list.append(train)
                    id = train["unique_id"]
                    train_name.remove(train_name[unique_train_id.index(id)])
                    unique_train_id.remove(id)
            for qatar in my_train_list:
                train_info.remove(qatar)
            line_info.remove(line_info[line_name_list.index(Line_name)])
            line_name_list.remove(Line_name)
            print("was deleted")
        my_input = input("Back to the employee panel? yes/no: ")
        while my_input not in ['yes','no']:
            print("Unspecified entry")
            my_input = input("Back to the employee panel? yes/no: ")
        print("---------------------------------")
        if my_input == 'no':
            self.delete_line()
        elif my_input == 'yes': 
            self.train_employee_panel()
            return


    def give_line_info(self):
        if len(line_info)==0:
            print("The list is empty")
        else:
            print("---------------------------------")
            for info in line_info:
                print(f"Line: {info["Line_name"]}\t  Origin: {info["Origin_name"]}\tDestination: {info["Destination_name"]}\t Number_station: {info["Number_of_station"]}\tStation: {info["Station_names"]}")
            print("---------------------------------")
        my_input = input("Back to the employee panel? (yes): ")
        while my_input != "yes":
            print("Unspecified entry")
            my_input = input("Back to the employee panel? (yes): ")
        print("---------------------------------")
        self.train_employee_panel()

    def add_train(self):
        self.train_name = input("Train name: ")
        while len(self.train_name.strip())==0:
            print("The input cannot be empty try again")
            self.train_name = input("Train name: ")
        self.line_movement = input("Line of motion: ")
        while self.line_movement not in line_name_list:
            print("The line does not exist\nTry again!")
            my_input = input("Back to the employee panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the employee panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.line_movement = input("Line of motion: ")
            elif my_input == 'yes': 
                self.train_employee_panel()
                return
        '''info_line = line_info[line_name_list.index(self.line_movement)]
        self.stop_amount = []
        print("Enter the amount of stops for each station")
        for station in info_line["Station_names"]:
            try:
                stop = float(input(f"{station}: "))
            except:
                print("check that you are adding str!")
                self.add_train()
            self.stop_amount.append(f"{station}:{stop}")'''
        try:
            self.average_speed = float(input("Average speed(m/s): "))
            while self.average_speed <= 0:
                print("The speed cannot be zero and negative")
                self.average_speed = float(input("Average speed(m/s): "))
            self.stop_amount = float(input("Stop station(min): "))
            while self.stop_amount < 0:
                print("The stop cannot be negative")
                self.stop_amount = float(input("Stop station(min): "))
            self.quality_degree = int(input("Quality degree(max=5,min=1): "))
            while self.quality_degree < 1 or self.quality_degree > 5:
                print("The quality degree not in range")
                self.quality_degree = int(input("Quality degree(max=5,min=1): "))
            self.ticket_price = float(input("ticket price(toman): "))
            while self.ticket_price < 0:
                print("The price cannot be negative")
                self.ticket_price = float(input("ticket price(toman): "))
            self.train_capacity = int(input("Train capacity: "))
            while self.train_capacity < 0:
                print("The capacity cannot be negative")
                self.train_capacity = int(input("Train capacity: "))
            
        except:
            print("check that you are adding wrong input!")
            my_input = input("Back to the employee panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the employee panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.add_train()
            elif my_input == 'yes': 
                self.train_employee_panel()
        if self.my_gozineh == "5":
            rand = random.randint(100,999)
            while rand in unique_train_id:
                rand = random.randint(100,999)
            rand = str(rand)
            print(f"Unique id: {rand}")
            train_name.append(self.train_name)
            unique_train_id.append(rand)
            self.train_info = dict(train=self.train_name, line=self.line_movement, speed=self.average_speed, stop=self.stop_amount, quality=self.quality_degree, price=self.ticket_price, capacity=self.train_capacity, unique_id=rand)
            train_info.append(self.train_info)
            my_input = input("Back to the employee panel? yes/no: ")
            while my_input not in ['yes','no']:
                print("Unspecified entry")
                my_input = input("Back to the employee panel? yes/no: ")
            print("---------------------------------")
            if my_input == 'no':
                self.add_train()
            elif my_input == 'yes': 
                self.train_employee_panel()
                return
    
    def delete_train(self):
        id = input("Enter the train ID: ")
        if id not in unique_train_id:
            print("The ID does not exist")
        else:
            train_name.remove(train_name[unique_train_id.index(id)])
            train_info.remove(train_info[unique_train_id.index(id)])
            unique_train_id.remove(id)
            print("was deleted")
        my_input = input("Back to the employee panel? yes/no: ")
        while my_input not in ['yes','no']:
            print("Unspecified entry")
            my_input = input("Back to the employee panel? yes/no: ")
        print("---------------------------------")
        if my_input == 'no':
            self.delete_train()
        elif my_input == 'yes': 
            self.train_employee_panel()
            return

    def give_train_info(self):
        if len(train_info) != 0:
            header = train_info[0].keys()
            row = "{:<10}"*len(header)
            print(row.format(*header))
            print("--------------------------------------------------------------------------------")
            for emp in train_info:
                print(row.format(*emp.values()))
        else:
            print("There is no train")
        my_input = input("Back to the employee panel? (yes): ")
        while my_input != "yes":
            print("Unspecified entry")
            my_input = input("Back to the employee panel? (yes): ")
        print("---------------------------------")
        self.train_employee_panel()
        return
    


         









        
            


            



            
            


        

    

 
    

    