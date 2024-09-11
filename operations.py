import csv
import os
from utils.input_utils import confirm_action, get_validated_input, input_contact
from utils.ui_utils import print_contact, print_contact_pagination, print_header


def add_contact(contacts, name_index):
    print_header("Add New Contact")

    new_id = max(contacts.keys(), default=0) + 1

    new_contact = input_contact()
    new_contact["id"] = new_id

    contacts[new_id] = new_contact

    name_key = new_contact["name"].lower()
    if name_key in name_index:
        name_index[name_index].append(new_id)
    else:
        name_index[name_key] = [new_id]

    print("\nContact added successfully! New Contact Details:")
    print_contact(new_contact)


def delete_contact(contacts, name_index):
    print_header("Delete Contact")

    if not contacts:
        print("No contacts available to delete.")
        return

    contact_id = get_validated_input(
        "Enter the ID of the contact to delete: ",
        lambda x: x.isdigit() and int(x) in contacts,
        "Invalid ID. Please enter a valid contact ID."
    )
    contact_id = int(contact_id)

    contact = contacts[contact_id]
    print("\nContact to be deleted:")
    print_contact(contact)

    if not confirm_action("Are you sure you want to delete this contact?"):
        print("Deletion cancelled.")
        return

    name_key = contact['name'].lower()
    name_index[name_key].remove(contact_id)
    if not name_index[name_key]:
        del name_index[name_key]

    del contacts[contact_id]
    print(f"\nContact with ID {contact_id} has been successfully deleted.")


def load_contacts():
    contacts = {}
    name_index = {}
    csv_file = "contacts.csv"

    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "phone", "address",
                            "email", "website", "categories"])
        return contacts, name_index

    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            contact_id = int(row["id"])
            row["id"] = contact_id
            row["categories"] = row["categories"].split(
                ",") if row["categories"] else []

            contacts[contact_id] = row

            name_key = row["name"].lower()
            if name_key in name_index:
                name_index[name_key].append(contact_id)
            else:
                name_index[name_key] = [contact_id]

    return contacts, name_index


def search_contacts(contacts, name_index):
    print_header("Search Contacts")

    search_term = get_validated_input("Enter search term: ", lambda x: len(
        x.strip()) > 0, "Search term cannot be empty")

    results = []

    for name, ids in name_index.items():
        if search_term in name:
            results.extend([contacts[id] for id in ids])

    for contact in contacts.values():
        if contact not in results:  # Avoid duplicates
            if (search_term in contact["phone"].lower() or
                search_term in contact["email"].lower() or
                any(search_term in category.lower() for category in contact["categories"])):
                results.append(contact)

    if not results:
        print("No matching contacts found.")
        return

    print(f"\n Found {len(results)} matching contacts:")
    print_contact_pagination(results, "Search Results")


def update_contact(contacts, name_index):
    print_header("Update Contact")

    contact_id = get_validated_input("Enter the ID of the contact to update: ", lambda x: x.isdigit(
    ) and int(x) in contacts, "Invalid ID. Please enter a valid contact ID.")
    contact_id = int(contact_id)

    contact = contacts[contact_id]
    print("\nCurrent contact details:")
    print_contact(contact)

    updated_contact = input_contact(contact)

    if updated_contact["name"].lower() != contact["name"].lower():
        old_name_key = contact["name"].lower()
        new_name_key = updated_contact["name"].lower()
        name_index[old_name_key].remove(contact_id)
        if not name_index[old_name_key]:
            del name_index[old_name_key]
        if new_name_key in name_index:
            name_index[new_name_key].append(contact_id)
        else:
            name_index[new_name_key] = [contact_id]

    contacts[contact_id] = updated_contact

    print("\nContact updated successfully. New details:")
    print_contact(updated_contact)


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    contacts_list = list(contacts.values())
    print_contact_pagination(contacts_list, "View Contacts")
