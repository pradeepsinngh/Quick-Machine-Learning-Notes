## Resampling

Resampling in statistics means to repeatedly sample values from observed data, with a general goal of assessing random 
variability in a statistic.

There are two main types of resampling procedures: 
- the bootstrap and 
- permutation tests. 

The bootstrap is used to assess the reliability of an estimate. Permutation tests are used to test hypotheses, typically involving two or more groups.

**Permutation test :** The procedure of combining two or more samples together, and randomly (or exhaustively) reallocating the observations to resamples. Also, called Randomization test, random permutation test, exact test.

**With or without replacement :** In sampling, whether or not an item is returned to the sample before the next draw.

## Permutation Test
- In a permutation test, two or more samples are involved, typically the groups in an A/B or other hypothesis test. 
- Permute means to change the order of a set of values. 
- The permutation procedure is as follows:
  - Combine the results from the different groups in a single data set.
  - Shuffle the combined data, then randomly draw (without replacing) a resample of the same size as group A.
  - From the remaining data, randomly draw (without replacing) a resample of the same size as group B.
  - Do the same for groups C, D, and so on.
  - Whatever statistic or estimate was calculated for the original samples (e.g., difference in group proportions), calculate it now for the resamples, and record; this constitutes one permutation iteration.
  - Repeat the previous steps R times to yield a permutation distribution of the test statistic.
  - Now go back to the observed difference between groups and compare it to the set of permuted differences. 
  - If the observed difference lies well within the set of permuted differences, then we have not proven anything—the observed difference is within the range of what chance might produce. 
  - However, if the observed difference lies outside most of the permutation distribution, then we conclude that chance is not responsible. In technical terms, the difference is statistically significant.
