with open("text2.txt", "r", ) as f_sent:
    lines = f_sent.readlines()  # создание списка строк
    print(f"В файле {len(lines)} строк")
    i = 0
    for line in lines:
        print(f"В {i + 1} строке {len(line.split())} слов")
        i += 1
