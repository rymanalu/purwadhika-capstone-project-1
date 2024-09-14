from utils.input_utils import get_validated_input, get_valid_search_term, input_continue
import utils.ui_utils as ui_utils


def view_contacts_menu(contacts, name_index, phone_index):
    while True:
        ui_utils.clear_screen()
        ui_utils.print_header("View Contacts")
        ui_utils.print_menu(["List all contacts", "Search by ID", "Search by name",
                             "Search by phone number", "Back to main menu"])

        choice = get_validated_input(
            "Enter your choice (1-5): ",
            lambda x: x.isdigit() and 1 <= int(x) <= 5,
            "Invalid choice. Please enter a number between 1 and 5."
        )

        if choice == "1":
            __list_all_contacts(contacts)
        elif choice == "2":
            __search_by_id(contacts)
        elif choice == "3":
            __search_by_name(contacts, name_index)
        elif choice == "4":
            __search_by_phone(contacts, phone_index)
        else:
            break


def __list_all_contacts(contacts):
    if ui_utils.print_no_contacts_found(contacts):
        return

    ui_utils.print_contact_pagination(list(contacts.values()), "All contacts")


def __search_by_id(contacts):
    if ui_utils.print_no_contacts_found(contacts):
        return

    contact_id = get_validated_input(
        "Enter ID to search: ", lambda x: x.isdigit(), "Invalid ID. Please enter digits only.")
    contact_id = int(contact_id)

    if ui_utils.print_no_contacts_found(contacts, contact_id):
        return

    ui_utils.clear_screen()
    ui_utils.print_header(f"View Contact by ID: {contact_id}")
    ui_utils.print_contact(contacts[contact_id])
    input_continue()


def __search_by_name(contacts, name_index):
    if ui_utils.print_no_contacts_found(contacts):
        return

    search = get_valid_search_term("Enter name to search: ")
    search_lower = search.lower()
    matching_ids = set()

    for name, ids in name_index.items():
        if search_lower in name:
            matching_ids.update(ids)

    matching_contacts = [contacts[id] for id in matching_ids]

    if ui_utils.print_no_contacts_found(matching_contacts):
        return

    ui_utils.print_contact_pagination(
        matching_contacts, f"Contacts matching '{search}'")


def __search_by_phone(contacts, phone_index):
    if ui_utils.print_no_contacts_found(contacts):
        return

    search = get_valid_search_term("Enter phone number to search: ")
    matching_contacts = __do_search_by_phone(search, contacts, phone_index)

    if ui_utils.print_no_contacts_found(matching_contacts):
        return

    ui_utils.print_contact_pagination(
        matching_contacts, f"Contacts matching phone '{search}'")


def __do_search_by_phone(search, contacts, phone_index, exact=False):
    matching_ids = set()

    if exact:
        matching_ids.update(phone_index[search])
    else:
        for phone, ids in phone_index.items():
            if search in phone:
                matching_ids.update(ids)

    return [contacts[id] for id in matching_ids]
