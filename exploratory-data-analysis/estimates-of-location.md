## Estimates of Location

Variables with measured or count data might have thousands of distinct values. A basic step in exploring your data is getting 
a “typical value” for each feature (variable): an estimate of where most of the data is located (i.e., its central tendency).

- Mean : The sum of all values divided by the number of values.
  - Synonyms : average
- Weighted mean : The sum of all values times a weight divided by the sum of the weights.
  - Synonyms : weighted average
- Median : The value such that one-half of the data lies above and below.
  - Synonyms : 50th percentile
- Weighted median : The value such that one-half of the sum of the weights lies above and below the sorted data.
- Trimmed mean : The average of all values after dropping a fixed number of extreme values.
  - Synonyms : truncated mean
- Robust : Not sensitive to extreme values.
  - Synonyms : resistant
- Outlier : A data value that is very different from most of the data.
  - Synonyms : extreme value


**NOTE:** While the mean is easy to compute, it may not always be the best measure for a central value. For this reason, statisticians have developed several alternative estimates to the mean.

## Metrics and Estimates:
statisticians estimate, and data scientists measure.

Statisticians often use the term estimates for values calculated from the data at hand, to draw a distinction between what we see from the data, and the theoretical true or exact state of affairs. 

Data scientists are more likely to refer to such values as a metric. 

The difference reflects the approach of statistics versus data science: accounting for uncertainty lies at the heart of the discipline of statistics, whereas concrete business or organizational objectives are the focus of data science.
