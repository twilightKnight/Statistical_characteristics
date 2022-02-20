# Статистические характеристики для лаб

## Что делать?????

+ Скачать файлики с вирусами
+ Установить командой ниже

```sh
pip install 'path_to_files'\statistical_charasteristics\dist\statistical_characteristics-0.0.1-py3-none-any.whl
```
+ импортировать смешным методом

```sh
from statistical_characteristics.statistical_characteristics import StaticalCharacteristic
```

+ ???
+ profit

## А как использовать-то???

+ Инициализировать класс сравниваемыми данными
```
tmp = StaticalCharacteristic(data1, data2)
```
+ Попросить посчитать метрику
```sh
what_i_need = tmp.normalised_average_absolute_difference()
```
## А какие есть метрики у тебя-то???
+ maximum_difference()
+ average_absolute_difference()
+ normalised_average_absolute_difference()
+ average_quadratic_error()
+ normalised_average_quadratic_error()
