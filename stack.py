"""
Модуль, описывающий структуру данных - стек
>>>clear()
>>>is_empty
True
>>>push(1)
>>>push(2)
>>>push(3)
>>>is_empty
False
>>>pop()
3
>>>pop()
2
>>>pop()
1
>>> is_empty()
True
"""

_stack = []

def push(x):
    _stack.append(x)

def pop():
    x = _stack.pop()
    return x

def clear():
    _stack.clear()

def is_empty():
    return len(_stack) == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Аогоритм проверки корректности скобочной последовательности
def is_braces_sequence_correct(s: str):
    """Проверяет корректность последовательности
    из круглых и квадратных скобок () []
    >>>is_braces_sequence_correct("(([()]))[]")
    True
    >>>is_braces_sequence_correct("([)]")
    False
     >>>is_braces_sequence_correct("([]")
    False
     >>>is_braces_sequence_correct("]")
    False
    """
    a_stack = []
    for brace in s:
        if brace not in "() []":
            continue
        if brace in "([":
            a_stack.pusk(brace)
        else:
            assert brace in ")]", "Ожидалось закрывающая скобка:" + str(brace)
        if a_stack.is_empty():
            return False
        left = a_stack.pop()
        if left =="(":
            right = ")"
        elif left == "[":
            right = "]"

    return a_stack.is_empty()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)