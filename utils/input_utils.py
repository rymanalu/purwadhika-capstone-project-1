def get_validated_input(prompt, validator=None, error_message="Invalid input. Please try again."):
    while True:
        value = input(prompt)
        if validator is None or validator(value):
            return value
        print(error_message)
