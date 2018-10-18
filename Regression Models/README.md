# Regression Models

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
