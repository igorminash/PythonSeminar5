# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def degree(n, deg):
    if deg == 0:
        result = 1
    elif deg == 0:
        result = n
    else:
        result = n * degree(n,deg-1)
    return result

A = int(input("Введите число: "))
B = int(input("Введите степень числа: "))

print(f"Число {A} в степени {B} равняется = {degree(A,B)}")

    
    
    
