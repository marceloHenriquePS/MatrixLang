from . import matrix_parser
from .validator import validate_matrix

def parse_and_validate(input_string):
    ast = matrix_parser.matrix_parser.parse(input_string)

    if ast is None:
        raise ValueError("Syntax error: could not parse input")

    if ast[0] == 'CREATE':
        matrix = ast[1]
    else:
        raise ValueError("Unsupported operation")
    
    validate_matrix(matrix)
    
    return matrix

def main():
    matrixes = ["""CREATE(
                    [
                        [1,2,3],
                        [3,4,4],
                        [5,6,7]
                    ]
                );""",]

    for input_str in matrixes:
        try:
            matrix = parse_and_validate(input_str)
            print("Parsed and validated matrix:", matrix)
        except ValueError as e:
            print("Validation error:", e)


if __name__ == "__main__":
    main()
