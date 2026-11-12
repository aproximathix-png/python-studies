import json
try:
    with open('contact.json', 'r') as r:
        contact = json.load(r)
except FileNotFoundError:
    contact = []

restart = True 
while restart:
    print("Welcome to the Contact Book!")
    print("What do you want to do?")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Delete a contact")  
    print("4. update a contact")
    print("5. Search a contact")
    print("6. Exit")
    answer = input("Enter your choice (1-6): ")
    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid input. Please enter a number between 1 and 6.")
        answer = input("Enter your choice (1-6): ")
    if answer == "1":
        print("Enter the contact details:")
        validation1 = False
        while validation1 == False:
            name = input("Name: ")
            name = name.strip().lower()
            mail = input("Email: ")
            mail = mail.strip().lower()
            if name == "" or mail == "":
                print("can't be empty")
                validation1 = False
            else:
                validation1 = True
        phone = (input("phone number : "))
        while not phone.isdigit():
            print("phone number must be a number")
            phone = (input("phone number : "))
        contacts = {"name": name, "mail": mail, "phone": phone}
        contact.append(contacts)

    if answer == "2" :
        if  contact == [] :
            print("No friend boohoo.")
        for index, contact_dict in enumerate(contact):
            for key, value in contact_dict.items():
                print(f'{index} - {key}: {value}')

            
    if answer == "3" :
        if  contact == []:
            print("No contact found.")  
        else:         
            print("Enter the index of the contact to delete:")
                
            index = (input())
            while not index.isdigit() or int(index) >= len(contact):
                print("Invalid input. Please enter a valid index.")
                index = input()
            contact.pop(int(index))
            print("contact removed successfully")


    if answer == "4":
        if  contact == []:
             print("No contact found.")  
        else:   
            print("which contact do you want to update")
            index = input()
            while not index.isdigit() or int(index) >= len(contact) or index == "":
                print("Invalid input. Please enter a valid index.")
                index = input()
            print("what are the change you wanna do ? ")
            print("name")
            print("mail")
            print("number")
            change = input()
            if change == "name" :
                new_name = input("New name: ")
                index = int(index)
                contact[index]["name"] = new_name

            elif change == "mail":
                new_mail = input("New email: ")
                while new_mail.strip() == "":
                    print("Email can't be empty")
                    new_mail = input("New email: ")
                index = int(index)
                contact[index]["mail"] = new_mail
            elif change == "number":
                new_number = input("New phone number: ")
                while not new_number.isdigit():
                    print("Phone number must be a number")
                    new_number = input("New phone number: ")
                index = int(index)
                contact[index]["phone"] = new_number

            else:
                print("Invalid option. Please choose name, mail, or number.")
            


    if answer == "5":
        if  contact == []:
            print("No contact found.")  
        else:   
            print("who are we searching for ? ")
            name = input().strip()
            name = name.lower()
            found = False
            for searched_name, contact_dict in enumerate(contact):
                if name == contact_dict["name"]:
                    print(contact_dict) 
                    found = True
            if found == False : 
                print("no name found")


    with open("contact.json", "w") as f:
            json.dump(contact, f)

    if answer == "6" :
        restart = False

