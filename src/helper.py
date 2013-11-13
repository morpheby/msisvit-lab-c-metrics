
""" Helper functions """


def find_adjacent_bracket(text, open_close_brackets):
    """ Finds the last dangling closing bracket in text """

    brackets = 0

    for i in range(0, len(text)):
        if text[i] == open_close_brackets[0]:
            brackets += 1
        elif text[i] == open_close_brackets[1]:
            brackets -= 1

        if brackets == 0:
            return i+1
        elif brackets < 0:
            break

    raise SyntaxError('Syntax error: unmatched bracket')


def parse_operand(text):
    """ returns operand name, args with brackets, body with brackets and index of body end """
    
    first_bracket = text.find('(')
    operand_name = text[:first_bracket]
    
    last_bracket = first_bracket + find_adjacent_bracket(text[first_bracket:], '()')
    args = text[first_bracket:last_bracket]
    
    first_curly_bracket = text[last_bracket:].find('{')
    last_curly_bracket = first_curly_bracket + find_adjacent_bracket(text[first_curly_bracket:], '{}')
    
    body = text[first_curly_bracket:last_curly_bracket]

    return (operand_name, args, body, last_curly_bracket + 1)


