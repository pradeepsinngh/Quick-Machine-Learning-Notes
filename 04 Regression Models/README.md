# Regression Models
- Regression means, a measure of the relation between one variable (e.g. output) and corresponding values of other variables (eg input variables)
- We fit a curve / line to the data points, in such a manner that the differences between the distances of data points from the curve or line is minimized.


### Performace Measure for Regression Problems:
1. **Root Mean Square Error(RMSE):**
   - gives idea how much error the system typically makes in its prediction.
   - gives higher weight for larger errors.
   - corresponds to eculidian norm: also called L2 norm
   - denoted as ```|| . ||```

2. **Mean Absolute Error (MAE):**
   - also called Avg. Absolute Deviation.
   - also called Manhattan norm, becuase it measure the dist b/w 2 point ina  city if you can only travel along orthogonal 
   city blocks.
   - also called L1 norm
   
- The higher the norm index, the more it focuses on larger values and neglects the small ones. 
- This is why RMSE is more sensitive to outliers then MAE.
-  But, when outliers are exponentially rare (like a bell-shaped curve), the RMSE performs very well and is generally preferred.

### Notes on Correlation Measure:

1. Correlation coefficient ranges from -1 to 1. 
2. When correlation is close to 1, it means there is a strong positive correlation.
   - For eg: Median house value tends to go up when the median income goes up.
3. When correlation is close to -1, it means that there is negative correlation.
   - Foe eg: house prices goes down as you go down the hill.
4. When correlation is close to 0, it means that there is No linear correlation.

**NOTE:** The correlation coefficient only measures linear correlations. for eg: if X goes up/down, Y goes down/up. It may completely miss the non-linear relationships, eg: if x is close to zero then y generally goes up/down.
