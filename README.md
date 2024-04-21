# Документация SimplexMethod

## Описание

Класс `SimplexMethod` использует симплекс-метод для решения задач линейного программирования. Он принимает коэффициенты целевой функции `c`, матрицу ограничений `A`, вектор значений `b` и находит оптимальное решение задачи.

## Методы

**`__init__(self, c: np.ndarray, A: np.ndarray, b: np.ndarray)`**

+ **Описание: ** Инициализирует объект `SimplexMethod` с коэффициентами целевой функции `c`, матрицой ограничений `A` и вектором значений `b`.

+ **Параметры: **

	+ `c` (numpy.ndarray): Коэффициенты целевой функции.
	+ `A` (numpy.ndarray): Матрица ограничений.
	+ `b` (numpy.ndarray): Вектор значений.

**`solve(self)`**

+ **Описание: ** Решает задачу линейного программирования симплекс-методом.

+ **Возвращает: **

	+ `optimal_value` (float): Оптимальное значение целевой функции.
	+ `optimal_solution` (numpy.ndarray): Вектор значений, при котором получается оптимальное решение целевой функции.

## Установка

```bash
git clone https://github.com/DemidAntipin/SimplexMethod.git
cd SimplexMethod
python setup.py
```

Или

```bash
pip install -e git+https://github.com/DemidAntipin/SimplexMethod.git#egg=SimplexMethod
```
