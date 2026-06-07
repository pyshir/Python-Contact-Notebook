import time
import sys

loader = {} # Data will load temporary at here to make operations
# Main functions
def load_data():
    with open('notebook.csv', 'r') as f:
        next(f)
        for i in f:
            x,y = i.strip().split(',')
            loader[x] = y

def write_data():
    with open('notebook.csv', 'w') as f:
        f.write(f'Name,Phone\n')
        for i,j in loader.items():
            count = 0
            f.write(f'{i},{j}')
            if count <= len(loader) - 1:
                f.write(f'\n')
            count += 1

def add_data(x,y):
    load_data()
    for i,j in loader.items():
        if i == x or j == y:
            print('Name or Phone already exist!')
            sys.exit()
    loader[x] = y
    write_data()
    print('Contact successfully added!')

def delete_data(x, y):
    load_data()
    count = 0
    for i,j in loader.items():
        if i == x and j == y:
            del loader[i]
            write_data()
            print(f'{i} Removed from Notebook successfully!')
            sys.exit()
        else:
            count += 1
    if count == len(loader):
        print(f'{x} not found in the Notebook')

def search_data(x):
    load_data()
    if x in loader:
        print(loader[x])
    else:
        print(f'{x} is not in the Notebook')

def edit_data(x,y):
    load_data()
    count = 0
    for i,j in loader.items():
        if i == x and j == y:
            new_number = input('Enter NEW phone number\n=')
            for i,j in loader.items():
                if j == new_number:
                    print('Number already exist, Try with different number')
                    sys.exit()
            print('Phone Number is Changing..')
            time.sleep(3)
            loader[x] = new_number
            write_data()
            print('Phone Number has been Changed Successfully!')
            sys.exit()
        else:
            count += 1

    if count == len(loader):
        print(f'{x} not found in the Notebook')




if __name__ == '__main__':
    operation = input('1.Add contact\n2.Delete contact\n3.Search contact\n4.Change Number\n=')

    if operation == '1':
        contact_name = input('Enter Contact Name\n=')
        phone = input('Enter Phone Number\n=')
        add_data(contact_name,phone)

    elif operation == '2':
        contact_name = input('Enter Contact Name\n=')
        phone = input('Enter Phone Number\n=')
        delete_data(contact_name, phone)

    elif operation == '3':
        contact_name = input('Enter Contact Name\n=')
        search_data(contact_name)

    elif operation == '4':
        contact_name = input('Enter Contact Name\n=')
        phone = input('Enter OLD Phone Number\n=')
        edit_data(contact_name,phone)
