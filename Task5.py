from random import randint

with open("text6.txt", 'w+', encoding="utf-8") as f_6:
    lines = [str(randint(5, 100)) for n in range(3)]  # список строк-чисел
    f_6.writelines(' '.join(lines))  # записываем их в файл
    f_6.seek(0)
    file_list = list(map(int, f_6.readline().split()))

print(sum(file_list))
