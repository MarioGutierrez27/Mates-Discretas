# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:29:19 2024

@author: zS23017362
"""

def euclides_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))


mcd = euclides_mcd(num1, num2)


print("El MCD de", num1, "y", num2, "es:", mcd)
