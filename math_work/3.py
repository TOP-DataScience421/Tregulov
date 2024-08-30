import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Загрузка данных
data_oil = pd.read_csv('urals_oil_rus_export_prices.csv', sep=' ')
data_diesel = pd.read_csv('dizel_fuel_rus_prices.csv', sep=' ')

# Заменяем кириллические месяцы на латинские
months = {
    'янв': 'jan', 'фев': 'feb', 'мар': 'mar', 'апр': 'apr', 'май': 'may', 'июн': 'jun',
    'июл': 'jul', 'авг': 'aug', 'сен': 'sep', 'окт': 'oct', 'ноя': 'nov', 'дек': 'dec'
}

data_oil['Date'] = data_oil['Date'].replace(months, regex=True)
data_diesel['Date'] = data_diesel['Date'].replace(months, regex=True)

# Преобразование строковых дат в формат datetime
data_oil['Date'] = pd.to_datetime(data_oil['Date'], format='%d.%b.%y', dayfirst=True)
data_diesel['Date'] = pd.to_datetime(data_diesel['Date'], format='%d.%b.%y', dayfirst=True)

# Остальная часть кода остается без изменений
best_corr = -1
best_shift = 0
for shift in range(-12, 13):  # Например, от -12 до +12 месяцев
    shifted_dates = data_diesel['Date'] + pd.DateOffset(months=shift)
    merged = pd.merge(data_oil, data_diesel.assign(Date=shifted_dates),
                      on='Date', suffixes=('_oil', '_diesel'))

    corr = merged['Price_oil'].corr(merged['Price_diesel'])
    print(f'Shift: {shift} months, Correlation: {corr}')

    if corr > best_corr:
        best_corr = corr
        best_shift = shift

# Построение регрессионной линии для лучшего сдвига
shifted_dates = data_diesel['Date'] + pd.DateOffset(months=best_shift)
merged = pd.merge(data_oil, data_diesel.assign(Date=shifted_dates), on='Date',
                  suffixes=('_oil', '_diesel'))

slope, intercept, r_value, p_value, std_err = linregress(merged['Price_oil'],
                                                         merged['Price_diesel'])

plt.scatter(merged['Price_oil'], merged['Price_diesel'], label='Data points')
plt.plot(merged['Price_oil'], slope * merged['Price_oil'] + intercept,
         color='red', label='Regression line')
plt.xlabel('Oil Prices')
plt.ylabel('Diesel Prices')
plt.title(f'Linear Regression (Shift: {best_shift} months)')
plt.legend()
plt.savefig('regression_plot.png', dpi=300)
plt.show()


print(f'Optimal Shift: {best_shift} months')
print(f'Regression Line: y = {slope:.2f}x + {intercept:.2f}')

# Shift: -12 months, Correlation: -0.2199730485500646
# Shift: -11 months, Correlation: -0.18426457454803494
# Shift: -10 months, Correlation: -0.18792856140493405
# Shift: -9 months, Correlation: -0.16343701239606373
# Shift: -8 months, Correlation: -0.07105849352363913
# Shift: -7 months, Correlation: 0.097658146000926
# Shift: -6 months, Correlation: 0.27327082603558966
# Shift: -5 months, Correlation: 0.2857681383634565
# Shift: -4 months, Correlation: 0.2819089467545891
# Shift: -3 months, Correlation: 0.7492538438108417
# Shift: -2 months, Correlation: 0.594301880308876
# Shift: -1 months, Correlation: 0.38104116206407174
# Shift: 0 months, Correlation: 0.8322116794457431
# Shift: 1 months, Correlation: 0.5722786651742973
# Shift: 2 months, Correlation: 0.3734081799835663
# Shift: 3 months, Correlation: 0.6854454280577629
# Shift: 4 months, Correlation: 0.7560428353229782
# Shift: 5 months, Correlation: 0.7210686553550679
# Shift: 6 months, Correlation: 0.674729805886475
# Shift: 7 months, Correlation: 0.6782607423869531
# Shift: 8 months, Correlation: 0.740319207819601
# Shift: 9 months, Correlation: 0.6493553683827877
# Shift: 10 months, Correlation: 0.38462438501658064
# Shift: 11 months, Correlation: 0.6114630171113762
# Shift: 12 months, Correlation: 0.6354933991998417
# Optimal Shift: 0 months
# Regression Line: y = 0.07x + 10.61
