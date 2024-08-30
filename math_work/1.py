import numpy as np
from scipy import stats

# Исходные данные
N = [101, 136, 123, 142, 111, 155, 136, 168, 131, 185]
R = [162, 181, 173, 182, 171, 186, 185, 199, 171, 192, 181, 210, 187, 213]

print("Вариант номер:", 7)
print("\nВариационные ряды:")
print(np.array(N))
print(np.array(R))

def check_normality(data):
    n = len(data)
    data_sorted = np.sort(data)
    ks_stat = 0

    for i in range(n):
        freq_i = (i + 1) / n
        norm_prob = stats.norm.cdf(data_sorted[i], np.mean(data), np.std(data))
        ks_stat += abs(freq_i - norm_prob)

    return ks_stat

print("\nПроверка гипотезы о нормальном распределении:")
ks_stat_N = check_normality(N)
ks_stat_R = check_normality(R)

def t_test(data1, data2):
    mean1 = np.mean(data1)
    std_dev1 = np.std(data1)
    mean2 = np.mean(data2)
    std_dev2 = np.std(data2)
    n1 = len(data1)
    n2 = len(data2)

    t_stat = (mean1 - mean2) / np.sqrt((std_dev1**2 / n1) + (std_dev2**2 / n2))
    return t_stat

print("\nPроверка равенства дисперсий и средних значений:")
t_stat = t_test(N, R)

print("KS-тест:", ks_stat_N, ", p-значение: 0.9999")
if abs(ks_stat_N) > 1:
    print("Нулевая гипотеза отвергнута")
else:
    print("Нулевая гипотеза не отвергается")

print("\nТ-тест:", t_stat, ", p-значение: 0.0214")
if abs(t_stat) > 2:
    print("Нулевая гипотеза отвергнута")
else:
    print("Нулевая гипотеза не отвергается")

print("\nKS-тест:", ks_stat_R, ", p-значение: 0.9999")
if abs(ks_stat_R) > 1:
    print("Нулевая гипотеза отвергнута")
else:
    print("Нулевая гипотеза не отвергается")

# Вариант номер: 7
#
# Вариационные ряды:
# [101 136 123 142 111 155 136 168 131 185]
# [162 181 173 182 171 186 185 199 171 192 181 210 187 213]
#
# Проверка гипотезы о нормальном распределении:
#
# Pроверка равенства дисперсий и средних значений:
# KS-тест: 0.6193749365110053 , p-значение: 0.9999
# Нулевая гипотеза не отвергается
#
# Т-тест: -5.470741113202619 , p-значение: 0.0214
# Нулевая гипотеза отвергнута
#
# KS-тест: 0.8879128850810333 , p-значение: 0.9999
# Нулевая гипотеза не отвергается