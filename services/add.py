from .view import __do_search_by_phone
import utils.input_utils as input_utils
from utils.ui_utils import clear_screen, print_contact, print_header, print_menu


def add_contact_menu(contacts, name_index, phone_index):
    """
    Display the add contact menu and handle user choices.

    Args:
        contacts (dict): Dictionary of all contacts.
        name_index (defaultdict): Index of contacts by name.
        phone_index (defaultdict): Index of contacts by phone number.
    """
    while True:
        clear_screen()
        print_header("Add New Contact")
        print_menu(["Add", "Back to main menu"])

        choice = input_utils.get_validated_input(
            "Enter your choice (1-2): ",
            lambda x: x in ["1", "2"],
            "Invalid choice. Please enter 1 or 2."
        )

        if choice == "1":
            __add_new_contact(contacts, name_index, phone_index)
        else:
            break


def __add_new_contact(contacts, name_index, phone_index):
    """
    Add a new contact to the contacts dictionary and update indexes.

    Args:
        contacts (dict): Dictionary of all contacts.
        name_index (defaultdict): Index of contacts by name.
        phone_index (defaultdict): Index of contacts by phone number.
    """
    clear_screen()
    print_header("Add New Contact")

    # Get phone number and check for existing contacts
    phone = input_utils.input_phone()
    matching_contacts = __do_search_by_phone(
        phone, contacts, phone_index, True)

    if matching_contacts:
        print("Contact already exists.")
        input_utils.input_continue()
        return

    # Create new contact
    new_id = max(contacts.keys(), default=0) + 1
    new_contact = {
        "id": new_id,
        "phone": phone,
        "name": input_utils.input_name(),
        "address": input_utils.input_address(),
        "email": input_utils.input_email(),
        "website": input_utils.input_website(),
        "categories": input_utils.input_categories()
    }

    # Preview and confirm
    clear_screen()
    print_header("Preview of New Contact")
    print_contact(new_contact)

    if input_utils.confirm_action("Save?"):
        # Update indexes and contacts dictionary
        name_index[new_contact["name"].lower()].append(new_id)
        phone_index[new_contact["phone"]].append(new_id)
        contacts[new_id] = new_contact

        print("\nContact added successfully!")
        input_utils.input_continue()
