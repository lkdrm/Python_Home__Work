def lucky_numb(a):
    b = str(a)
    first_part = int(b[0]) + int(b[1]) + int(b[2])
    second_part = int(b[-1]) + int(b[-2]) + int(b[-3])
    if first_part == second_part:
        print(True)
    else:
        print(False)

lucky_numb(123420)
lucky_numb(723422)
