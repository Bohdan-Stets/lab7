def get_float_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print("Невірно введене значення.")
                continue
            if max_val is not None and value > max_val:
                print("Невірно введене значення.")
                continue
            return value
        except ValueError:
            print("Невірно введене значення. Спробуйте ще раз.")

n = int(input("Введіть кількість елементів у списках (n): "))

x_list = []
print("Введіть елементи для списку [x1, ..., xn] (числа від 0 до 1):")
for i in range(n):
    x = get_float_input(f"Введіть елемент x{i+1}: ", 0, 1)
    x_list.append(x)

y_list = []
print("Введіть елементи для списку [y1, ..., yn] (числа від -10 до 10):")
for i in range(n):
    y = get_float_input(f"Введіть елемент y{i+1}: ", -10, 10)
    y_list.append(y)

z_list = []
print("Введіть елементи для списку [z1, ..., zn] (числа від 0 до 50):")
for i in range(n):
    z = get_float_input(f"Введіть елемент z{i+1}: ", 0, 50)
    z_list.append(z)

print("Список [х1, ..., хn] (числа від 0 до 1):", x_list)
print("Список [y1, ..., yn] (числа від -10 до 10):", y_list)
print("Список [z1, ..., zn] (числа від 0 до 50):", z_list)
