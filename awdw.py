import numpy as np
import time
from scipy.linalg import blas
print("Савенков Захар Владимирович 090304 РПИб-о24")
print("1-й вариант")
# Генерация случайных матриц
n = 2048
A = np.random.rand(n, n).astype(np.complex64) + 1j * np.random.rand(n, n).astype(np.complex64)
B = np.random.rand(n, n).astype(np.complex64) + 1j * np.random.rand(n, n).astype(np.complex64)
# подчёт производительности и сложности
def dif(n, t):
    c = 2 * n ** 3
    p = c / t * 10 ** -6
    print("сложность алгоритма по формуле c = 2 n**3 = ",c)
    print("производительность в MFlops =", p)
# Перемножение матриц
start_time = time.time()
C = np.zeros((n, n), dtype=np.complex64)
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i, j] += A[i, k] * B[k, j]
end_time = time.time()
t1 = end_time - start_time
dif(n, t1)
print(f"Время работы: {t1:.6f} секунд")



print("2-й вариант")
# Перемножение матриц с использованием cblas_cgemm
start_time = time.time()
C = blas.cgemm(1.0, A, B, 0.0, overwrite_c=False)
end_time = time.time()
t2 = end_time - start_time
# Оценка производительности
dif(n, t2)
print(f"Время работы: {t2:.6f} секунд")

print("3-й вариант")
def optimized_block_matrix_multiply(A, B, block_size=256):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.complex64)
    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            for k in range(0, n, block_size):
                # Определяем размеры блоков
                i_end = min(i + block_size, n)
                j_end = min(j + block_size, n)
                k_end = min(k + block_size, n)
                # Перемножаем блоки
                C[i:i_end, j:j_end] += np.dot(A[i:i_end, k:k_end], B[k:k_end, j:j_end])
    return C



# Перемножение матриц с использованием блочного алгоритма
block_size = 64  # Размер блока
start_time = time.time()
D = optimized_block_matrix_multiply(A, B)

end_time = time.time()
t3 = end_time - start_time

# Оценка производительности
dif(n, t3)
print(f"Время работы: {t3:.6f} секунд")
