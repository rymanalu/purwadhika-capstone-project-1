import utils.input_utils as input_utils
import utils.ui_utils as ui_utils


def delete_contact_menu(contacts, name_index, phone_index):
    """
    Display the delete contact menu and handle user choices.

    Args:
        contacts (dict): Dictionary of all contacts.
        name_index (defaultdict): Index of contacts by name.
        phone_index (defaultdict): Index of contacts by phone number.
    """
    while True:
        ui_utils.clear_screen()
        ui_utils.print_header("Delete Contact")
        ui_utils.print_menu(["Delete", "Back to main menu"])

        choice = input_utils.get_validated_input(
            "Enter your choice (1-2): ",
            lambda x: x in ["1", "2"],
            "Invalid choice. Please enter 1 or 2."
        )

        if choice == "1":
            __delete_contact(contacts, name_index, phone_index)
        else:
            break


def __delete_contact(contacts, name_index, phone_index):
    """
    Delete a contact from the contacts dictionary and update indexes.

    Args:
        contacts (dict): Dictionary of all contacts.
        name_index (defaultdict): Index of contacts by name.
        phone_index (defaultdict): Index of contacts by phone number.
    """
    ui_utils.clear_screen()
    ui_utils.print_header("Delete Contact")
    contact_id = input_utils.input_contact_id(
        "Enter the ID of the contact to delete: ")

    if ui_utils.print_no_contacts_found(contacts, contact_id):
        return

    ui_utils.clear_screen()
    ui_utils.print_header("Preview of Deleted Contact")
    deleted_contact = contacts[contact_id]
    ui_utils.print_contact(deleted_contact)

    if input_utils.confirm_action("Delete?"):
        # Remove contact from indexes
        name_key = deleted_contact["name"].lower()
        phone_key = deleted_contact["phone"]

        name_index[name_key].remove(contact_id)
        phone_index[phone_key].remove(contact_id)

        # Clean up empty lists in indexes
        if not name_index[name_key]:
            del name_index[name_key]
        if not phone_index[phone_key]:
            del phone_index[phone_key]

        # Remove contact from main dictionary
        del contacts[contact_id]

        print("\nContact deleted successfully!")
        input_utils.input_continue()
