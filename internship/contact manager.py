contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("\nContact List:")
    for contact in contacts:
        print(f"Name: {contact['name']} | Phone: {contact['phone']}")
    print()


def search_contact():
    search = input("Enter name or phone number to search: ")

    for contact in contacts:
        if contact["name"] == search or contact["phone"] == search:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            print()
            return

    print("Contact not found.\n")


def update_contact():
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address:")
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


while True:
    print("===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Manager!")
        break
    else:
        print("Invalid choice. Please try again.\n")
