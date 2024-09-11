from services.display_contact import display_contact
from utils.ui_utils import clear_screen, print_header


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    contacts_list = list(contacts.values())
    page_size = 5
    current_page = 0
    total_pages = (len(contacts_list) - 1) // page_size + 1

    while True:
        clear_screen()
        print_header(f"View Contacts (Page {current_page + 1}/{total_pages})")

        start_idx = current_page * page_size
        end_idx = min(start_idx + page_size, len(contacts_list))

        for contact in contacts_list[start_idx:end_idx]:
            display_contact(contact)

        print("\nNavigation:")
        print("N - Next Page")
        print("P - Previous Page")
        print("Q - Return to Main Menu")

        choice = input("Enter your choice: ").upper()

        if choice == "N" and current_page < total_pages - 1:
            current_page += 1
        elif choice == "P" and current_page > 0:
            current_page -= 1
        elif choice == "Q":
            break
        else:
            input("Invalid choice. Press Enter to continue...")
