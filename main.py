# ШАГ. Д/з по сроку 26/06/2023 © Заливко Денис
import random


def task_4_137(k: int) -> int:
    """1) 4.137.
    Даны целое число k (1 k 180) и последовательность цифр 10111213...9899,
    в которой выписаны подряд все двузначные числа. Определить k-ю цифру.
        П р и м е ч а н и е
        Величины строкового типа не использовать.
    """
    number = int(''.join(str(item) for item in range(10, 100)))
    print(f'Заданное число:\n{number}, длина = {len(str(number))}')

    # k = random.randint(1, 180)
    print(f'Элемент к: {k}')

    list_int = []
    aNumber = number
    while aNumber > 0:
        cipher = aNumber % 10
        list_int.insert(0, cipher)
        aNumber = aNumber // 10
    # print(lInt)
    result_from_list = {list_int[k]}
    print(f'Элемент из списка {k} = ({list_int[k - 1]}) >>> {result_from_list} <<< ({list_int[k + 1]})')

    result = (k // 2) + 10
    result = result // 10 if k % 2 == 0 else result % 10
    print(f'Результат арифметических действий: {result}')

    return result


def task_5_62(*classes):
    """2) 5.62.
    2) 5.62. Известны оценки по физике каждого ученика двух классов. Определить среднюю оценку в каждом классе.
        Количество учащихся в каждом классе одинаковое.
    :return:
    """
    result = tuple()
    for item in classes:
        result += (sum(item) / len(item),)

    return result


def task_2_43(a: int, b: int):
    """3) 2.43.
    3) 2.43. Даны два целых числа a и b. Если a делится на b или b делится на a, то вывести 1, иначе — любое другое
        число. Условные операторы и операторы цикла не использовать.
    :return:
    """
    return 1 if (b != 0 and a % b == 0) or (a != 0 and b % a == 0) else 0


def task_17_7(tvs: list[int]):
    """4) 17.7.
    4) 17.7. Известны стоимости 12 марок телевизоров (все значения разные). Определить стоимость телевизора,
        являющегося "пятым из самых дешевых моделей".
    :return:
    """
    result = list(tvs)
    result.sort()
    return result[4]


def task_6_97(points: list[int], N: int):
    """5) 6.97.
    5) 6.97. Известно количество очков, набранных каждой из 20-ти команд-участниц первенства по футболу. Перечень
        очков дан в порядке убывания (ни одна пара команд не набрала одинаковое количество очков). Определить,
        какое место заняла команда, набравшая N очков (естественно, что значение N имеется в перечне). Условный оператор
        не использовать.
    :return:
    """
    try:
        rating = points.index(N) + 1
    except ValueError:
        rating = -1
    return rating



if __name__ == '__main__':
    print('''
    Д/з по сроку 26.06.2023:

    1) 4.137. Даны целое число k (1 <= k <= 180) и последовательность цифр 10111213...9899,
        в которой выписаны подряд все двузначные числа. Определить k-ю цифру.
            П р и ме ч а н и е
            Величины строкового типа не использовать.

    2) 5.62. Известны оценки по физике каждого ученика двух классов. Определить среднюю оценку в каждом классе. 
        Количество учащихся в каждом классе одинаковое.

    3) 2.43. Даны два целых числа a и b. Если a делится на b или b делится на a, то вывес-ти 1, иначе — любое другое 
        число. Условные операторы и операторы цикла не использовать.
        
    4) 17.7. Известны стоимости 12 марок телевизоров (все значения разные). Определить стоимость телевизора, 
        являющегося "пятым из самых дешевых моделей".
    
    5) 6.97. Известно количество очков, набранных каждой из 20-ти команд-участниц первенства по футболу. Перечень 
        очков дан в порядке убывания (ни одна пара команд не набрала одинаковое количество очков). Определить, 
        какое место заняла команда, набравшая N очков (естественно, что значение N имеется в перечне). Условный оператор 
        не использовать.

    ''')

    taskNumber = int(input('\nВведите номер запускаемой задачи: '))

    if 1 < taskNumber > 6:
        print('Ошибка! Значение введено неверно!')
    elif taskNumber == 1:
        # task_4_137(10)
        task_4_137(random.randint(1, 180))

    elif taskNumber == 2:
        count_students = 25
        class_1 = []
        class_2 = []
        for _ in range(0, count_students):
            class_1.append(random.randint(1, 10))
            class_2.append(random.randint(1, 10))

        results = task_5_62(class_1, class_2)
        print(f'Класс 1.\nОценки:\n{class_1}\nСредняя успеваемость: {results[0]}\n')
        print(f'Класс 2.\nОценки:\n{class_2}\nСредняя успеваемость: {results[1]}')

    elif taskNumber == 3:
        a = int(input('Input a: '))
        b = int(input('Input b: '))
        result = task_2_43(a, b)
        print(result)

    elif taskNumber == 4:
        tvs = []
        while len(tvs) < 12:
            cost = random.randint(10, 100)
            if cost not in tvs:
                tvs.append(cost)
        result = task_17_7(tvs)
        print(f'Стоимость телевизоров:\n{tvs}')
        print(f'Самый дешёвый на пятом месте стОит: {result}')

    elif taskNumber == 5:
        points = []
        while len(points) < 20:
            point = random.randint(10, 50)
            if point not in points:
                points.append(point)
        points.sort()
        print(f'Очки, набранные командами:\n{points}')
        n = int(input('Введите N (количество очков): '))
        result = task_6_97(points, n)
        if result > 0:
            print(f'Команда, с количеством очков N={n}, находится на {result} месте.')
        else:
            print(f'Не найдена команда, набравшая {n} очков.')
        pass
