def input_error(func): #декоратор з обробки помилок
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"
    return inner

@input_error
def parse_input(user_input): #розбір команди та аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts): #додавання контакту до словника
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts): #зміна контакту якщо знайдений
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found." #якщо не знайдений - помилка

@input_error
def phone_num(args, contacts): #друк номеру телефону за ім'ям якщо знайдено
    name = args[0]
    if name in contacts:
        return f"{name.capitalize()} phone number is {contacts[name]}."
    else:
        return "Contact not found." #якщо не знайдений - помилка


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                    print(add_contact(args, contacts))
            case "change":
                    print(change_contact(args, contacts))           
            case "phone":
                    print(phone_num(args, contacts))
            case "all":
                for key, value in contacts.items():
                    print(f"{key.capitalize():<10}{value}")
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()

