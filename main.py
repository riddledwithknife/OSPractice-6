import methods

# Кол-во сегментов
print("Введите количество сегментов памяти: ")
bn = input()
while bn.isdigit() == False or (bn.isdigit() == True and int(bn) == 0):
    bn = input("Введите допустимое значение: ")
block_num = int(bn)

# Размер
print("Введите размер сегмента: ")
block_size = []
for i in range(0, block_num, 1):
    bin = input()
    while bin.isdigit() == False or int(bin) == 0:
        bin = input("Введите допустимое значение: ")
    block_size.append(int(bin))

# Кол-во процессов
print("Введите количество процессов: ")
pn = input()
while pn.isdigit() == False or (pn.isdigit() == True and int(pn) == 0):
    pn = input("Введите допустимое значение: ")
process_num = int(pn)

# Размер
print("Введите размер процесса, подаваемого в память: ")
process_size = []
for i in range(0, process_num, 1):
    pin = input()
    while pin.isdigit() == False or int(pin) == 0:
        pin = input("Введите допустимое значение: ")

    process_size.append(int(pin))

# Выбор алгоритма
print("Введите алгоритм аллокации (1- First fit, 2- Best fit, 3- Worst fit): ")
option = input()
while option.isdigit() == False or (option.isdigit() == True and (int(option) < 1 or int(option) > 3)):
    option = input("Введите допустимое значение: ")
choice = int(option)
if choice == 1:
    ans1, ans2 = methods.firstFit(
        block_num, block_size, process_num, process_size)
elif choice == 2:
    ans1, ans2 = methods.bestFit(
        block_num, block_size, process_num, process_size)
elif choice == 3:
    ans1, ans2 = methods.worstFit(
        block_num, block_size, process_num, process_size)

if choice == 2 or choice == 3:
    index = []
    for w in range(0, len(ans1), 1):
        for l in range(0, len(block_size), 1):
            if ans1[w] == block_size[l]:
                index.append(l)
    ans1 = index
# Инфо
print("Номер процесса  Размер процесса    Номер сегмента   Размер сегмента")
for i in range(0, len(ans2), 1):
    print("      " + str(ans2[i] + 1) + "              " + str(process_size[ans2[i]]
                                                            ) + "             " + str(
        ans1[i] + 1) + "                " + str(block_size[ans1[i]]) + "                      " + str(
        block_size[ans1[i]] - process_size[ans2[i]]) + " байт блока: " + str(ans1[i] + 1) + " пусты.")

# Ожидание
print("Процессы этих размеров в очереди: ")
for z in range(0, process_num, 1):
    if z not in ans2:
        print("p" + str(z + 1) + " : " + str(process_size[z]))
