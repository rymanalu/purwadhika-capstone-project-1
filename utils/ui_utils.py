import os
from .input_utils import input_continue


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_contact(contact):
    print(f"\nID: {contact["id"]}")
    print(f"Name: {contact["name"]}")
    print(f"Phone: {contact["phone"]}")
    if contact["address"]:
        print(f"Address: {contact["address"]}")
    if contact["email"]:
        print(f"Email: {contact["email"]}")
    if contact["website"]:
        print(f"Website: {contact["website"]}")
    if contact["categories"]:
        print(f"Categories: {", ".join(contact["categories"])}")
    print("-" * 60)


def print_contact_pagination(contacts, header, page_size=5):
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
        print("[n] Next Page")
        print("[p] Previous Page")
        print("[q] Return to Previous Menu")

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
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)


def print_menu(options):
    for i, option in enumerate(options, 1):
        print(f"[{i}] {option}")
