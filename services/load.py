from collections import defaultdict
import csv
import os


fieldnames = ["id", "name", "phone", "address",
              "email", "website", "categories"]


def load_contacts(filename="contacts.csv"):
    contacts = {}
    name_index = defaultdict(list)
    phone_index = defaultdict(list)

    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(fieldnames)
        return contacts, name_index, phone_index

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            contact_id = int(row["id"])
            row["id"] = contact_id
            row["categories"] = row["categories"].split(
                ',') if row["categories"] else []

            contacts[contact_id] = row
            name_index[row["name"].lower()].append(contact_id)
            phone_index[row["phone"]].append(contact_id)

    return contacts, name_index, phone_index
