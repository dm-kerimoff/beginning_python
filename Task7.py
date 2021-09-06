firm_dict = {}
aver_dict = {}
with open("text7.txt", "r") as f_7:
    for line in f_7:
        sentence = line.split()  # список строк
        firm_dict[sentence[0]] = float(sentence[2]) - float(sentence[3])

    sum_list = [firm_dict[i] for i in firm_dict.keys() if firm_dict[i] > 0]

aver_dict["average_profit"] = (sum(sum_list) / len(sum_list))
print(aver_dict)
