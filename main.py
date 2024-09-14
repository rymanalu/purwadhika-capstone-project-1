import operations
from services.add import add_contact_menu
from services.load import load_contacts
from services.update import update_contact_menu
from services.view import view_contacts_menu
from utils.input_utils import get_validated_input
from utils.ui_utils import clear_screen, print_header, print_menu


def main():
    contacts, name_index, phone_index = load_contacts()

    while True:
        clear_screen()
        print_header("Contacts")
        print_menu(["View", "Add", "Update", "Delete", "Exit"])

        choice = get_validated_input(
            "Enter your choice (1-6): ",
            lambda x: x.isdigit() and 1 <= int(x) <= 6,
            "Invalid choice. Please enter a number between 1 and 6."
        )

        if choice == "1":
            view_contacts_menu(contacts, name_index, phone_index)
        elif choice == "2":
            add_contact_menu(contacts, name_index, phone_index)
        elif choice == "3":
            update_contact_menu(contacts, name_index, phone_index)
        elif choice == "4":
            operations.delete_contact(contacts, name_index)
        elif choice == "6":
            operations.save_contacts(contacts)
            print("Thank you for using Contacts. Goodbye!")
            break


if __name__ == "__main__":
    main()
