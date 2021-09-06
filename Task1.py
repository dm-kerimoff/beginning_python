with open("text1.txt", "w", encoding="utf-8") as f:
    while True:
        str = input()
        if str == '':
            break
        else:
            f.write(f"{str}\n")
