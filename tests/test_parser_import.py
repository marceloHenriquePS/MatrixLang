def test_parser_import():
    import importlib
    module = importlib.import_module('src.matrix_parser')
    assert hasattr(module, 'matrix_parser')
