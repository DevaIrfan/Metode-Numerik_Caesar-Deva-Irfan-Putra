# Caesar Deva Irfan Putra 21120123130062
# Metode Secant
import numpy as np

def f1(x, y): return x**2 + x*y - 10
def f2(x, y): return y + 3*x*y**2 - 57

def print_header(title):
    print(f"\n=== {title} ===")
    print("Caesar Deva Irfan Putra 21120123130062")
    print("-" * 70)
    print(f"{'i':<5}{'x':>12}{'y':>12}{'deltaX':>15}{'deltaY':>15}")
    print("-" * 70)

def secant(x0, y0, x1, y1, tol=1e-6, max_iter=50):
    print_header("Metode Secant")
    for i in range(max_iter):
        F0 = np.array([f1(x0, y0), f2(x0, y0)])
        F1 = np.array([f1(x1, y1), f2(x1, y1)])
        J_approx = (F1 - F0) / np.array([x1 - x0, y1 - y0])
        x2 = x1 - F1[0] / J_approx[0]
        y2 = y1 - F1[1] / J_approx[1]
        deltaX = abs(x2 - x1)
        deltaY = abs(y2 - y1)
        print(f"{i:<5}{x1:>12.6f}{y1:>12.6f}{deltaX:>15.6f}{deltaY:>15.6f}")
        if deltaX < tol and deltaY < tol:
            break
        x0, y0 = x1, y1
        x1, y1 = x2, y2
    print(f"Hasil akhir: x={x2:.6f}, y={y2:.6f}")
    return x2, y2

if __name__ == "__main__":
    secant(1.4, 3.4, 1.5, 3.5)
