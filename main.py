import itertools

numbers = [9, 1, 2, 5]
operators = ['+', '-', '*', '/']


def get_expressions(numbers: list[int], operators: list[str]) -> list[str]:
    result = []
    for first_number, second_number, third_number, fourth_number in itertools.permutations(numbers):
        for first_operator, second_operator, third_operator in itertools.product(operators, repeat = 3):
            result.append(f'{first_number} {first_operator} {second_number} {second_operator} {third_number} {third_operator} {fourth_number}')
            result.append(f'({first_number} {first_operator} {second_number}) {second_operator} {third_number} {third_operator} {fourth_number}')
            result.append(f'({first_number} {first_operator} {second_number} {second_operator} {third_number}) {third_operator} {fourth_number}')
            result.append(f'({first_number} {first_operator} {second_number} {second_operator} {third_number} {third_operator} {fourth_number})')
            result.append(f'{first_number} {first_operator} ({second_number} {second_operator} {third_number}) {third_operator} {fourth_number}')
            result.append(f'{first_number} {first_operator} ({second_number} {second_operator} {third_number} {third_operator} {fourth_number})')
            result.append(f'{first_number} {first_operator} {second_number} {second_operator} ({third_number} {third_operator} {fourth_number})')
    return result

def get_valid_expressions(expressions: list[str]) -> list[str]:
    result = []
    for expression in expressions:
        try:
            evaluation = eval(expression)
            if evaluation == 10:
                result.append(expression)
        except:
            print('cannot do the operation: ', expression)
    return result

if __name__ == '__main__':
    expressions = get_expressions(numbers, operators)
    valid_expressions = get_valid_expressions(expressions)
    print(f'there are {len(valid_expressions)} expressions')
    for valid_expression in valid_expressions:
        print(valid_expression)