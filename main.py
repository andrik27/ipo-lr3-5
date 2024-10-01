import math
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
r = float(input("Введите радиус круга: "))
ox = math.sqrt(x**2+y**2)
if ox < r:
    print("Точка попадает в круг.")
else:
    print("Точка не попадает в круг.")