l = []

n = int(input('Enter how many elements do you want in list : '))
for i in range(n):
    temp = input(f'Enter element no. {i} : ')
    try:
        temp = int(temp)
    except:
        if(temp == 'True' or temp == 'False'):
            temp = bool(temp)
        else:
            temp = str(temp)
    l.append(temp)

for i in l:
    print(i,type(i),sep=' -> ')