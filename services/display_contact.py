def display_contact(contact):
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
