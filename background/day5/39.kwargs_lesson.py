def sum_num(**kwargs):
    print(type(kwargs))
    print(kwargs)

    total = 0

    for c,v in kwargs.items():
        print(c, '=', v)
        total += v
    return total

print(sum_num(x=1,
              y=2,
              z=3))

def test(num1, num2, *args, **kwargs):
    print(f"First value is {num1}")
    print(f"First value is {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for c,v in kwargs.items():
        print(f"{c} = {v}")

test(1,2,100,200,300,400,x=5_000,y=6_000,z=7_000)

args = [100,200,300,400]
kwargs = {"x":5_000,"y":6_000,"z":7_000}

test(1,2,*args,**kwargs)