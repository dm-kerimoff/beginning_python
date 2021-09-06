with open("text3.txt", "r", encoding="utf-8") as f_obj:
    my_list = f_obj.readlines()  # создание списка строк
    average = 0
    for line in my_list:
        if float(line.split()[1]) < 20000:
            print(line.split()[0])
        average += float(line.split()[1])

print(f"Средняя зарплата работников равна {average})
