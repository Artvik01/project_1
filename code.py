#only with even nambers
input = 4.8
if input > 0:
    hoper = input % 2
    if hoper < 0.5:
        print(int(input))
    else:
        print(int(input + 1))
elif input < 0:
    hoper1 = (input - 2 * input) % 2
    if hoper1 < 0.5:
        print(int(input))
    else:
        print(int(input - 1))