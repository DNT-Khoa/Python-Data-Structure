from Stack import Stack

# Define a function to reverse string using stack
def reverse_string(inputString):
    s = Stack()

    # Push every letter of the string
    # to the stack
    for i in range(len(inputString)):
        s.push(inputString[i])

    rev_str = ""

    # Pop every letter from the stack out and concatenate it to the rev_str
    # as long as the stack is not empty

    while not s.is_empty():
        rev_str += s.pop()

    return rev_str

print(reverse_string("Hello"))