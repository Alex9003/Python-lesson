# list_1=[2,22,3,4,88]
# #print("length =%d" % len(list_1))
# for i in range(len(list_1)):
#     print(list_1[i])
# for i in list_1:
#     print(i)

# import random
# random_list=[]
# list_sum=[]
# sum=0
# for i in range(9):
#     random_list.append(random.randint(0,100))
#
#     print(random_list[i])
# for i in random_list:
#     sum += i
# print(sum)
# # x=0
# for i in range(len(random_list)):
#     x=count(random_list[i])
#     list_sum[i]=x*random_list[i]
# print(list_sum)

# import random
# histogram=[]
# for i in range(5):
#     histogram.append(random.randint(0,10))
# print(histogram)
# for i in histogram:
#     red=''
#     if i>5:
#         red='\x1b[0;31m';
#
#     print(red, '\u2588'*i , i, '\x1b[0;38m')

import random
# numbers=[]
# for i in range(5):
#      numbers.append(random.randint(1,5))
# unigue=[]
# for num in numbers:
#     if num not in unigue:
#         unigue.append(num)
# print(numbers)
# print(unigue)
#numbers=[random.randint(0,10) for i in range(10)]
# numbers=[i*i for i in range(10)]
# print(numbers)
#
# file=open('num.txt','w')
# for i in numbers:
#     file.write("%s\n" % i)
# file.close()
numbers_from_file=[]
file=open('num.txt','r')
for i in file.readlines():
    numbers_from_file.append(int(i))
print(numbers_from_file)
file.close()
