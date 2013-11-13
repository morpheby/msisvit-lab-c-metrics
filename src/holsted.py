import code_cleanup, re, math, functioner

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
    text = ""

    def __init__(self, code):
        self.text = code
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

    def get_theoretical_program_dictionary(self):
        functions = functioner.get_function_declaration(self.text)
        n1s = 0
        n2s = 0
        for func in functions:
            n2s += len(func[2].split(","))
        n1s = len(functions)
        return n1s, n2s

    def run(self):
        self.get_all_operators()
        self.get_all_operands()

        n1 = self.unique_operators_count
        n2 = self.unique_operands_count
        N1 = self.total_operators_count
        N2 = self.total_operands_count

        print("Общее число операторов (N1): ", self.total_operators_count)
        print("Число уникальных операторов (n1): ", self.unique_operators_count)
        print("Общее число операндов (N2): ", self.total_operands_count)
        print("Число уникальных операндов (n2): ", self.unique_operands_count)

        n = self.unique_operators_count + self.unique_operands_count
        print("Алфавит (n): ", n)

        Ne = self.total_operators_count + self.total_operands_count
        print("Экспериментальна длина программы (Nэ): ", Ne)
        Nt = n1 * math.log(n1, 2) + n2 * math.log(n2, 2)
        print("Теоретическая длина программы (Nт): ", Nt)

        V = Ne * math.log(n, 2)
        print("Объем программы (V): ", V)

        n1s, n2s = self.get_theoretical_program_dictionary()

        Vs = Nt * math.log(n1s + n2s, 2)
        print("Потенциальный oбъем (V*): ", Vs)

        L = Vs / V
        print("Уровень программы (L): ", L)

        S = 1 / L
        print("Сложность программы (S): ", S)

        Ls = (2 / n2)*(n2 / N2)
        print("Ожидание уровня программы (L'): ", Ls)

        D = 1 / Ls
        print("Трудоемкость кодирования программы (D): ", D)

        I = V / D
        print("Интеллект программы (I): ", I)

        E = Nt * math.log(n/L, 2)
        print("Оценка необходимых интеллектуальных усилий при разработке (E): ", E)
