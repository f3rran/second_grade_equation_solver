#!/usr/bin/python
# Simple project to calculate second grade equations.

import sys
import math


def calculate_equation(quad, x, real):
    root = (x**2) - (4*quad*real)

    if root < 0:
        print('Sin soluciones')
    elif root == 0:
        single_result = (-x + math.sqrt(root)) / 2*quad
        print('Solución única: '+str(single_result))
    elif root > 0:
        solution_one = (-x + math.sqrt(root)) / (2*quad)
        solution_two = (-x - math.sqrt(root)) / (2*quad)
        print('Solución 1: '+str(solution_one)+' - Solución 2: '+str(solution_two))


if len(sys.argv) == 4:
    calculate_equation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
else:
    quad_input = input("Introduzca la a (a * x^2): ")
    x_input = input("Introduzca la b (b * x): ")
    real_input = input("Introduzca la c (Número real): ")

    calculate_equation(int(quad_input), int(x_input), int(real_input))
