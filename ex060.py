n1 = int(input('Numero pro fatorial: '))
fat = 1
while n1 > 0:
    if n1 != 1:
        print(n1, end=' x ')
    else:
        print(n1, end=' = ')
    fat *= n1
    n1 -= 1

print('{}'.format(fat))
