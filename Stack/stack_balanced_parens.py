"""
Use a stack to check where or not a string
has a balanced usage of parenthesis

Example:
    (), ()(), (({[]}))  <- Balanced
    (() , {{{)]}, [][]]] <- Not Balanced

Balanced Example: {[]}
Non Balanced Example: (()
Non Balanced Example: ))
"""

from Stack import Stack


def is_match(p1, p2):
    return True if p1 + p2 in ['{}', '()', '[]'] else False


def is_paren_balanced(inputStr):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(inputStr) and is_balanced:
        paren = inputStr[index]

        if paren in "{([":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False

        index += 1

    return is_balanced and s.is_empty()


print(is_paren_balanced("{{(())}}"))



