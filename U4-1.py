#Во втором массиве сохранить индексы четных элементов первого массива.
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
#надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
#именно в этих позициях первого массива стоят четные числа.
import random
min_item = 0
max_item = 100
size = 1000
res_mass = []
mass_1 = [random.randint(min_item, max_item) for i in range (size)]
import timeit
import cProfile
def test ():
   for idx, num in enumerate (mass_1):
      if num % 2 == min_item:
         res_mass.append(idx)
   return (mass_1, res_mass)
def test2():
    line1 = len(mass_1)
    i = 0
    while i != line1:
      if mass_1[i]  % 2 == min_item:
         res_mass.append(i)
      i +=1
          
    return (mass_1, res_mass)

cProfile.run('test()')
cProfile.run('test2()')
#print (timeit.timeit(test, number = 100))
#print (timeit.timeit(test2, number = 100))
# test 0.0013013469999999527 при списке 10 значений
# test2 0.0018222970000000283 при списке 10 значений
#print (test())
#print (test2())

"""
Выводы:
В данной задаче цикл for и решение с помощью while показывают одинаковые
результаты и по времени и по повторяемости операций при выполнении кода.
Самая часто повторяемая операция, которая линейно зависит от величины массива - операция
добавления индекса в список.
"""
"""
test
 10 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 U4-1.py:13(test)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}        """
"""
test2
59 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 U4-1.py:18(test2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       54    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        """
#test    0.010475229999999947 при списке 100 значений
# test2  0.10398914199999998
"""
test
51 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 U4-1.py:13(test)
        1    0.001    0.001    0.001    0.001 {built-in method builtins.exec}
       47    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        """
"""
test 2
50 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 U4-1.py:18(test2)
        1    0.001    0.001    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       45    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        """
#0.07281797499999998 при списке 1000 значений
# test2  0.00016625999999997365
"""
test
497 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 U4-1.py:13(test)
        1    0.001    0.001    0.002    0.002 {built-in method builtins.exec}
      493    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        """
"""
test2
498 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 U4-1.py:18(test2)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      493    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}        """
