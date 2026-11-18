def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Give me name and phone please."


def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    except IndexError:
        return "Enter user name."


def change_contact(args, contacts):
    try:
        name, new_number = args
        if name in contacts:
            contacts[name] = new_number
            return 'Contact updated.'
        else:
            return 'Contact not found.'
    except ValueError:
        return "Give me name and phone please."


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


def main():
    print('Welcome to the assistant bot!')
    exit_commands = ['exit', 'close']
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
        command, *args = parse_input(user_input)
        if command in exit_commands:
            print("Good bye!")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

