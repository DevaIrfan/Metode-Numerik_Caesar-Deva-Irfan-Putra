# Caesar Deva Irfan Putra 21120123130062
# Metode Jacobi
import numpy as np

def f1(x, y): return x**2 + x*y - 10
def f2(x, y): return y + 3*x*y**2 - 57

def g1B(x, y):
    val = 10 - x*y
    return np.sqrt(val) if val >= 0 else x

def g2A(x, y):
    return 57 - 3*x*y**2

def print_header(title):
    print(f"\n=== {title} ===")
    print("Caesar Deva Irfan Putra 21120123130062")
    print("-" * 70)
    print(f"{'i':<5}{'x':>12}{'y':>12}{'deltaX':>15}{'deltaY':>15}")
    print("-" * 70)

def jacobi(x0, y0, tol=1e-6, max_iter=50):
    print_header("Metode Jacobi")
    for i in range(max_iter):
        x_new = g1B(x0, y0)
        y_new = g2A(x0, y0)
        deltaX = abs(x_new - x0)
        deltaY = abs(y_new - y0)
        print(f"{i:<5}{x0:>12.6f}{y0:>12.6f}{deltaX:>15.6f}{deltaY:>15.6f}")
        if deltaX < tol and deltaY < tol:
            break
        x0, y0 = x_new, y_new
    print(f"Hasil akhir: x={x_new:.6f}, y={y_new:.6f}")
    return x_new, y_new

if __name__ == "__main__":
    jacobi(1.5, 3.5)
