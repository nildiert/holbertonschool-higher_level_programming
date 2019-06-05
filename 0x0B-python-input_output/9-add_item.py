#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

new_list = []

try:
    my_set = load_from_json_file("add_item.json")
    for my_item in my_set:
        new_list.append(my_item)
except:
    pass

for args in argv[1:]:
    new_list.append(str(args))


save_to_json_file(new_list, "add_item.json")
