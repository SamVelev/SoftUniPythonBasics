from math import pi

figure = input()

if figure == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")

if figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")

if figure == "circle":
    a = float(input())
    area = a * a * pi
    print(f"{area:.3f}")

if figure == "triangle":
    a = float(input())
    b = float(input())
    area = a * b / 2
    print(f"{area:.3f}")



