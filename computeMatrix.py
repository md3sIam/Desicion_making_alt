import numpy as np
from numpy import linalg
import random


def compute_matrix(matrices, sign=True):
    # чуть поменял параметр и инициализацию (просто для удобства)
    A = matrices[0]
    b = matrices[1]

    signs = [sign] * len(b)

    # константный коэф (это как для градиентного спуска, тут можно любой от 0 до 2/3)
    J = 1 / 3

    # вставка доп. переменных
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                if signs[i] == True:  # значит там знак БОЛЬШЕ или БОЛЬШЕ ЛИБО РАВНО
                    A[i].append(-1)
                else:  # а это значит там знак МЕНЬШЕ или МЕНЬШЕ ЛИБО РАВНО
                    A[i].append(1)
            else:
                A[i].append(0)

    x = np.ones(len(A[0]))  # искомые значения
    b_k = 1  # коэф для окончания, это стр 83 самый верх

    while True:

        # 13 формула, считаем r
        r = b - np.matmul(A, x)

        # если r +- равен 0, то выходим, т.к. приближенный ответ найден
        end = 0
        for i in range(len(r)):
            end += abs(r[i])
        if end < 0.001:
            print('Матрица совместна')
            return True

        # формула 14, а также ее диагональная матрица
        d = x * x
        D = np.diag(d)

        # считаем матрицы U и S по формулам 19 и 20
        try:
            u = np.matmul(linalg.inv(np.matmul(np.matmul(A, D), np.transpose(A))), r)
            s = np.matmul(np.matmul(D, np.transpose(A)), u)
        except np.linalg.LinAlgError:
            print("Матрица несовместна")
            return False

        #находим минимальный S, удовлетворяющий условиям, формула 21
        empty = True
        for i in range(len(s)):
            if s[i] < 0:
                if empty:
                    min = x[i] * (-s[i])
                    empty = False
                else:
                    if x[i] * (-s[i]) < min:
                        min = x[i]*(-s[i])

        if (empty):
            min = 1
        else:
            min *= J

        if min > 1:
            min = 1

        # корректируем Х, формула 22
        for i in range(len(s)):
            x[i] += min * (s[i])

        # основная часть закончена, далее идет часть, которая отсекает случай, когда система неравенстр решений не имеет
        # а эквивалентная система уравнений решения имеет
        # (а у нас именно так)

        u_k = [] # опять 83 стр самый верх

        # считаем f_t
        f_t = 0
        for i in range(len(u)):
            f_t += s[i] * s[i] / d[i]

        # формируем u_k из u, снова 83 стр самый верх
        for i in range(len(u)):
            u_k.append(b_k / f_t * u[i])
        t = np.matmul(np.transpose(A), u_k)

        # здесь при умножении всегда получается матрица из 1 строки, дальше как раз тот самый загадочный оператор ()+
        # если в этой строке нет отрицательных компонент - считаем ее норму, иначе норма будет 0 (стр 83 внизу)
        f = False
        for j in range(np.size(t)):
            if t[j] < 0:
                f = True

        # все еще считаем норму
        if f:
            max = 0
        else:
            max = 0
            for j in range(np.size(t)):
                if abs(t[j]) > max:
                    max = t[j]
        t = max # норма


        # правая часть уравнения, стр 83 внизу
        t1 = abs(np.matmul(b, u_k)-1)
        t += t1

        # если вот тут меньше эпсилон - мы уперлись, у неравенства решения нет, у уравнения есть, система несовместна
        if t < 0.001:
            return False

        b_k *= (1-min)


def __main__():
    print(compute_matrix([[69, 73, 89, 75, 6, 10, 89], [45, 77, 84, 64, 95, 18, 17], [12, 62, 72, 89, 87, 71, 60], [2, 26, 57, 91, 3, 85, 79], [27, 43, 0, 6, 43, 97, 79]], [39, 61, 3, 83, 45], [True, True, True, True, True]
    ))

    #
    # sovm = 0
    # nesovm = 0
    # for i in range(100):
    #     A = []
    #     b = []
    #     s = []
    #     for j in range(5):
    #         b.append(random.randrange(0,100))
    #         a = []
    #         s.append(True)
    #         for z in range(7):
    #             a.append(random.randrange(0,100))
    #         A.append(a)
    #     print(A, b, s)
    #     #print(compute_matrix(A, b, s))
    #     if compute_matrix(A, b, s):
    #         sovm += 1
    #     else:
    #         nesovm += 1
    #
    # print(sovm, nesovm)

    #
    #
    # print(compute_matrix([[37, 31, 75, 79, 9, 37, 73],
    #                       [9, 87, 78, 54, 97, 91, 8],
    #                       [29, 36, 69, 72, 29, 55, 14],
    #                       [15, 29, 25, 77, 83, 49, 73],
    #                       [54, 53, 94, 82, 43, 18, 83]],
    #                                                     [11, 28, 50, 68, 60], [True, True, True, True, True]))

    # print(compute_matrix([[1,1], [1,1]], [5, -8], [True, False]))


if __name__ == "__main__":
    __main__()
