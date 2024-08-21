def print_parms(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_parms(2, 3, 5,)
print_parms(b = 25)
print_parms(c = [1, 2, 3])

values_list = [2, 'Tatiana', False]
values_dict = {'a': 2, 'b': 'Denis', 'c': 5}

print_parms(*values_list)
print_parms(**values_dict)

values_list_2 = [28, 'Anna']
print_parms(*values_list_2, 42)

