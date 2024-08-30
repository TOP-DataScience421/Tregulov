import numpy as np
import pandas as pd

# Загрузка данных
science_data = pd.read_csv('science_investetions.csv', sep=' ')
malignancy_data = pd.read_csv('early_malignancy.csv', sep=' ')

# Сортировка данных по годам
science_data = science_data.sort_values(by=science_data.columns[0])
malignancy_data = malignancy_data.sort_values(by=malignancy_data.columns[0])

# Извлечение значений
science_values = science_data[science_data.columns[1]].values
malignancy_values = malignancy_data[malignancy_data.columns[1]].values
years = science_data[science_data.columns[0]].values

# Нормализация данных
science_values_normalized = (science_values - np.mean(science_values)) / np.std(science_values)
malignancy_values_normalized = (malignancy_values - np.mean(malignancy_values)) / np.std(malignancy_values)


def calculate_correlations(science_values, malignancy_values, max_shift):
    max_correlation = None
    best_shift = 0
    best_science_series = None
    best_malignancy_series = None

    for shift in range(-max_shift, max_shift + 1):
        if shift > 0:
            # Научные данные смещены вперед
            shifted_science = science_values[:-shift]
            shifted_malignancy = malignancy_values[shift:]
        elif shift < 0:
            # Данные по заболеваемости смещены вперед
            shifted_science = science_values[-shift:]
            shifted_malignancy = malignancy_values[:shift]
        else:
            # Нет сдвига
            shifted_science = science_values
            shifted_malignancy = malignancy_values

        min_len = min(len(shifted_science), len(shifted_malignancy))
        shifted_science = shifted_science[:min_len]
        shifted_malignancy = shifted_malignancy[:min_len]

        # Вычисление корреляции
        correlation = np.corrcoef(shifted_science, shifted_malignancy)[0, 1]

        # Сохранение максимальной корреляции
        if max_correlation is None or abs(correlation) > abs(max_correlation):
            max_correlation = correlation
            best_shift = shift
            best_science_series = shifted_science
            best_malignancy_series = shifted_malignancy

        print(f'Сдвиг: {shift} год(а)')
        print(f'Ряд science: {shifted_science}')
        print(f'Ряд malignancy: {shifted_malignancy}')
        print(f'Коэффициент корреляции: {correlation}\n')

    return best_shift, max_correlation, best_science_series, best_malignancy_series

max_shift = 5  # Например, проверим сдвиги до 5 лет
best_shift, max_correlation, best_science_series, best_malignancy_series = calculate_correlations(science_values_normalized, malignancy_values_normalized, max_shift)

print(f'Максимальная корреляция {max_correlation} была достигнута при сдвиге {best_shift} года(лет).')

# Сдвиг: -5 год(а)
# Ряд science: [-0.49829094 -0.33987892 -0.00299288  0.20480231  0.27358717  0.54348844]
# Ряд malignancy: [-1.80415377 -1.37736471 -0.77274687 -0.41708931 -0.09699751  0.18752853]
# Коэффициент корреляции: 0.9933240662336457
#
# Сдвиг: -4 год(а)
# Ряд science: [-0.80417728 -0.49829094 -0.33987892 -0.00299288  0.20480231  0.27358717
#   0.54348844]
# Ряд malignancy: [-1.80415377 -1.37736471 -0.77274687 -0.41708931 -0.09699751  0.18752853
#   0.54318608]
# Коэффициент корреляции: 0.9915103933608597
#
# Сдвиг: -3 год(а)
# Ряд science: [-1.08275162 -0.80417728 -0.49829094 -0.33987892 -0.00299288  0.20480231
#   0.27358717  0.54348844]
# Ряд malignancy: [-1.80415377 -1.37736471 -0.77274687 -0.41708931 -0.09699751  0.18752853
#   0.54318608  0.15196277]
# Коэффициент корреляции: 0.9573206662234112
#
# Сдвиг: -2 год(а)
# Ряд science: [-1.18313593 -1.08275162 -0.80417728 -0.49829094 -0.33987892 -0.00299288
#   0.20480231  0.27358717  0.54348844]
# Ряд malignancy: [-1.80415377 -1.37736471 -0.77274687 -0.41708931 -0.09699751  0.18752853
#   0.54318608  0.15196277  0.72101486]
# Коэффициент корреляции: 0.9672414482859641
#
# Сдвиг: -1 год(а)
# Ряд science: [-1.36009028 -1.18313593 -1.08275162 -0.80417728 -0.49829094 -0.33987892
#  -0.00299288  0.20480231  0.27358717  0.54348844]
# Ряд malignancy: [-1.80415377 -1.37736471 -0.77274687 -0.41708931 -0.09699751  0.18752853
#   0.54318608  0.15196277  0.72101486  1.21893543]
# Коэффициент корреляции: 0.9540270649850032
#
# Сдвиг: 0 год(а)
# Ряд science: [-1.56459312 -1.36009028 -1.18313593 -1.08275162 -0.80417728 -0.49829094
#  -0.33987892 -0.00299288  0.20480231  0.27358717  0.54348844]
# Ряд malignancy: [-1.80415377 -1.37736471 -0.77274687 -0.41708931 -0.09699751  0.18752853
#   0.54318608  0.15196277  0.72101486  1.21893543  1.6457245 ]
# Коэффициент корреляции: 0.9550894123491617
#
# Сдвиг: 1 год(а)
# Ряд science: [-1.56459312 -1.36009028 -1.18313593 -1.08275162 -0.80417728 -0.49829094
#  -0.33987892 -0.00299288  0.20480231  0.27358717]
# Ряд malignancy: [-1.37736471 -0.77274687 -0.41708931 -0.09699751  0.18752853  0.54318608
#   0.15196277  0.72101486  1.21893543  1.6457245 ]
# Коэффициент корреляции: 0.9554713323413168
#
# Сдвиг: 2 год(а)
# Ряд science: [-1.56459312 -1.36009028 -1.18313593 -1.08275162 -0.80417728 -0.49829094
#  -0.33987892 -0.00299288  0.20480231]
# Ряд malignancy: [-0.77274687 -0.41708931 -0.09699751  0.18752853  0.54318608  0.15196277
#   0.72101486  1.21893543  1.6457245 ]
# Коэффициент корреляции: 0.9526644633032525
#
# Сдвиг: 3 год(а)
# Ряд science: [-1.56459312 -1.36009028 -1.18313593 -1.08275162 -0.80417728 -0.49829094
#  -0.33987892 -0.00299288]
# Ряд malignancy: [-0.41708931 -0.09699751  0.18752853  0.54318608  0.15196277  0.72101486
#   1.21893543  1.6457245 ]
# Коэффициент корреляции: 0.9460048057664611
#
# Сдвиг: 4 год(а)
# Ряд science: [-1.56459312 -1.36009028 -1.18313593 -1.08275162 -0.80417728 -0.49829094
#  -0.33987892]
# Ряд malignancy: [-0.09699751  0.18752853  0.54318608  0.15196277  0.72101486  1.21893543
#   1.6457245 ]
# Коэффициент корреляции: 0.955110243305614
#
# Сдвиг: 5 год(а)
# Ряд science: [-1.56459312 -1.36009028 -1.18313593 -1.08275162 -0.80417728 -0.49829094]
# Ряд malignancy: [0.18752853 0.54318608 0.15196277 0.72101486 1.21893543 1.6457245 ]
# Коэффициент корреляции: 0.9198971201380847
#
# Максимальная корреляция 0.9933240662336457 была достигнута при сдвиге -5 года(лет).