user_list = []
file = open('list.txt','r')
for i in file.readlines():
    user_list.append(i.strip())
while True:
    print('## list ##')
    print('1.Add Task\n 2.Edit Task\n 3.Delete Task \n4.Show lisrt \n 5.Exit\n')
    action=int(input('Actoin: '))
    if action==5:
        file = open('list.txt','w')
        for l in user_list:
            file.write('%s\n'% l)
        break
    elif action==1:
        task=input('Input tast: ')
        user_list.append(task)
    elif action==4:
        i=0
        for item in user_list:
            print(i,' > ',item)
            i+=1
    elif action == 2:
        indeks = int(input("Ведіть індекс в який ви хочити змінити:"))
        task=input("Ведіть значення:")
        user_list[indeks] = task
    elif action == 3:
        indeks = int(input("Ведіть індекс в який ви хочити видалити:"))
        del user_list[indeks]
        #indeks = input("Ведіть індекс в який ви хочити видалити:")
        #user_list.remove(indeks)


