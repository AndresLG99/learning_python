def check_digits(num):
    return num in range(100,1_000)

num_sum = 586 + 482

result = check_digits(num_sum)
print(result)

def check_digits_list(lst):

    lst_3 = []

    for n in lst:
        if n in range(100,1_000):
            lst_3.append(n)
        else:
            pass
    return lst_3

result = check_digits_list([555,99,600])
print((type(result)))
print(result)