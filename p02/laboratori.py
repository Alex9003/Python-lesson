print("------------------------")
print("--Планета з станціями --\n\n\n")
area_planetu=int(input("Ведіть площу "))
big_laboratori_area=int(input("Ведіть площу великої лабораторії:"))
middle_laboratori_area=int(input("Ведіть площу середньої лабораторії:"))
small_laboratori_area=int(input("Ведіть площу маненької лабораторії: "))
all_big_laboratori=area_planetu//big_laboratori_area
last_area=area_planetu-all_big_laboratori
all_middle_laboratori=last_area//middle_laboratori_area
last_area=last_area-all_middle_laboratori
all_small_laboratori=last_area//small_laboratori_area
print(f"{all_big_laboratori}\n{all_middle_laboratori}\n{all_small_laboratori}")