from utils.input_utils import get_validated_input, get_valid_search_term, input_continue
from utils.ui_utils import clear_screen, print_contact, print_contact_pagination, print_header, print_menu


def view_contacts_menu(contacts, name_index, phone_index):
    menu_options = ["List all contacts", "Search by ID", "Search by name",
                    "Search by phone number", "Back to main menu"]

    while True:
        clear_screen()
        print_header("View Contacts")
        print_menu(menu_options)

        choice = get_validated_input(
            "Enter your choice (1-5): ",
            lambda x: x in ['1', '2', '3', '4', '5'],
            "Invalid choice. Please enter a number between 1 and 5."
        )

        if choice == '1':
            __list_all_contacts(contacts)
            pass
        elif choice == '2':
            __search_by_id(contacts)
        elif choice == '3':
            __search_by_name(contacts, name_index)
        elif choice == '4':
            __search_by_phone(contacts, phone_index)
        else:
            break


def __display_no_contacts_found(contacts):
    if not contacts:
        print("No contacts found.")
        input_continue()
        return True

    return False


def __list_all_contacts(contacts):
    if __display_no_contacts_found(contacts):
        return

    print_contact_pagination(list(contacts.values()), "All contacts")


def __search_by_id(contacts):
    if __display_no_contacts_found(contacts):
        return

    contact_id = get_validated_input(
        "Enter ID to search: ",
        lambda x: x.isdigit() and int(x) in contacts,
        "Invalid ID. Please enter a valid contact ID."
    )
    contact_id = int(contact_id)

    clear_screen()
    print_header(f"View Contact by ID: {contact_id}")
    print_contact(contacts[contact_id])
    input_continue()


def __search_by_name(contacts, name_index):
    if __display_no_contacts_found(contacts):
        return

    search = get_valid_search_term("Enter name to search: ")
    search_lower = search.lower()
    matching_ids = set()

    for name, ids in name_index.items():
        if search_lower in name:
            matching_ids.update(ids)

    matching_contacts = [contacts[id] for id in matching_ids]

    if __display_no_contacts_found(matching_contacts):
        return

    print_contact_pagination(
        matching_contacts, f"Contacts matching '{search}'")


def __search_by_phone(contacts, phone_index):
    if __display_no_contacts_found(contacts):
        return

    search = get_valid_search_term("Enter phone number to search: ")
    matching_ids = set()

    for phone, ids in phone_index.items():
        if search in phone:
            matching_ids.update(ids)

    matching_contacts = [contacts[id] for id in matching_ids]

    if __display_no_contacts_found(matching_contacts):
        return

    print_contact_pagination(
        matching_contacts, f"Contacts matching phone '{search}'")
