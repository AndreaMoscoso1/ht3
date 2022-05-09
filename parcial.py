'''
UFM / Programación I / Parcial II
{Andrea Eugenia Moscoso Dominguez}

Escenarios de prueba:
1) UPC-A Verifier:
    code A = 036000291457 (Inválido)
    code B = 129462537728 (Inválido)
    code C = 036000291452 (Válido)
2) Insertion Sort:
    list A = [3, 9, 1, -2, 39]
    list B = [90, 20, 5, 4, 5, 5, 9]
3) Sorting Benchmark:
    list 1 = {20,000 elementos en orden aleatorio}
    list 2 = {20,000 elementos en orden descendiente}
'''

from sorting import insertion_sort, selection_sort
from upca import upca_verify

import random 
import time 

code_a = '036000291457'
code_b = '129462537728'
code_c = '036000291452' 

list_a = [3, 9, 1, -2, 39]
list_b = [90, 20, 5, 4, 5, 5, 9]

list_1 = random.sample(range(0, 20000), 20000)
list_2 = sorted(list_1, reverse=True)

# Testing UPC-A
print('\n***** Testing UPC-A *****\n')
print('UPC-A, code A:', code_a, upca_verify(code_a))
print('UPC-A, code B:', code_b, upca_verify(code_b))
print('UPC-A, code C:', code_c, upca_verify(code_c))

# TODO: Terminar testing de códigos B y C.

# Testing Insertion Sort
print('\n***** Testing Insertion Sort *****\n')
print('Insertion Sort, list A:', insertion_sort(list_a))
print('\n***** Testing Insertion Sort *****\n')
print('Insertion Sort, list B:', insertion_sort(list_b))

# Becnhmarking Sorting Algorithms
print('\n***** Sorting Benchmarking *****\n')
start_time = time.time()
selection_sort(list_1)
diff_time = time.time() - start_time
print('Selection Sort, list 1:', diff_time, 'sec')

start_time = time.time()
insertion_sort(list_1)
diff_time = time.time() - start_time
print('Insertion Sort, list 1:', diff_time, 'sec')

start_time = time.time()
selection_sort(list_2)
diff_time = time.time() - start_time
print('Selection Sort, list 2:', diff_time, 'sec')

start_time = time.time()
insertion_sort(list_2)
diff_time = time.time() - start_time
print('Insertion Sort, list 2:', diff_time, 'sec')
