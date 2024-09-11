import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title):
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)


def print_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
