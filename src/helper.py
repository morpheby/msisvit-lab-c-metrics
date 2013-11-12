def find_adjacent_bracket(text, open_close_brackes):
    """ Finds the last dangling closing bracket in text """

    brackets = 0

    for i in range(0, len(text)):
        if text[i] == open_close_brackes[0]:
            brackets += 1
        elif text[i] == open_close_brackes[1]:
            brackets -= 1

        if brackets == 0:
            return i+1
        elif brackets < 0:
            break

    raise SyntaxError('Syntax error: unmatched bracket')
