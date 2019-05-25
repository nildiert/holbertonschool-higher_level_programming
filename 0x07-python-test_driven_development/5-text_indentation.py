#!/usr/bin/python3
def text_indentation(text):
    new_list = []
    la_otra_lista = []
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_str1 = text.replace('.', '.\n\n')
    new_str2 = new_str1.replace('?', '?\n\n')
    new_str1 = new_str2.replace(':', ':\n\n')
    new_str1 = new_str1.strip()
    new_list = new_str1.split("\n")
    for char in new_list:
        la_otra_lista.append(char.strip())
    print('\n'.join(la_otra_lista))
