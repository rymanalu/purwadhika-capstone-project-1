from utils.contact_utils import load_contacts
from utils.input_utils import get_validated_input
from utils.ui_utils import clear_screen


def main():
    contacts, name_index = load_contacts()

    while True:
        clear_screen()
        break


if __name__ == "__main__":
    main()
