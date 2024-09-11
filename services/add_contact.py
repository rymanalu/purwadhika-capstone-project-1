from services.display_contact import display_contact
from utils.input_utils import get_validated_input
from utils.ui_utils import print_header


def add_contact(contacts, name_index):
    print_header("Add New Contact")

    new_id = max(contacts.keys(), default=0) + 1

    name = get_validated_input(
        "Enter name: ", lambda x: x.strip() != "", "Name cannot be empty.")
    phone = get_validated_input("Enter phone number: ", lambda x: x.replace(
        "-", "").isdigit(), "Invalid phone number. Please enter digits only.")
    address = input("Enter address (optional): ")
    email = get_validated_input(
        "Enter email (optional): ", lambda x: "@" in x or x == "", "Invalid email format.")
    website = input("Enter website (optional): ")

    categories = []
    while True:
        category = input("Enter a category (or press Enter to finish): ")
        if category == "":
            break
        categories.append(category)

    new_contact = {
        "id": new_id,
        "name": name,
        "phone": phone,
        "address": address,
        "email": email,
        "website": website,
        "categories": categories
    }

    contacts[new_id] = new_contact

    name_key = name.lower()
    if name_key in name_index:
        name_index[name_index].append(new_id)
    else:
        name_index[name_key] = [new_id]

    print("\nContact added successfully!")
    print("\nNew Contact Details:")
    display_contact(new_contact)

    return new_id
