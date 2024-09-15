from .view import __do_search_by_phone
import utils.input_utils as input_utils
import utils.ui_utils as ui_utils


def update_contact_menu(contacts, name_index, phone_index):
    """
    Display the update contact menu and handle user choices.

    Args:
        contacts (dict): Dictionary of all contacts.
        name_index (defaultdict): Index of contacts by name.
        phone_index (defaultdict): Index of contacts by phone number.
    """
    while True:
        ui_utils.clear_screen()
        ui_utils.print_header("Update Contact")
        ui_utils.print_menu(["Update", "Back to main menu"])

        choice = input_utils.get_validated_input(
            "Enter your choice (1-2): ",
            lambda x: x in ["1", "2"],
            "Invalid choice. Please enter 1 or 2."
        )

        if choice == "1":
            __update_contact(contacts, name_index, phone_index)
        else:
            break


def __update_contact(contacts, name_index, phone_index):
    """
    Update an existing contact in the contacts dictionary and update indexes.

    Args:
        contacts (dict): Dictionary of all contacts.
        name_index (defaultdict): Index of contacts by name.
        phone_index (defaultdict): Index of contacts by phone number.
    """
    ui_utils.clear_screen()
    ui_utils.print_header("Update Contact")
    contact_id = input_utils.input_contact_id(
        "Enter the ID of the contact to update: ")

    if ui_utils.print_no_contacts_found(contacts, contact_id):
        return

    ui_utils.clear_screen()
    ui_utils.print_header("Update Contact")
    old_contact = contacts[contact_id]
    updated_contact = old_contact.copy()

    # Update contact information
    phone = input_utils.input_phone(updated_contact["phone"])
    matching_contacts = __do_search_by_phone(
        phone, contacts, phone_index, True)

    if any(contact["id"] != contact_id for contact in matching_contacts):
        print("Contact with this phone number already exists.")
        input_utils.input_continue()
        return

    updated_contact.update({
        "phone": phone,
        "name": input_utils.input_name(updated_contact["name"]),
        "address": input_utils.input_address(updated_contact["address"]),
        "email": input_utils.input_email(updated_contact["email"]),
        "website": input_utils.input_website(updated_contact["website"]),
        "categories": input_utils.input_categories(updated_contact["categories"])
    })

    # Preview and confirm
    ui_utils.clear_screen()
    ui_utils.print_header("Preview of Updated Contact")
    ui_utils.print_contact(updated_contact)

    if input_utils.confirm_action("Save?"):
        # Update name index if name changed
        if updated_contact["name"].lower() != old_contact["name"].lower():
            old_name_key = old_contact["name"].lower()
            new_name_key = updated_contact["name"].lower()
            name_index[old_name_key].remove(contact_id)
            name_index[new_name_key].append(contact_id)
            if not name_index[old_name_key]:
                del name_index[old_name_key]

        # Update phone index if phone changed
        if updated_contact["phone"] != old_contact["phone"]:
            old_phone_key = old_contact["phone"]
            new_phone_key = updated_contact["phone"]
            phone_index[old_phone_key].remove(contact_id)
            phone_index[new_phone_key].append(contact_id)
            if not phone_index[old_phone_key]:
                del phone_index[old_phone_key]

        contacts[contact_id] = updated_contact
        print("\nContact updated successfully!")
        input_utils.input_continue()
