import re, helper


def get_function_declaration(text):
    # regex group1, name group2, arguments group3
    rproc = r"((?<=[\s:~])(\w+)\s*\(([\w\s,<>\[\].=&':/*]*?)\)\s*(const)?\s*(?={))"
    cppwords = ['if', 'while', 'do', 'for', 'switch', 'main']
    functions = [(i.group(1), i.group(2), i.group(3)) for i in re.finditer(rproc, text) if i.group(2) not in cppwords]

    return functions


def find_function_body(text, function):
    position = text.find(function[0])
    if position != -1:

        #get first open bracket
        while text[position] != "{" and text[position] != ";" and position != len(text):
            position += 1
        if text[position] == "{":
            start = position
            end = start + helper.find_adjacent_bracket(text[position:], "{}")
            return text[start:end]

        raise SystemError("Incorrect bracket positions")