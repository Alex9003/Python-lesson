print("\n---------------------------")
print("- Співвідношення учнів у класі -")
print("\n---------------------------")
boys=int(input("Ведіть кількість хлопців в класі: "))
girls=int(input("Ведіть кількість дівчат в класі: "))
people=int(boys)+int(girls)
porsent_boys=int((float(boys)/float(people))*100)
#porsent_girls=int((float(girls)/float(people))*100)
porsent_girls=100-porsent_boys

print(f"Кількість учнів {people}\n")
print("Кількість хлопців ",porsent_boys,"%")
print("\nКількість дівчат ",porsent_girls,"%")
#print("Дівчата"+str(porsent_girls)+"%, Хлопців"+str(porsent_boys)+"%")
print("\n----- Кінець програми------","\n\n\n")