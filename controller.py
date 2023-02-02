import view
import model

def start():
    view.hello_user()
    view.create_menu()
    model.menu_action()

def input_option():
    view.option_choice()
    return input()

def data_for_record():
    name = input(view.text_for_record('name'))
    surname = input(view.text_for_record('surname'))
    phone = input(view.text_for_record('phone'))
    return f'\n{name};{surname};{phone}'

def name_to_search():
    return input(view.put_name())