from . import matrix_parser
from .validator import validate_matrix
from .evaluator import evaluate

env = {}

def parse(matrix_str):
    ast = matrix_parser.matrix_parser.parse(matrix_str)
    if not ast:
        raise ValueError("Syntax error: could not parse input")
    return ast

def main():
    matrix = """matrix = CREATE
                    [
                        [1,2,3],
                        [3,4,4],
                        [5,6,7]
                    ]
                ;"""
    
    matrix = """matrix = CREATE
                    [
                        [1,2,3],
                        [3,4,4],
                        [8,8,8]
                    ]
                ;"""
    
    print = """PRINT matrix;"""

    ast = parse(matrix)
    evaluate(ast, env)

    ast = parse(print)
    evaluate(ast, env)

    # printtest = ["""myMatrix = CREATE [[1,2,3],[3,4,4]];""", 
    #             """PRINT myMatrix;"""]
    
    # for m in printtest:
    #     ast = parse(m)
    #     evaluate(ast, env)

    # ast_create = ('CREATE', 'myMatrix', [[1,2,3],[4,5,6]])
    # evaluate(ast_create, env)

    # ast_print = ('PRINT', 'myMatrix')
    # evaluate(ast_print, env)


if __name__ == "__main__":
    main()
