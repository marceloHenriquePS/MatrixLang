import pytest
from importlib import import_module


evaluator = import_module('src.evaluator')


def test_evaluate_create_success_new():
    ast = ('CREATE', [[1, 2], [3, 4]])
    env = evaluator.evaluate(ast, {})
    assert '_last' in env
    assert env['_last'] == [[1, 2], [3, 4]]


def test_evaluate_create_invalid_matrix_new():
    ast = ('CREATE', [[1, 2], [3]])
    with pytest.raises(evaluator.EvalError):
        evaluator.evaluate(ast, {})
