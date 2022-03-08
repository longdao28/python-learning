def commaCode(list):
    if list == []:
        print('Empty list')
    for i in range(len(list)):
        if i < len(list) - 1 :
            print(str(list[i]) + ', ', end='')
        else:
            print('and ' + str(list[i]))

spam = [42, 78, 87]
commaCode(spam)
