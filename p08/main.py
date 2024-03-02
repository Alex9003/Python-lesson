import random
# range(40)
# range(1,4)
# range(0,40,4)
# y=range(40)
# print(y)
# x=random.randint(0,10)
# print(x)
# y={'x': 222,'y':111,'z':12}
# print(y['y'])
# x=1
# y=3
# z=9
# for key, item in y.items():
#     print(key,' = ', item)
random_namber=random.randint(1,100)
your_namber=int(input("Ведіть число від 1 до 100:"))
while True:
    if random_namber==your_namber:
        print('Ви вийграли!!!!')
        break
    elif random_namber>your_namber:
        print("Ваше число менеше загаданого")
    elif random_namber<your_namber:
        print("Ваше число більше загаданого")
    your_namber=int(input("Ведіть нове число"))
















