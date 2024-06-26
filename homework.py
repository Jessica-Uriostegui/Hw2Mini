
# Make a function for adding new contacts. Having unique key, 
# to check for existing contact.
contacts = {}

def add_contact():
    unique_key = input("Please enter contact phone number: only use numbers 0-9 no dashes \n")
    if unique_key in contacts:
        print("This contact already exists")
        return
    name = input("Add new contact name:  \n")
    phone_number = input("Add new contact phone number: xxx-xxx-xxxx use this format \n")
    email = input("Add new contact email:  \n")
    # udpate contacts
    contacts[unique_key] = {"Name": name, "Phone number": phone_number, "Email": email}
    print("Contact info update!")
# Make a function to edit existing contact
def edit_contact():
    unique_key = input("Enter the phone number of contact to edit: only use numbers 0-9 no dashes \n ")
    if unique_key not in contacts:
        print("Contact does not exist")
        return
    name = input("Enter the new name: \n")
    phone_number = input("Enter the new phone number: xxx-xxx-xxxx use this format \n ")
    email = input("Enter the new email: \n")
    #update contact
    contacts[unique_key] = {"Name": name, "Phone number": phone_number, "Email": email}
    print("Your contact has been updated")
# make a function to delete a contact using unique_key to locate.
def delete_contact():
    unique_key = input("Enter contact phone number that you would like to delete: only use numbers 0-9 no dashes \n")
    if unique_key in contacts:
# delete contact by using unique_key
        del contacts[unique_key]
        print("Contact has been deleted")
    else:
        print("Contact does not exist")
# make function to search contacts using unique_key
def search_contacts(): 
    search_contact = input("Enter phone number of contact to search: only use numbers 0-9 no dashes\n")
    if search_contact in contacts:
        contact = contacts[search_contact]
        print(f"Name: {contact["Name"]}, Phone number: {contact["Phone number"]}, Email: {contact["Email"]}")
    else:
        print("That contact does not exist")
# make function for displaying all contacts
def display_contacts():
    if contacts:
        for unique_key, contact in contacts.items():
            print(f"ID: {unique_key}, Name: {contact["Name"]}, Phone number: {contact["Phone number"]}, Email: {contact["Email"]}")
    else:
        print("No contacts available")  
# make a function to export contacts into a text file
def export_contacts():
    with open ("contact_directory.txt", "w") as file:
        for unique_key, contact in contacts.items():
            file.write(f"{unique_key},{contact["Name"]},{contact["Phone number"]},{contact["Email"]}\n")
    print("Your contacts have been exported")  
# make a function to import a text file
def import_contacts():
    try:
        with open("contact_directory.txt", "r") as file:
            for line in file:
                unique_key, name, phone_number, email = line.strip().split(",")
                contacts[unique_key] = {"Name": name, "Phone number": phone_number, "Email": email}
        print("Your contacts have been imported")
       
    except FileNotFoundError:
        print("File not found.")
     
# Function to run program main()
def main():
    # greeting and menu
    a ="""
    Hello welcome to Contact Manager 
    """ 
    b = """
    1. Add a new contact
    2. Edit an existing contact
    3. Delet a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file 
    8. Quit
    """
    print(a)
    print(b)
    print("************************************ \n")

    # While loop created to let user keep choosen until they decide to quit
    while True:
        choice = input("Please select an option:  \n")
        if choice == "1":
            add_contact()
            print(b)
        elif choice == "2":
            edit_contact()
            print(b)
        elif choice == "3":
            delete_contact()
            print(b)
        elif choice == "4":
            search_contacts()
            print(b)
        elif choice == "5":
            display_contacts()
            print(b)
        elif choice == "6":
            export_contacts()
            print(b)
        elif choice == "7":
            import_contacts()
            print(b)
        elif choice == "8":
            print("Have a great day, goodbye.")
            break
        else:
            print("Invalid choice, please try again.")
            print(b)
        
main()   
       


