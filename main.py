import operations
from utils.input_utils import get_validated_input
from utils.ui_utils import clear_screen, print_header, print_menu


def main():
    contacts, name_index = operations.load_contacts()
    menu_options = ["Add", "View", "Update", "Delete", "Search", "Exit"]

    while True:
        clear_screen()
        print_header("Contacts")
        print_menu(menu_options)

        choice = get_validated_input(
            "Enter your choice (1-6): ",
            lambda x: x.isdigit() and 1 <= int(x) <= 6,
            "Invalid choice. Please enter a number between 1 and 6."
        )

        if choice == "1":
            operations.add_contact(contacts, name_index)
        elif choice == "2":
            operations.view_contacts(contacts)
        elif choice == "3":
            operations.update_contact(contacts, name_index)
        elif choice == "4":
            # delete
            pass
        elif choice == "5":
            operations.search_contacts(contacts, name_index)
            pass
        elif choice == "6":
            print("Thank you for using Contacts. Goodbye!")
            break

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
