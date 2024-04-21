import numpy as np

class SimplexMethod:
    def __init__(self, c: np.ndarray, A: np.ndarray, b: np.ndarray):
        self.c = c
        self.A = A
        self.b = b

    def solve(self):
        m, n = self.A.shape
        c = np.concatenate((self.c, np.zeros(m)))
        A = np.hstack((self.A, np.eye(m)))
        c_b = c[n:]
        c_n = c[:n]
        B = A[:, n:]
        N = A[:, :n]
        x_b = np.linalg.solve(B, self.b)
        z = np.dot(c_b, x_b)
        while True:
            if np.all(c_n <= 0):
                return z, x_b

            entering_var = np.argmax(c_n)

            if np.all(A[:, entering_var] <= 0):
                return None, None

            ratios = x_b / A[:, entering_var]
            leaving_var = np.argmin(ratios)

            B_inv = np.linalg.inv(B)
            d = np.dot(B_inv, A[leaving_var])
            t = d[entering_var]
            B_inv[leaving_var] /= t
            for i in range(m):
                if i != leaving_var:
                    B_inv[i] -= d[i] / t * B_inv[leaving_var]
            x_b -= x_b[leaving_var] / t * d
            z += c_n[entering_var] * x_b[leaving_var] / t
            c_b[leaving_var], c_n[entering_var] = c_n[entering_var], c_b[leaving_var]
            B[:, leaving_var], N[:, entering_var] = N[:, entering_var], B[:, leaving_var]
            A[:, [entering_var, n + leaving_var]] = A[:, [n + leaving_var, entering_var]]
