def confirm_action(prompt):
    """
    Ask for user confirmation with a yes/no prompt.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        bool: True if the user confirms, False otherwise.
    """
    while True:
        response = input(f"{prompt} (y/n): ").lower().strip()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        print("Please answer with 'y' or 'n'.")


def get_validated_input(prompt, validator=None, error_message="Invalid input. Please try again."):
    """
    Get user input and validate it using a provided validator function.

    Args:
        prompt (str): The prompt to display to the user.
        validator (callable, optional): A function to validate the input.
        error_message (str): The message to display if validation fails.

    Returns:
        str: The validated user input.
    """
    while True:
        value = input(prompt)
        if validator is None or validator(value):
            return value
        print(error_message)


def get_valid_search_term(prompt, min_length=3):
    """
    Get a valid search term with a minimum length.

    Args:
        prompt (str): The prompt to display to the user.
        min_length (int): The minimum length of the search term.

    Returns:
        str: The validated search term.
    """
    return get_validated_input(
        prompt,
        lambda x: len(x.strip()) >= min_length,
        f"Search term must be at least {
            min_length} characters long. Please try again."
    )


def input_address(current_value=""):
    """Get user input for address."""
    prompt = "Enter address (optional): " if not current_value else f"Enter new address (or press Enter to keep '{
        current_value}'): "
    return input(prompt) or current_value


def input_categories(current_categories=None):
    """
    Get user input for categories.

    Args:
        current_categories (list, optional): The current list of categories.

    Returns:
        list: The updated list of categories.
    """
    if current_categories:
        print("Current categories:", ", ".join(current_categories))
    print("Enter categories (press Enter after each category, press Enter twice to finish):")
    categories = []
    while True:
        category = input().strip()
        if not category:
            break
        categories.append(category)
    return categories or current_categories or []


def input_contact_id(prompt="Enter contact ID: "):
    """Get and validate a contact ID from user input."""
    return int(get_validated_input(
        prompt,
        lambda x: x.isdigit(),
        "Invalid ID. Please enter digits only."
    ))


def input_continue(message="Press Enter to continue..."):
    """Prompt the user to continue."""
    input(message)


def input_email(current_value=""):
    """Get and validate an email address from user input."""
    prompt = "Enter email (optional): " if not current_value else f"Enter new email (or press Enter to keep '{
        current_value}'): "
    return get_validated_input(
        prompt,
        lambda x: x == "" or "@" in x,
        "Invalid email format."
    ) or current_value


def input_name(current_value="", required=True):
    """Get and validate a name from user input."""
    prompt = "Enter name: " if not current_value else f"Enter new name (or press Enter to keep '{
        current_value}'): "

    def validator(x):
        return (not required and x == "") or (x == "" and current_value) or len(x.strip()) > 0
    error_msg = "Name cannot be empty." if required else ""
    return get_validated_input(prompt, validator, error_msg) or current_value


def input_phone(current_value="", required=True):
    """Get and validate a phone number from user input."""
    prompt = "Enter phone number: " if not current_value else f"Enter new phone (or press Enter to keep '{
        current_value}'): "

    def validator(x):
        if (not required and x == "") or (x == "" and current_value):
            return True
        digits = "".join(filter(str.isdigit, x))
        return 8 <= len(digits) <= 13
    error_msg = "Invalid phone number. Please enter 8 to 13 digits."
    return get_validated_input(prompt, validator, error_msg) or current_value


def input_website(current_value=""):
    """Get user input for website."""
    prompt = "Enter website (optional): " if not current_value else f"Enter new website (or press Enter to keep '{
        current_value}'): "
    return input(prompt) or current_value
