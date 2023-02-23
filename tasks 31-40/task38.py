#  38. Древо семьи
family = [
    {'name': 'a', 'parent': ''},
    {'name': 'b', 'parent': 'a'},
    {'name': 'c', 'parent': 'a'},
    {'name': 'd', 'parent': 'b'},
    {'name': 'e', 'parent': 'd'},
    {'name': 'f', 'parent': ''},
    {'name': 'g', 'parent': 'f'},
    {'name': 'h', 'parent': 'a'}
]

INDENT = '  '


def print_family(parent, family, indent=0):
    for child in family:
        if child['parent'] == parent:
            print('%s%s' % (INDENT * indent, child['name']))
            print_family(child['name'], family, indent + 1)

print_family('', family)

while True:

    a = str(input('Введи имя ребенка - '))
    b = str(input('Введи имя родителя - '))
    family.append({'name': a, 'parent': b})
    print_family('', family)