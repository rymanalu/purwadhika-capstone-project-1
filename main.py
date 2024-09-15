from services.add import add_contact_menu
from services.delete import delete_contact_menu
from services.export_import import load_contacts, save_contacts
from services.update import update_contact_menu
from services.view import view_contacts_menu
from utils.input_utils import get_validated_input
from utils.ui_utils import clear_screen, print_header, print_menu


def main():
    """
    Main function to run the Contacts application.
    Handles the main menu and user interactions.
    """
    contacts, name_index, phone_index = load_contacts()

    menu_options = {
        "1": ("View", lambda: view_contacts_menu(contacts, name_index, phone_index)),
        "2": ("Add", lambda: add_contact_menu(contacts, name_index, phone_index)),
        "3": ("Update", lambda: update_contact_menu(contacts, name_index, phone_index)),
        "4": ("Delete", lambda: delete_contact_menu(contacts, name_index, phone_index)),
        "5": ("Exit", None)
    }

    while True:
        clear_screen()
        print_header("Contacts")
        print_menu([option[0] for option in menu_options.values()])

        choice = get_validated_input(
            "Enter your choice (1-5): ",
            lambda x: x in menu_options,
            "Invalid choice. Please enter a number between 1 and 5."
        )

        action = menu_options[choice][1]

        if action:
            action()
        else:
            save_contacts(contacts)
            print("Thank you for using Contacts. Goodbye!")
            break


if __name__ == "__main__":
    main()
