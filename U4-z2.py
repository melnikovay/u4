#Написать два алгоритма нахождения i-го по счёту простого числа.
#Функция нахождения простого числа должна принимать на вход натуральное
#и возвращать соответствующее простое число. Проанализировать скорость и
#сложность алгоритмов.
#Вариант1 — «Решето Эратосфена».
import timeit
import cProfile
def ersn (n):
    k = n*n
    sieve = [i for i in range (k)]
    sieve[1] = 0
    for i in range (2, k):
        if sieve[i] != 0:
            j = i + i
            while j < k:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return (res[n])
def var1():
    return (ersn(100))

    
# Вариант 2
def test1(n):
    k = n*n
    sieve = [i for i in range (k)]
    sieve[1] = 0
    for i in range (3, k):
        if sieve[i]%2 == 0:
            sieve [i] = 0
        else:
            j = i + i
            while j < k:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return (res[n])
def var2():
    return (test1(100))
#print (var1())
#print (var2())
#print (test1(10))
#print (timeit.timeit(var1, number = 100))
#0.01762196599999999 при n = 10
# 2.084422545 при n = 100
# 258.56666613299996 при n = 1000
#print (timeit.timeit(var2, number = 100))
#0.01646881599999994 при n = 10
#1.994579088 при n = 100
# 254.50273796 при n = 1000
#cProfile.run('var1()')
"""
n = 10
7 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 U4-z2.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 U4-z2.py:18(<listcomp>)
        1    0.000    0.000    0.000    0.000 U4-z2.py:20(var1)
        1    0.000    0.000    0.000    0.000 U4-z2.py:8(ersn)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

n = 100
 7 function calls in 0.026 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
        1    0.002    0.002    0.002    0.002 U4-z2.py:10(<listcomp>)
        1    0.001    0.001    0.001    0.001 U4-z2.py:18(<listcomp>)
        1    0.000    0.000    0.025    0.025 U4-z2.py:20(var1)
        1    0.022    0.022    0.025    0.025 U4-z2.py:8(ersn)
        1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

#cProfile.run('var2()')

"""
 7 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 U4-z2.py:25(test1)
        1    0.000    0.000    0.000    0.000 U4-z2.py:27(<listcomp>)
        1    0.000    0.000    0.000    0.000 U4-z2.py:37(<listcomp>)
        1    0.000    0.000    0.000    0.000 U4-z2.py:39(var2)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

n = 100
7 function calls in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.024    0.024 <string>:1(<module>)
        1    0.021    0.021    0.024    0.024 U4-z2.py:25(test1)
        1    0.002    0.002    0.002    0.002 U4-z2.py:27(<listcomp>)
        1    0.001    0.001    0.001    0.001 U4-z2.py:37(<listcomp>)
        1    0.000    0.000    0.024    0.024 U4-z2.py:39(var2)
        1    0.001    0.001    0.025    0.025 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# Выводы: вариант 2 чуть более оптимизирован о времени относительно варианта 1.     
