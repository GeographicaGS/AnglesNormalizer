#Angles normalizer (with or without Numpy)

A little tool to normalize angles (e.g. latitude and longitude).
The main feature is to use Numpy arrays as input data.

You can solve a common geographical problem with this library: Bounding box crossing longitude 180 deg.

##Requeriments
* Numpy

##Usage
* Example 1: input data are Numpy array
```python
import numpy as np
from lib.numpynormalizeangles import NumpyNormalizeAngles


lower = -180
upper = 180

npna = NumpyNormalizeAngles()

arr_angles_1 = np.array([[-175.5, 185.2, 210.],
                       [-50., 195.1, 3.2],
                       [178.4, 23., 181.7]])

result_1 = npna.getValues(arr_angles, lower=lower, upper=upper)

print("Normalize angles with Numpy (1):")
print(result)

arr_angles_2 = np.linspace(180, -180, 10000)

result_2 = npna.getValues(arr_angles, lower=lower, upper=upper)

print("Normalize angles with Numpy (2):")
print(result)           
```

* Example 2: input data are an integer
```python
from lib.numpynormalizeangles import NumpyNormalizeAngles


lower = -180
upper = 180

angle = 185

npna = NumpyNormalizeAngles(usenumpy=False)

result = npna.getValues(angle, lower=lower, upper=upper)

print("Normalize angles without Numpy:")
print(result)
```


##Credits
Some parts of this work are based on code developed by Prasanth Nair, Professor at the University of Toronto Institute for Aerospace Studies (UTIAS) (http://arrow.utias.utoronto.ca/~pbn/).
https://github.com/phn/angles


##License
Released under BSD.
http://www.opensource.org/licenses/bsd-license.php.
