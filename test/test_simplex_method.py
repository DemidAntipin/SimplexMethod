import numpy as np
import pytest

from simplex_method.simplex_method import SimplexMethod

@pytest.fixture
def simplex_instance():
    c = np.array([-3, -2, 0, 0])
    A = np.array([[1,  1,  1,  0],
                  [2,  1,  0,  1]])
    b = np.array([4, 5])
    return SimplexMethod(c, A, b)

def test_solve_optimal_solution(simplex_instance):
    z, x_b = simplex_instance.solve()
    assert z == -9
    assert np.allclose(x_b, np.array([2, 2]))

def test_solve_unbounded_problem():
    c = np.array([1, 1])
    A = np.array([[1, -1],
                  [-1, 1]])
    b = np.array([1, 1])
    simplex_instance = SimplexMethod(c, A, b)
    z, x_b = simplex_instance.solve()
    assert z is None
    assert x_b is None

def test_solve_infeasible_problem():
    c = np.array([1, 1])
    A = np.array([[1, 1],
                  [1, 1]])
    b = np.array([1, 2])
    simplex_instance = SimplexMethod(c, A, b)
    z, x_b = simplex_instance.solve()
    assert z is None
    assert x_b is None
