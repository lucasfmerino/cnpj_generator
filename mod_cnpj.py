import re
from random import randint


def just_numbers(str_var):
    new_str = re.sub(r'[^0-9]', '', str_var)
    return new_str[:-2]


def sum_for_digit(str_var):
    return sum(
        [a * b for a, b in zip(
            [int(n) for n in str_var],
            [score - 7 if score > 8 else score + 1 for score in range(len(str_var), 0, -1)])]
    )


def digit_calculation(int_var):
    d = 11 - (int_var % 11)
    return 0 if d > 9 else d


def add_especial_char(str_var):
    score = 0
    new_str = ''
    for i in str_var:
        if score == 1 or score == 4:
            i += '.'
        if score == 7:
            i += '/'
        if score == 11:
            i += '-'
        new_str += i
        score += 1
    return new_str


def digit_appends(str_var):
    # REMOVER CARCTERES NÃO NUMÉRICOS E DÍGITOS FINAIS:
    new_str = just_numbers(str_var)

    # CALCULAR PRIMEIRO DÍGITO VÁLIDO:
    sum_01 = sum_for_digit(new_str)
    digit_1 = digit_calculation(sum_01)

    # CALCULAR SEGUNDO DÍGITO VÁLIDO:
    sum_02 = sum_for_digit(new_str + str(digit_1))
    digit_2 = digit_calculation(sum_02)

    # RETORNANDO CARACTERES ESPECIAIS:
    end_str = add_especial_char(new_str + str(digit_1) + str(digit_2))

    # RESULTADO:
    return end_str


def generator():
    # GERANDO VALOR ALEATÓRIO
    random_var = ''.join([str(randint(0, 9)) for _ in range(8)]) + '0001'

    # CALCULAR PRIMEIRO DÍGITO VÁLIDO:
    sum_01 = sum_for_digit(random_var)
    digit_1 = digit_calculation(sum_01)

    # CALCULAR SEGUNDO DÍGITO VÁLIDO:
    sum_02 = sum_for_digit(random_var + str(digit_1))
    digit_2 = digit_calculation(sum_02)

    # RETORNANDO CARACTERES ESPECIAIS:
    end_str = add_especial_char(random_var + str(digit_1) + str(digit_2))

    # RESULTADO:
    return end_str


# -------------------------------------------------------------------------------------------------------------------- #
# Program tests (with validator)
if __name__ == '__main__':
    cnpj_i = generator()

    cnpj = digit_appends(cnpj_i)

    print(cnpj_i)
    print('valid' if cnpj == cnpj_i else 'invalid')


