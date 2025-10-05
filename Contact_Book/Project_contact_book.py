

import json
class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name:{self.name}, phone: {self.phone}, Email:{self.email}"
    

class ContactBook:
    def __init__(self):
        self.contacts = {} #Store contacts in a dictonary 
    
    def add_contact(self, name, phone, email):
        self.contacts[name] = Contact(name, phone, email)
        print(f"Contact '{name}' added Sucessfully")

    def view_contacts(self):
        if not self.contacts:
            print("No contact found!")
        else:
            for contact in self.contacts.values():
                print(contact)
    
    def search_contacts(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print("contact not found!")
    
    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            print("Contact '{name}' updated successfully!")

        else:
            print("Contact info not found")
        
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found!")
    
    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump( {name: vars(contact) for name,contact in self.contacts.items()}, file)
            print("Contacts saved successfully!")
    

    def load_from_file(self, filename="contact.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.contacts = {name: Contact(**info) for name, info in data.items()}
                print("Contacts loaded successfully!")
        except FileNotFoundError:
            print("No saved contacts found!")
#  creating the Main Menu:


def main():

    contact_book = ContactBook()
    contact_book.load_from_file()   #Load contacts if avaliable

    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")
        choice = input("Choose an option: ")


        if choice == "1":
            name  = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)


        elif choice == "2":
            contact_book.view_contacts()


        elif choice == "3":
            name = input("Enter name to search: ")
            contact_book.search_contacts(name)


        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contact_book.update_contact(name, phone if phone else None, email if email else None)

        elif choice == "5":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == "6":
            contact_book.save_to_file()
            print("Exiting from Contact Book. Have a great day!")
            break

        else:
            print("Invaid option! Please choose a valid option.")


if __name__ == "__main__":
    main()