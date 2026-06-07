# Python Contact Notebook

A simple command-line contact management application built with Python. The program stores contacts in a CSV file and allows users to add, search, edit, and delete contacts.

## Features

* Add new contacts
* Search contacts by name
* Update existing phone numbers
* Delete contacts
* Store data in a CSV file
* Prevent duplicate names and phone numbers

## Project Structure

```
.
├── notebook.py
├── notebook.csv
└── README.md
```

## CSV Format

The application stores data in `notebook.csv`.

Example:

```csv
Name,Phone
John,01712345678
Alice,01812345678
```

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

```bash
python notebook.py
```

## Menu

When the program starts, you will see:

```text
1.Add contact
2.Delete contact
3.Search contact
4.Change Number
```

Select an option by entering the corresponding number.

---

### Add Contact

```text
Enter Contact Name
=John

Enter Phone Number
=01712345678
```

Output:

```text
Contact successfully added!
```

---

### Search Contact

```text
Enter Contact Name
=John
```

Output:

```text
01712345678
```

---

### Change Number

```text
Enter Contact Name
=John

Enter OLD Phone Number
=01712345678

Enter NEW phone number
=01987654321
```

Output:

```text
Phone Number has been Changed Successfully!
```

---

### Delete Contact

```text
Enter Contact Name
=John

Enter Phone Number
=01987654321
```

Output:

```text
John Removed from Notebook successfully!
```

## Validation

The application includes the following checks:

* Duplicate contact names are not allowed.
* Duplicate phone numbers are not allowed.
* Users must provide the correct existing phone number before updating or deleting a contact.
* Search notifies the user when a contact does not exist.

## Learning Goals

This project demonstrates:

* Python dictionaries
* File handling
* CSV data storage
* Functions
* Loops and conditional statements
* Basic CRUD operations (Create, Read, Update, Delete)

## Future Improvements

* Use the `csv` module instead of manual file parsing.
* Add input validation for phone numbers.
* Implement exception handling.
* Convert the project into a GUI application.
* Add support for multiple phone numbers.
* Store data using SQLite.

## Author

Created as a Python learning project.
