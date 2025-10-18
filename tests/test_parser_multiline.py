from importlib import import_module


def test_parser_accepts_multiline_matrix():
    module = import_module('src.matrix_parser')
    parser = module.matrix_parser

    input_str = (
        "CREATE(\n"
        "    [\n"
        "       [1, 2],\n"
        "       [3, 4]\n"
        "    ]\n"
        ");"
    )

    ast = parser.parse(input_str)
    assert ast[0] == 'CREATE'
    assert ast[1] == [[1, 2], [3, 4]]
