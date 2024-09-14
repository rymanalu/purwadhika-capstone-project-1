import utils.input_utils as input_utils
from utils.ui_utils import clear_screen, print_contact, print_header, print_menu


def delete_contact_menu(contacts, name_index, phone_index):
    while True:
        clear_screen()
        print_header("Delete Contact")
        print_menu(["Delete", "Back to main menu"])

        choice = input_utils.get_validated_input(
            "Enter your choice (1-2): ",
            lambda x: x in ['1', '2'],
            "Invalid choice. Please enter 1 or 2."
        )

        if choice == '1':
            __delete_contact(contacts, name_index, phone_index)
        else:
            break


def __delete_contact(contacts, name_index, phone_index):
    clear_screen()
    print_header("Delete Contact")
    contact_id = input_utils.get_validated_input(
        "Enter the ID of the contact to delete: ", lambda x: x.isdigit(), "Invalid ID. Please enter digits only.")
    contact_id = int(contact_id)

    if not contact_id in contacts:
        print("No contacts found.")
        input_utils.input_continue()
        return

    clear_screen()
    print_header("Preview of Deleted Contact")
    deleted_contact = contacts[contact_id]
    print_contact(deleted_contact)
    confirmed = input_utils.confirm_action("Delete?")

    if confirmed:
        name_key = deleted_contact["name"].lower()
        name_index[name_key].remove(contact_id)
        phone_index[deleted_contact["phone"]].remove(contact_id)

        if not name_index[name_key]:
            del name_index[name_key]

        if not phone_index[deleted_contact["phone"]]:
            del phone_index[deleted_contact["phone"]]

        del contacts[contact_id]

        print("\nContact deleted successfully!")
        input_utils.input_continue()
