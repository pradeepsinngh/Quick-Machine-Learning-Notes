## Projection

In most problems, training instances are not spread out uniformly across all dimensions. Many features are almost constant, while others are highly correlated. As a result, all the training instances actually lie within a much lower dimensional subspace of the high dimensional space.

For eg: if you see a dataset in 3D, you might see all the training instances might lie cloas a plane: this woild be a 2D subspace of a high dimensional (3D) space. Now, if we project every training instance perpendicular onto this subspace, we get new 2D dataset. Ta Da! We have just reduced the dataset's dimensionality from 3D to 2D.

However, projection is not always the best approach to dimensioanlity reduction. In many cases, the subspace may twist and turn, such as in famous swiss roll toy dataset.

![Swiss Roll](/images/swiss-roll.png)

Simply projecting onto a plan (eg: by dropping x3) would squash different layers of swiss roll together. however, what we want is to unroll the Swiss roll to obtain the 2D dataset.

![Swiss Roll Unrolled](/images/swiss-roll-unrolled.png)
