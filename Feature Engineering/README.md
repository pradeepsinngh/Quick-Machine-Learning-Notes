# Feature Engineering

1. **Data Cleaning:**
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

2. **Handling Text and Categorical Attributes:**
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


3. **Custom Transformers:**
You need to write your own transformers for tasks such as custom cleanup operations or combining specific attributes.

4. **Feature Scaling:**
- ML algorithms doesn't work well when the I/P numerical attributes have very different scales.
- **NOTE:** Scaling the target values is generally not required.
- There are two common ways to get all attributes to have same scale: *min-max scaling* and *standardization*.

**Min-Max Scaling:** values are shifted and rescaled so that they end up ranging from 0 to 1. 
  - Many people call this normazlization.
  - We do this by substracting the min and dividing by the max-minus the min.
  - Scikit-Learn provides a transformer called ```MinMaxScaler``` for this. It has feature range hyperparamter that lets you change the range if you don't want 0-1 range fro some reason.
  
**Standardization:** First substract the mean value (so that standardized values always have zero mean), and then it divides by the variance so that the resulting distribution have unit variance.
  - Unlike, Min-Max Sacling, standardization  does not bound values to a specific range, which may be a problem for some algorithm -- For eg, Neural N/W often expect input value ranging from 0 to 1.
  - Standardization is much less affected by outliers.
  - Scikit-Learn provides a transformer called ```StandardScaler``` for this.











