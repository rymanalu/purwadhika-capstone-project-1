import os
from .input_utils import input_continue


def clear_screen():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_contact(contact):
    """
    Print details of a single contact.

    Args:
        contact (dict): The contact information to print.
    """
    print(f"\nID: {contact["id"]}")
    print(f"Name: {contact["name"]}")
    print(f"Phone: {contact["phone"]}")
    for field in ["address", "email", "website"]:
        if contact[field]:
            print(f"{field.capitalize()}: {contact[field]}")
    if contact["categories"]:
        print(f"Categories: {", ".join(contact["categories"])}")
    print("-" * 60)


def print_contact_pagination(contacts, header, page_size=5):
    """
    Print contacts with pagination.

    Args:
        contacts (list): List of contacts to display.
        header (str): Header text for the contact list.
        page_size (int): Number of contacts to display per page.
    """
    current_page = 0
    contacts_len = len(contacts)
    total_pages = (contacts_len - 1) // page_size + 1

    while True:
        clear_screen()
        print_header(f"{header} (Page {current_page + 1}/{total_pages})")

        start_idx = current_page * page_size
        end_idx = min(start_idx + page_size, contacts_len)

        for contact in contacts[start_idx:end_idx]:
            print_contact(contact)

        print(f"\nShowing results {start_idx + 1}-{end_idx} of {contacts_len}")
        print("\nNavigation:")

        nav_options = []
        if current_page > 0:
            nav_options.append("[p] Previous Page")
        if current_page < total_pages - 1:
            nav_options.append("[n] Next Page")
        nav_options.append("[q] Return to Previous Menu")

        print("\n".join(nav_options))

        choice = input("Enter your choice: ").upper()

        if choice == "N" and current_page < total_pages - 1:
            current_page += 1
        elif choice == "P" and current_page > 0:
            current_page -= 1
        elif choice == "Q":
            break
        else:
            input_continue("Invalid choice. Press Enter to continue...")


def print_header(title):
    """
    Print a formatted header.

    Args:
        title (str): The title to display in the header.
    """
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)


def print_menu(options):
    """
    Print a numbered menu of options.

    Args:
        options (list): List of menu options to display.
    """
    for i, option in enumerate(options, 1):
        print(f"[{i}] {option}")


def print_no_contacts_found(contacts, contact_id=None):
    """
    Check if contacts exist and print a message if none are found.

    Args:
        contacts (dict): Dictionary of contacts.
        contact_id (int, optional): Specific contact ID to check for.

    Returns:
        bool: True if no contacts were found, False otherwise.
    """
    if (contact_id is not None and contact_id not in contacts) or not contacts:
        print("No contacts found.")
        input_continue()
        return True
    return False
