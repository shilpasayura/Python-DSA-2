def is_match(p1, p2):
    return (p1 == '(' and p2 == ')') or (p1 == '{' and p2 == '}') or (p1 == '[' and p2 == ']')


def balance_check(string):
    opening = '([{'
    closing = ')}]'
    stack = list()
    for ch in string:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            if len(stack):
                if not is_match(stack.pop(), ch):
                    return False

    if len(stack) != 0:
        return False

    return True

string = raw_input()

print balance_check(string)