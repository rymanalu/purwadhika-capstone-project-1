import csv

fieldnames = ['id', 'name', 'phone', 'address',
              'email', 'website', 'categories']


def save_contacts(contacts, filename='contacts.csv'):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for contact in contacts.values():
                contact_copy = contact.copy()
                contact_copy['categories'] = ','.join(
                    contact_copy['categories'])
                writer.writerow(contact_copy)
    except IOError as e:
        print(f"An error occurred while saving contacts: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
