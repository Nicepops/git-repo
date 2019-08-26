__author__ = 'Осипов П.Д.'

#easy
#1


def my_round(number, ndigits):
    result = number * 10 ** ndigits // 1

    if result >= 5:
        return (result + 1) / 10 ** ndigits
    else:
        return result / 10 ** ndigits


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#2


def lucky_ticket(ticket_number):
    left_part = (int(str(ticket_number)[0]) + int(str(ticket_number)[1]) + int(str(ticket_number)[2]))
    right_part = (int(str(ticket_number)[-1]) + int(str(ticket_number)[-2]) + int(str(ticket_number)[-3]))
    if left_part == right_part:
        if len(str(ticket_number)) != 6:
            return None
        else:
            return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))                 #неправильно указанный номер => None
print(lucky_ticket(436751))

print(lucky_ticket(345899))                #добавил свой пример

#normal
#1


def fibonacci(n, m):
    fib1 = 1
    fib2 = 2
    fib = []
    while n-1 < 2:
        fib.append(fib1)
        n += 1
    while n-1 == 2:
        fib.append(fib2)
        n += 1
    while n-1 > 2 and n < m+1:
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        fib.append(fib2)
        n += 1
    return fib

print(fibonacci(4, 9))

#2


def sort_to_max(origin_list):
    print("исходный список: ", origin_list)
    N = len(origin_list)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    sorted_list = print("Преобразованый список: ", origin_list)
    return sorted_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

#3

def alt_filter(func, itr):
    new_itr = [elem for elem in itr if func(elem)]
    if type(itr) is tuple:
        new_itr = tuple(new_itr)
    if type(itr) is set:
        new_itr = set(new_itr)
    if type(itr) is str:
        new_itr = ''.join(new_itr)
    print(new_itr)
    return new_itr


alt_filter(lambda x: x > 5, {2, 10, -12, 2.5, 20, -11, 4, 4, 0})
alt_filter(lambda x: x < 0, range(-5, 5))