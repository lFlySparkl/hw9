# Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.


contacts = {"dima": "0909899", "petr": "9089800"}


def user_error(func):
    def inner(*args):
        # Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error.
        # Цей декоратор відповідає за повернення користувачеві повідомлень виду "Enter user name",
        # "Give me name and phone please" і т.п. Декоратор input_error повинен обробляти винятки,
        # що виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
        try:
            return func(*args)
        except IndexError:
            return "Not enought params. Try again."
        except KeyError:
            return "Uknown rec_id. Try another or use help."
        except ValueError:
            return "Wrong value. Try again."

    return inner


def hello_func(*args):
    # "hello", відповідає у консоль "How can I help you?"
    return "How can I help you?"


@user_error
def add_func(*args):
    # "add ...". За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт.
    #  Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    contact_name = args[0]
    contact_phone = args[1]
    contacts[contact_name] = contact_phone
    return f"Add contact {contact_name = }, {contact_phone = }"


@user_error
def change_func(*args):
    # "change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту.
    # Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    contact_name = args[0]
    new_phone = args[1]
    contact = contacts[contact_name]
    if contact:
        contacts[contact_name] = new_phone
        return f"Change contact {contact_name = }, {new_phone = }"


def phone_func(*args):
    # "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту.
    # Замість ... користувач вводить ім'я контакту, чий номер треба показати.
    contact_name = args[0]
    contact_phone = contacts[contact_name]
    if contact_phone:
        return f"Show contact {contact_name = }, {contact_phone = }"


def show_all_func():
    # "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
    show_all_cont = ""
    for name, phone in contacts.items():
        show_all_cont += f"Name: {name} - Phone: {phone}" + "\n"
    return show_all_cont


def good_bye_func(*args):
    print("Good bye!")
    return exit()


def close_func(*args):
    print("Good bye!")
    return exit()


def exit_func(*args):
    # "good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
    # Бот завершує свою роботу, якщо зустрічає слова: .
    print("Good bye!")
    return exit()


def unknown_comand():
    # Бот приймає команди:
    return "Unknown comand. Try again."


COMANDS = {
    hello_func: "hello",
    add_func: "add",
    change_func: "change",
    phone_func: "phone",
    show_all_func: "show all",
    good_bye_func: "good bye",
    close_func: "close",
    exit_func: "exit",
}


def parcer(text: str):
    for func, kw in COMANDS.items():
        if text.startswith(kw):
            if (
                text == "hello"
                or text == "good bye"
                or text == "close"
                or text == "exit"
            ):
                return func, text
            elif "add" in text or "phone" in text or "change" in text:
                return func, text.replace(kw + " ", "").strip().split()
            else:
                return func, text[len(kw) :].strip().split()
    return unknown_comand, []


def main():
    # Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.
    while True:
        # Бот повинен перебувати в безкінечному циклі, чекаючи команди користувача.
        user_input = input("Write comand:").lower()
        # Бот не чутливий до регістру введених команд.
        func, data = parcer(user_input)
        print(func(*data))


if __name__ == "__main__":
    main()
