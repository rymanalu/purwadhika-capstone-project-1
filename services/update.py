from .view import __do_search_by_phone
import utils.input_utils as input_utils
import utils.ui_utils as ui_utils


def update_contact_menu(contacts, name_index, phone_index):
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
    ui_utils.clear_screen()
    ui_utils.print_header("Update Contact")
    contact_id = input_utils.get_validated_input(
        "Enter the ID of the contact to update: ", lambda x: x.isdigit(), "Invalid ID. Please enter digits only.")
    contact_id = int(contact_id)

    if ui_utils.print_no_contacts_found(contacts, contact_id):
        return

    ui_utils.clear_screen()
    ui_utils.print_header(f"Update Contact by ID: {contact_id}")
    old_contact = contacts[contact_id]
    updated_contact = old_contact.copy()

    phone = input_utils.input_phone(updated_contact["phone"])
    matching_contacts = __do_search_by_phone(
        phone, contacts, phone_index, True)

    if matching_contacts:
        for matching_contact in matching_contacts:
            if contact_id != matching_contact["id"]:
                print("Contact already exists.")
                input_utils.input_continue()
                return

    updated_contact["phone"] = phone
    updated_contact["name"] = input_utils.input_name(updated_contact["name"])
    updated_contact["address"] = input_utils.input_address(
        updated_contact["address"])
    updated_contact["email"] = input_utils.input_email(
        updated_contact["email"])
    updated_contact["website"] = input_utils.input_website(
        updated_contact["website"])
    updated_contact["categories"] = input_utils.input_categories(
        updated_contact["categories"])

    ui_utils.clear_screen()
    ui_utils.print_header("Preview of Updated Contact")
    ui_utils.print_contact(updated_contact)
    confirmed = input_utils.confirm_action("Save?")

    if confirmed:
        if updated_contact["name"].lower() != old_contact["name"].lower():
            old_name_key = old_contact["name"].lower()
            name_index[old_name_key].remove(contact_id)
            name_index[updated_contact["name"].lower()].append(contact_id)

            if not name_index[old_name_key]:
                del name_index[old_name_key]

        if updated_contact["phone"] != old_contact["phone"]:
            old_phone_key = old_contact["phone"]
            phone_index[old_phone_key].remove(contact_id)
            phone_index[updated_contact["phone"]].append(contact_id)

            if not phone_index[old_phone_key]:
                del phone_index[old_phone_key]

        contacts[contact_id] = updated_contact

        print("\nContact updated successfully!")
        input_utils.input_continue()
