from utils.input_utils import get_validated_input, get_valid_search_term, input_continue, input_contact_id
import utils.ui_utils as ui_utils


def view_contacts_menu(contacts, name_index, phone_index):
    """
    Display the view contacts menu and handle user choices.

    Args:
        contacts (dict): Dictionary of all contacts.
        name_index (defaultdict): Index of contacts by name.
        phone_index (defaultdict): Index of contacts by phone number.
    """
    while True:
        ui_utils.clear_screen()
        ui_utils.print_header("View Contacts")
        ui_utils.print_menu([
            "List all contacts", "Search by ID", "Search by name",
            "Search by phone number", "Back to main menu"
        ])

        choice = get_validated_input(
            "Enter your choice (1-5): ",
            lambda x: x.isdigit() and 1 <= int(x) <= 5,
            "Invalid choice. Please enter a number between 1 and 5."
        )

        actions = {
            "1": lambda: __list_all_contacts(contacts),
            "2": lambda: __search_by_id(contacts),
            "3": lambda: __search_by_name(contacts, name_index),
            "4": lambda: __search_by_phone(contacts, phone_index),
            "5": None
        }

        action = actions.get(choice)
        if action:
            action()
        else:
            break


def __list_all_contacts(contacts):
    """List all contacts if any exist."""
    if not ui_utils.print_no_contacts_found(contacts):
        ui_utils.print_contact_pagination(
            list(contacts.values()), "All contacts")


def __search_by_id(contacts):
    """Search for a contact by ID."""
    if ui_utils.print_no_contacts_found(contacts):
        return

    contact_id = input_contact_id("Enter the ID of the contact to view: ")
    if not ui_utils.print_no_contacts_found(contacts, contact_id):
        ui_utils.clear_screen()
        ui_utils.print_header("Contact Details")
        ui_utils.print_contact(contacts[contact_id])
        input_continue()


def __search_by_name(contacts, name_index):
    """Search for contacts by name."""
    if ui_utils.print_no_contacts_found(contacts):
        return

    search = get_valid_search_term("Enter name to search: ").lower()
    matching_ids = {id for name, ids in name_index.items()
                    if search in name for id in ids}
    matching_contacts = [contacts[id] for id in matching_ids]

    if not ui_utils.print_no_contacts_found(matching_contacts):
        ui_utils.print_contact_pagination(
            matching_contacts, f"Contacts matching '{search}'")


def __search_by_phone(contacts, phone_index):
    """Search for contacts by phone number."""
    if ui_utils.print_no_contacts_found(contacts):
        return

    search = get_valid_search_term("Enter phone number to search: ")
    matching_contacts = __do_search_by_phone(search, contacts, phone_index)

    if not ui_utils.print_no_contacts_found(matching_contacts):
        ui_utils.print_contact_pagination(
            matching_contacts, f"Contacts matching phone '{search}'")


def __do_search_by_phone(search, contacts, phone_index, exact=False):
    """
    Perform a search by phone number.

    Args:
        search (str): The phone number to search for.
        contacts (dict): Dictionary of all contacts.
        phone_index (defaultdict): Index of contacts by phone number.
        exact (bool): Whether to perform an exact match or partial match.

    Returns:
        list: List of matching contacts.
    """
    if exact:
        matching_ids = set(phone_index[search])
    else:
        matching_ids = {id for phone, ids in phone_index.items()
                        if search in phone for id in ids}

    return [contacts[id] for id in matching_ids]
