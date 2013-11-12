import re


all_strings = set()


def cleanup_string(text):
    filtered_code = re.sub("L?\"(\\\\.|[^\\\\\"])*\"", lambda match: all_strings.add(match.group(0)), text)
    print(filtered_code)


def cleanup_comments(text):
    without_comments = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", text)
    without_comments = re.sub(re.compile("//.*?\n"), "", without_comments)
    print(without_comments)