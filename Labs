from datetime import datetime
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y
# Ввод данных
a = int(input())
b = int(input())
# Засекаем начальное время
start_time = datetime.now()
# Вычисление НОД и коэффициентов
d, x, y = extended_gcd(a, b)
end_time = datetime.now()
elapsed_time = end_time - start_time
# Вывод результата
print(d, x, y)
print(f"Время выполнения: {elapsed_time}")

 


      
           
        

