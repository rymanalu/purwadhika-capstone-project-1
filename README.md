# Purwadhika Capstone Project Module 1: Contacts Book

## Description

This is a simple command-line contacts management application built with Python. It allows users to store, view, add, update, and delete contact information.

## Features

- View all contacts
- Add new contacts
- Update existing contacts
- Delete contacts
- Search for contacts by name or phone number
- Data persistence (saves contacts to a CSV file)

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory.

## Setup

1. The application uses a file named `contacts.csv` to store contact data.
2. A sample file named `contacts.example.csv` is provided with dummy data.
3. To start with this sample data, copy `contacts.example.csv` and rename it to `contacts.csv`:

```
cp contacts.example.csv contacts.csv
```

4. If you don't copy the example file, a new `contacts.csv` will be created when you add your first contact.

## Usage

Run the application by executing the main script:

```
python main.py
```

Follow the on-screen prompts to navigate through the application:

1. View Contacts: Display all stored contacts
2. Add Contact: Add a new contact to the list
3. Update Contact: Modify an existing contact's information
4. Delete Contact: Remove a contact from the list
5. Exit: Save changes and close the application

## Data Storage

Contacts are stored in `contacts.csv` in the same directory as the application. This file is created automatically if it doesn't exist, or you can initialize it with the provided example data as described in the Setup section.

## Contributing

This is a simple project for educational purposes. Feel free to fork and modify as needed.

## License

This project is open source and available under the [MIT License](LICENSE).
