# Написать программу, проверяющую правильность написания выражения со скобками.
# {(())}([]{{[]}}) - правильно {[)}(){)) - неправильно, *указать где ошибка
#                                ^

def check_brackets(brcs):
    stack = []
    brc = {'(': ')', '[': ']', '{': '}'}

    for i in range(len(brcs)):
        if brcs[i] in brc.keys():
            stack.append(brcs[i])
        elif brcs[i] in brc.values():
            if len(stack) > 0:
                b = stack.pop()
                if brc[b] != brcs[i]:
                    return i
            else:
                return i
    if len(stack) == 0:
        return 0
    else:
        return len(brc)
brcs = '{[)}(){))'
print(brcs)
pos = check_brackets(brcs)
if pos > 0:
    s = ' '*(pos - 1)
    print(f'{s} ^')