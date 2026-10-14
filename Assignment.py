cbook={}
while (True):
    print("---Welcome to contact management system---")
    print("choose from the following options:")
    print("1.Add contact:")
    print("2.Search contact:")
    print("3.Update contact:")
    print("4.Delete contact:")
    print("5.Display contact:")
    print("6.Exit contact:")
    choice=int(input("enter your choice:"))
    if choice == 1:
        name=input("enter your name:")
        phone=int(input("Enter your phone no:"))
        cbook[name]=phone
        print("added successfully")
    elif choice == 2:
        name=input("Enter name to search: ")
        if name in cbook:
            print("Phone:",cbook[name])
        else:
            print("Contact not found")
    elif choice == 3:
        name=input("Enter name to update:")
        if name in cbook:
            print("phone:",cbook[name])
        else:
            print("Contact not found")
    elif choice == 4:
        name=input("Enter name to delete:")
        if name in cbook:
            del cbook[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")
    elif choice == 5:
        if not cbook:
            print("No contacts found")
        else:
            print("Contact List:")
            for name,phone in cbook.items():
                print("Name:",name)
                print("Phone:",phone)
    elif choice == 6:
        print("Existing contact management system")
        print("Thank you for using the contact management system!!!!")
        break
    else:
        print("Invalid choice! please  try again.")