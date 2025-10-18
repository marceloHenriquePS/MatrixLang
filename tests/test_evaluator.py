import pytest
from importlib import import_module


evaluator = import_module('src.evaluator')


def test_evaluate_create_success():
    ast = ('CREATE', 'm', [[1, 2], [3, 4]])
    env = evaluator.evaluate(ast, {})
    assert 'm' in env
    assert env['m'] == [[1, 2], [3, 4]]


def test_evaluate_create_invalid_matrix():
    ast = ('CREATE', 'm', [[1, 2], [3]])
    with pytest.raises(evaluator.EvalError):
        evaluator.evaluate(ast, {})
