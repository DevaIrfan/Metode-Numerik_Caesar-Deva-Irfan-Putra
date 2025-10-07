# Caesar Deva Irfan Putra 21120123130062
# Metode Newton-Raphson
import numpy as np

def f1(x, y): return x**2 + x*y - 10
def f2(x, y): return y + 3*x*y**2 - 57

def df1dx(x, y): return 2*x + y
def df1dy(x, y): return x
def df2dx(x, y): return 3*y**2
def df2dy(x, y): return 1 + 6*x*y

def print_header(title):
    print(f"\n=== {title} ===")
    print("Caesar Deva Irfan Putra 21120123130062")
    print("-" * 70)
    print(f"{'i':<5}{'x':>12}{'y':>12}{'deltaX':>15}{'deltaY':>15}")
    print("-" * 70)

def newton_raphson(x0, y0, tol=1e-6, max_iter=50):
    print_header("Metode Newton-Raphson")
    for i in range(max_iter):
        J = np.array([[df1dx(x0, y0), df1dy(x0, y0)],
                      [df2dx(x0, y0), df2dy(x0, y0)]])
        F = np.array([f1(x0, y0), f2(x0, y0)])
        delta = np.linalg.solve(J, -F)
        x1, y1 = x0 + delta[0], y0 + delta[1]
        deltaX = abs(x1 - x0)
        deltaY = abs(y1 - y0)
        print(f"{i:<5}{x0:>12.6f}{y0:>12.6f}{deltaX:>15.6f}{deltaY:>15.6f}")
        if np.linalg.norm(delta) < tol:
            break
        x0, y0 = x1, y1
    print(f"Hasil akhir: x={x1:.6f}, y={y1:.6f}")
    return x1, y1

if __name__ == "__main__":
    newton_raphson(1.5, 3.5)
