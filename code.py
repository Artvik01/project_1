#only with even nambers
input = 0
if input > 0:
    hoper = float(input) - int(input)
    if hoper < 0.5:
        print(int(input))
    else:
        print(int(input + 1))
elif input < 0:
    hoper1 = float(input) - int(input)
    if hoper1 > -0.5:
        print(int(input))
    else:
        print(int(input - 1))
else:
    print(0
