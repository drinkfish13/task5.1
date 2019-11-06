import json
data3 ={}
with open('purchase_log.txt', encoding='utf-8') as f: #открываем файл для чтения, чтобы создать словарь
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        data3[dict_.get('user_id')] = dict_.get('category')

f = open('visit_log.csv', 'r')
k = open('funnel.csv', 'w+')
another_line = f.readline()
while another_line:
    another_line_2 = another_line.strip().split(',')
    another_line = f.readline()
    if another_line_2[0] == 'user_id': # создаем первую строку
        another_line_2.append("category")
        k.writelines(",".join(another_line_2) + "\n")
    else:
        if another_line_2[0] in data3: # проверяем наличие покупки и записываем совпадения в файл
            another_line_2.append(data3[another_line_2[0]])
            k.writelines(",".join(another_line_2) + "\n")


