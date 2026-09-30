import json

FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


while True:
    print("\n======================")
    print("      CONTACT BOOK")
    print("======================")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        if name.strip() == "":
            print("Contact name cannot be empty.")

        elif phone.strip() == "":
            print("Phone number cannot be empty.")

        elif not phone.isdigit():
            print("Phone number must contain only digits.")

        elif len(phone) != 10:
            print("Phone number must contain 10 digits.")

        else:
            contacts[name] = phone
            save_contacts()

            print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\nYour Contacts:")

            for name, phone in contacts.items():
                print("Name:", name)
                print("Phone:", phone)
                print("----------------")

    # Search Contact
    elif choice == "3":
        name = input("Enter contact name to search: ")

        if name.strip() == "":
            print("Contact name cannot be empty.")

        elif name in contacts:
            print("\nContact Found!")
            print("Name:", name)
            print("Phone:", contacts[name])

        else:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name.strip() == "":
            print("Contact name cannot be empty.")

        elif name in contacts:
            new_phone = input("Enter new phone number: ")

            if new_phone.strip() == "":
                print("Phone number cannot be empty.")

            elif not new_phone.isdigit():
                print("Phone number must contain only digits.")

            elif len(new_phone) != 10:
                print("Phone number must contain 10 digits.")

            else:
                contacts[name] = new_phone
                save_contacts()

                print("Contact updated successfully!")

        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name.strip() == "":
            print("Contact name cannot be empty.")

        elif name in contacts:
            del contacts[name]
            save_contacts()

            print("Contact deleted successfully!")

        else:
            print("Contact not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")