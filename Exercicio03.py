a_x, a_y = float(15000), float(15000)
b_x = float(45000)
c_x = float(65000)
a, b = 0, 0

while (a_x < b_x):
    a_x += a_x*0.1
    b_x += b_x*0.05
    a += 1

while True:
    a_y += a_y*0.1
    c_x += c_x*0.025
    if a_y-(a_y*0.23) >= c_x:
        break
    b += 1

print(f'A população A irá se igualar ou ultrapassar a B em {a} anos')
print(f'A população A ultrapassar a C em 23% em {b} anos')
