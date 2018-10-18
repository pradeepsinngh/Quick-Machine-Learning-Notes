# Feature Engineering

1. Data Cleaning: 
Clean/ Fix Missing Values
- Get rid of those values
- Get rid of the whole attributes
- Set the value to some value (zero, mean, median etc.)

Use can use following functions/ methods in Pandas:
 - ```dropna()```
 - ```fillna()```
 - ```drop()```
 
In Scikit-Learn, we have a class called ```Imputer``` to car eof missing values. For eg: replace missing values with median,
```
from sklearn.preprocessing import Imputer
imputer = Imputer(strategy="median")
```

2. Handling Text and Categorical Attributes:
Most machine learning algorithms perfer to work with numbers, so our first approach should always be to convert text/categorical data into numbers.

1. Pandas ```factorize()``` method
   - maps each category to a different integer.
   
2. Scikit-Learn ```OneHotEncoder``` method
   - converts integer categorical vlues into one-hot vectors. For eg: 
   ```
   from sklearn.preprocessing import OneHotEncoder
   encoder = OneHotEncoder()
   housing_encoded = encoder.fit_transform(housing)
   ```

3. Scikit-Learn ```CategoricalEncoder``` method
- converts text categories to interger categories, then from integer ategories to one-hot vectors.
```
from sklearn.preprocessing import CategoricalEncoder
encoder = CategoricalEncoder()
housing_encoded = encoder.fit_transform(housing)
```
















