# Hometask 7

Практические задания к теме "Декораторы".

Каждое задание должно быть выполнено в отдельном файле.
Можно пользоваться только встроенными модулями.
Обязательно соблюдение PEP8. Код должен быть проверен линтерами pylint и flake8.

1.Напишите параметризованный декоратор, который считает и выводит при каждом вызове среднее время работы функции за n последних вызовов.
   Время выводить в миллисекундах.
  Пример использования:
```python
  @average_time(n=2)
  def foo(a):
      sleep(a)
      return a

  foo(3) # вернет 3 и выведет сообщение "Среднее время работы: 3000 мс."
  foo(7) # вернет 7 и выведет сообщение "Среднее время работы: 5000 мс."
  foo(1) # вернет 1 и выведет сообщение "Среднее время работы: 4000 мс."
```

2. Напишите параметризованный декоратор для классов, 
 который будет считать и выводить время работы методов класса, имена которых переданы в параметрах декоратора.
Пример:
```python
  @time_methods('inspect', 'finalize')
  class Spam:
      def __init__(self, s):
          self.s = s
      def inspect(self):
           sleep(self.s)
      def foo(self):
           return self.s

 a = Spam(2)
 a.inspect()  #  должно вывести сообщение о времени работы
 a.foo()  # ничего не выводить
```

3. Каррирование. 
  Преобразовать вызов функции с конечным количеством позиционных аргументов f(a, b, c, d) в вызов вида f(a)(b)(c)(d), используя декоратор.
  Пример:
```python
  @carry
  def foo(a, b):
        return a + b

   foo(1)(5)  # вернет 6
```

4. Написать декоратор, который будет проверять тип аргументов при вызове функции согласно аннотации функции.
   Декорирование функции без аннотации или с неполной аннотацией (когда аннотированы не все аргументы) должно рейзить ошибку.
   В случае несовпадения переданных во время вызова функции аргументов с типами аргументов в аннотации - выводить сообщение.