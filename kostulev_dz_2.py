# 1 задание
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# 2 задача
my_list = ["в", "5", "часов", "17", "минут", "температура", "воздуха", "была", "+5", "градусов"]

list1 = []
for elem in my_list:
    if elem.isdigit():
        list1.extend(['""', f'{int(elem):02}', '""'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        list1.extend(['""', f'{elem[0]}{int(elem[1:]):02}', '""'])
    else:
        list1.append(elem)
out_info = ' '.join(list1)
print(out_info)

symbol_idxs = []
for idx, letter in enumerate(out_info):
    if letter == '""':
        symbol_idxs.append(idx)
for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] - 1

for del_idx in reversed(symbol_idxs):
    out_info = out_info[:del_idx] + out_info[del_idx + 1:]



# 4 задание
my_list = ("инженер-конструктор Игорь", "главный бухгалтер МАРИНА", "токарь высшего разряда нИКОЛАЙ", "диерктор аэлита")
for i in my_list:
    print(f"Привет, {i.split()[-1].title()}!")



#  5 задание
list = [40.3, 35.8, 70, 44.22, 13, 67.43, 33.13, 84.33, 56, 55]
message = ""
for i in list:
    price = f"{i:.2f}".split(".")
    message += (f"{price[0]} rub : {price[1]} kop ")
print(message)

list = [40.3, 35.8, 70, 44.22, 13, 67.43, 33.13, 84.33, 56, 55]
print(id(list))
list.sort()
print(id(list))
for i in list:
    rub = int(i)
    kop = (i - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')


list = [40.3, 35.8, 70, 44.22, 13, 67.43, 33.13, 84.33, 56, 55]
for i in sorted(list)[::-1][:5]:
    rub = int(i)
    kop = (i - int(i)) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')



