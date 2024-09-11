def confirm_action(prompt):
    while True:
        response = input(f"{prompt} (y/n): ").lower().strip()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Please answer with 'y' or 'n'.")


def get_validated_input(prompt, validator=None, error_message="Invalid input. Please try again."):
    while True:
        value = input(prompt)
        if validator is None or validator(value):
            return value
        print(error_message)


def input_address(current_value=""):
    prompt = "Enter address (optional): " if not current_value else f"Enter new address (or press Enter to keep '{
        current_value}'): "
    return input(prompt) or current_value


def input_categories(current_categories=None):
    if current_categories:
        print("Current categories:", ', '.join(current_categories))
    print("Enter categories (press Enter after each category, press Enter twice to finish):")
    categories = []
    while True:
        category = input()
        if category == "":
            break
        categories.append(category)
    return categories if categories else (current_categories or [])


def input_contact(contact=None):
    if contact is None:
        contact = {}

    contact["name"] = input_name(contact.get("name", ""))
    contact["phone"] = input_phone(contact.get("phone", ""))
    contact["address"] = input_address(contact.get("address", ""))
    contact["email"] = input_email(contact.get("email", ""))
    contact["website"] = input_website(contact.get("website", ""))
    contact["categories"] = input_categories(contact.get("categories", []))

    return contact


def input_email(current_value=""):
    prompt = "Enter email (optional): " if not current_value else f"Enter new email (or press Enter to keep '{
        current_value}'): "
    error_msg = "Invalid email format."
    def validator(x): return '@' in x or x == ""
    return get_validated_input(prompt, validator, error_msg) or current_value


def input_name(current_value="", required=True):
    prompt = "Enter name: " if not current_value else f"Enter new name (or press Enter to keep '{
        current_value}'): "

    def validator(x):
        if (not required and x == "") or current_value != "":
            return True
        return len(x.strip()) > 0 if required else True
    error_msg = "Name cannot be empty." if required else ""
    return get_validated_input(prompt, validator, error_msg) or current_value


def input_phone(current_value="", required=True):
    prompt = "Enter phone number: " if not current_value else f"Enter new phone (or press Enter to keep '{
        current_value}'): "

    def validator(x):
        if (not required and x == "") or current_value != "":
            return True
        digits = "".join(filter(str.isdigit, x))
        return 8 <= len(digits) <= 13
    error_msg = "Invalid phone number. Please enter 8 to 13 digits."
    return get_validated_input(prompt, validator, error_msg) or current_value


def input_website(current_value=""):
    prompt = "Enter website (optional): " if not current_value else f"Enter new website (or press Enter to keep '{
        current_value}'): "
    return input(prompt) or current_value
