# Statical characteristics

## Installation

+ Download and unpack files
+ Install with the command below

```sh
pip install 'path_to_files'\statistical_charasteristics\dist\statistical_characteristics-0.0.1-py3-none-any.whl
```
+ import 

```sh
from statistical_characteristics.statistical_characteristics import StaticalCharacteristic
```

+ Done!

## Using:

+ Initialise class with needed data
```
tmp = StaticalCharacteristic(data1, data2)
```
+ Use one of provided functions to calculate the coefficient
```sh
what_i_need = tmp.normalised_average_absolute_difference()
```
## Implemented coefficiens
+ maximum_difference()
+ average_absolute_difference()
+ normalised_average_absolute_difference()
+ average_quadratic_error()
+ normalised_average_quadratic_error()
