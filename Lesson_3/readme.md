# Hometask 3

Каждое задание должно быть выполнено в отдельном файле.
Можно пользоваться только встроенными модулями.
Обязательно соблюдение PEP8. Код должен быть проверен линтерами pylint и flake8.

1. Написать несколько функций, которые в качестве единственного аргумента принимают список (или кортеж) целых чисел.
     - первая функция должна вернуть квадраты элементов коллекции;
     - вторая функция должна вернуть только элементы на четных позициях;
     - третья функция возвращает кубы четных элементов на нечетных позициях.

2. Написать функцию, которая принимает произвольное количество любых аргументов. 
    Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи. 
    Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
    Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел. 
    Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a) 
    При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.

3. Написать функцию, которая будет принимать только 4 позиционных аргументы (все аргументы числовые).
    Функция должна вернуть среднее арифметическое аргументов и самый большой аргумент за все время вызовов этой функции.
    Пример: foo(1,2,3,4) -> 2.5, 4
                  foo(-3, -2, 10, 1) -> 1.5, 10
                  foo(7,8,8,1) -> 6, 10

4. На вход функции передается строка с xml документом (тэги без аттрибутов, корневой элемент только один). 
   Нужно выполнить следующее преобразование и вывести максимальную вложенность.
   Пример: 
```bash
        a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
        foo(a) -> 
        {
            'name': 'root', 
            'children': [
                {'name': 'element1', 'children': []},
                {'name': 'element2', 'children': []},
                {
                    'name': 'element3', 
                    'children': [
                        {'name': 'element4', 'children': []}
                    ]
                }
            ]
        }, 2       
```
    в данном случае у element4 тэга вложенность/глубина 2

5. В этом задании можно отступить от PEP8. 
    Цель - выполнить задание за минимальное возможное количество символов в функции (если потребовался импорт отдельных модулей для функции, то инструкции импорта тоже считаются).
    Напишите функцию, которая будет принимать ввод пользовательской строки. В строке 1 или более отрицательных/положительных чисел.
    Функция должна вернуть ближайшее к нулю значение.
    пример foo() -> пользователь ввел '1 2 -0.5 0.75 22' -> функция доджна вернуть -0.5