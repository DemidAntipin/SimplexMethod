import numpy as np
import pytest

from SimplexMethod.SimplexMethod import SimplexMethod

@pytest.fixture
def problem1():
    c = np.array([-2, -3, -4], dtype=float)
    A = np.array([[3, 2, 1], [2, 5, 3], [4, 2, 2]], dtype=float)
    b = np.array([10, 15, 18], dtype=float)
    return SimplexMethod(c, A, b)

@pytest.fixture
def problem2():
    c = np.array([-1, -3, -5], dtype=float)
    A = np.array([[2, 1, 2], [4, 1, 1], [3, 4, 2]], dtype=float)
    b = np.array([4, 6, 7], dtype=float)
    return SimplexMethod(c, A, b)

def test_simplex_method1(problem1):
    opt_solution, opt_value = problem1.solve()
    opt_solution = {k: float(v) for k, v in opt_solution.items()}
    assert opt_solution == {1: 0.0, 2: 10.0, 3: 15.0}

def test_simplex_method2(problem2):
    opt_solution, opt_value = problem2.solve()
    opt_solution = {k: float(v) for k, v in opt_solution.items()}
    assert opt_solution == {1: 0.0, 2: 4.0, 3: 6.0}
