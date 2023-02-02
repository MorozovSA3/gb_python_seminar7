import controller
import view

def add_record():
    catalog = open('catalog.txt', mode='a', encoding='utf-8')
    catalog.write(controller.data_for_record())
    catalog.close()
    view.record_success()

def catalog_output():
    catalog = open('catalog.txt', mode='r', encoding='utf-8')
    all_records = catalog.read()
    catalog.close()
    return all_records

def search_by_name():
    catalog = open('catalog.txt', mode='r', encoding='utf-8')
    all_records = catalog.readlines()
    name_to_search = controller.name_to_search()
    filt_records = list(filter(lambda record: record.split(';')[0] == name_to_search, all_records))
    search_result = all_records[0]
    for i in filt_records:
        search_result += i
    view.show_filtered_catalog(search_result)

def menu_action():
    act_number = controller.input_option()
    if act_number == '1':
        add_record()
    elif act_number == '2':
        view.print_catalog(catalog_output())
    elif act_number == '3':
        search_by_name()