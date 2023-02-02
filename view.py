
def hello_user():
    print()
    print('Добрый день! Здесь вы можете совершать действия над телефонным справочником')

def create_menu():
    print()
    print('Выберите, пожалуйста, один из пунктов меню:')
    print('1 - Сделать запись в справочник')
    print('2 - Вывод всего справочника')
    print('3 - Поиск по имени')

def option_choice():
    print()
    print('Поле для ввода пункта меню: ', end = '')

def text_for_record(record_type):
    print()
    if record_type == 'name':
        return 'Введите имя абонента: '
    elif record_type == 'surname':
        return 'Введите фамилию абонента: '
    elif record_type == 'phone':
        return 'Введите телефон абонента: '

def record_success():
    print()
    print('Запись успешно добавлена в телефонный справочник!')

def print_catalog(catalog_records):
    print()
    print('Весь телефонный справочник перед вашими глазами:')
    print()
    print(catalog_records)
    
def put_name():
    print()
    print('Введите имя для поиска в справочнике: ', end='')

def show_filtered_catalog(filtered_catalog):
    print()
    print('Абоненты, удовлетворяющие вашему поиску:')
    print()
    print(filtered_catalog)