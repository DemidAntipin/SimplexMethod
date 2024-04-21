import numpy as np

class SimplexMethod:
    def __init__(self, c, A, b):
        self.c = c
        self.A = A
        self.b = b
        self.m, self.n = A.shape
        self.tableau = None

    def solve(self):
        c, A, b = self.c, self.A, self.b
        tableau = np.vstack([np.hstack([1, np.zeros(self.n), 0]), np.hstack([0, -c, 0]), np.column_stack([b, A, np.zeros(self.m)])])

        def pivot_col(tableau):
            return np.where(tableau[0, 1:-1] < 0)[0][0] + 1

        def pivot_row(tableau, col):
            candidates = [(i, tableau[i, 0] / tableau[i, col]) for i in range(1, tableau.shape[0]) if tableau[i, col] > 0]
            return min(candidates, key=lambda x: x[1])[0]

        def pivot_operation(tableau, pivot):
            pivot = (pivot_row(tableau, pivot_col(tableau)), pivot_col(tableau))
            tableau[pivot] /= tableau[pivot]
            for i in range(tableau.shape[0]):
                if i == pivot[0]:
                    continue
                tableau[i] -= tableau[i, pivot[1]] * tableau[pivot]

        while min(tableau[0, 1:-1]) < 0:
            pivot = (pivot_row(tableau, pivot_col(tableau)), pivot_col(tableau))
            pivot_operation(tableau, pivot)

        basic_vars = np.where(tableau[0, 1:-1] == 0)[0]
        opt_solution = {i: 0 for i in range(1, self.n + 1)}
        for i in range(len(basic_vars)):
            if basic_vars[i] < self.n:
                opt_solution[basic_vars[i] + 1] = tableau[i+1, 0]
        
        return opt_solution, -tableau[0, -1]


