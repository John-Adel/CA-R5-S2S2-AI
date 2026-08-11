import functions as fun
fun.interface()
while True:
    lst = fun.user_input_function()
    print(fun.calculate(float(lst[0]), float(lst[1]), int(lst[2])))