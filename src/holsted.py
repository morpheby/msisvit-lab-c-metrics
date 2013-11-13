import code_cleanup, re

operators = ["+-", "&=", "^=", "|=", "/=", "<<=", "%=", "*=", ">>=",
             "-=", "&&", "||", ",", "/", "%", "*", ".", "->",
             "--", "++", "==", ">=", ">", "<=", "!=", "<<", ">>", "!", "~",
             "sizeof", "+", "-", "=", "<", "&", "^", "|", "size_t"]

function_regex = r"([A-Za-z_][0-9A-Za-z_]*\s*\()"

operand_regex = r"([^:\s;\(\)\{\}\[\]]+)"

key_words = ["int", "float", "long", "signed", "unsigned", "double", "char", "short", "break", "return", "void", "else"]


class Holsted:

    total_operators_count = 0
    unique_operators_count = 0
    total_operands_count = 0
    unique_operands_count = 0
    cleaned_code = ""

    def __init__(self, code):
        cleaned_code = code_cleanup.cleanup_sharp(code)
        cleaned_code = code_cleanup.cleanup_comments(cleaned_code)
        (cleaned_code, total_string_count, unique_string_count) = code_cleanup.cleanup_and_get_strings_count(cleaned_code)
        self.total_operands_count += total_string_count
        self.unique_operands_count += unique_string_count
        self.cleaned_code = cleaned_code

    def get_all_operators(self):
        unique_operators = set()
        total_operators = 0

        for operator in operators:
            operators_count = self.cleaned_code.count(operator)
            if operators_count > 0:
                self.cleaned_code = self.cleaned_code.replace(operator, " ")
                total_operators += operators_count
                unique_operators.add(operator)
        self.total_operators_count += total_operators
        self.unique_operators_count += len(unique_operators)

        print(self.cleaned_code)

        unique_functions = set()
        count = len(re.findall(function_regex, self.cleaned_code))
        cleanup_code = re.sub(function_regex, lambda match: [unique_functions.add(match.group(0)), " "][0], self.cleaned_code)
        self.cleaned_code = cleanup_code
        self.total_operators_count += count
        self.unique_operators_count += len(unique_functions)

        print(self.cleaned_code)

    def get_all_operands(self):
        for key in key_words:
            self.cleaned_code = self.cleaned_code.replace(key, " ")

        print(self.cleaned_code)

        operands = re.findall(operand_regex, self.cleaned_code)
        self.total_operands_count = len(operands)
        self.unique_operands_count = len(set(operands))

    def run(self):
        self.get_all_operators()
        self.get_all_operands()

        print("Общее число операторов (N1): ", self.total_operators_count)
        print("Число уникальных операторов (n1): ", self.unique_operators_count)
        print("Общее число операндов (N2): ", self.total_operands_count)
        print("Число уникальных операндов (n2): ", self.unique_operands_count)

        print("Алфавит (n): ", self.unique_operators_count + self.unique_operands_count)
        print("Экспериментальна длина программы (Nэ): ", self.total_operators_count + self.total_operands_count)
        print("Теоретическая длина программы (Nт): ", self.total_operators_count + self.total_operands_count)
