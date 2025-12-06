def sum_num(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(sum_num(1))
print(sum_num(1,2))
print(sum_num(1,2,3))
print(sum_num(1,2,3,4))
print(sum_num(1,2,3,4,5))