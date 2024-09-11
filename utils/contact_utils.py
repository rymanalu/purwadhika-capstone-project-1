import csv
import os


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
