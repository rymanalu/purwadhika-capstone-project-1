from collections import defaultdict
import csv
import os

FIELDNAMES = ["id", "name", "phone", "address",
              "email", "website", "categories"]


def load_contacts(filename="contacts.csv"):
    """
    Load contacts from a CSV file and create indexes.

    Args:
        filename (str): Name of the CSV file to load contacts from.

    Returns:
        tuple: (contacts, name_index, phone_index)
            contacts (dict): Dictionary of all contacts.
            name_index (defaultdict): Index of contacts by name.
            phone_index (defaultdict): Index of contacts by phone number.
    """
    contacts = {}
    name_index = defaultdict(list)
    phone_index = defaultdict(list)

    if not os.path.exists(filename):
        return contacts, name_index, phone_index

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            contact_id = int(row["id"])
            row["id"] = contact_id
            row["categories"] = row["categories"].split(
                ",") if row["categories"] else []

            contacts[contact_id] = row
            name_index[row["name"].lower()].append(contact_id)
            phone_index[row["phone"]].append(contact_id)

    return contacts, name_index, phone_index


def save_contacts(contacts, filename="contacts.csv"):
    """
    Save contacts to a CSV file.

    Args:
        contacts (dict): Dictionary of contacts to save.
        filename (str): Name of the CSV file to save contacts to.
    """
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

            for contact in contacts.values():
                contact_copy = contact.copy()
                contact_copy["categories"] = ",".join(
                    contact_copy["categories"])
                writer.writerow(contact_copy)
    except IOError as e:
        print(f"An error occurred while saving contacts: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
