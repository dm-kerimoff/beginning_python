with open("text4.txt", "r", encoding="utf-8") as f_4:
    lines = f_4.read()  # строка
    lines = lines.replace("One", "Один").replace("Two", "Два").replace("Three", "Три").replace("Four", "Четыре")

with open("text4_1.txt", "w", encoding="utf-8") as f_41:
    print(lines, file=f_41)
