## Mean-Shift Clustering

- Mean shift clustering is a sliding-window-based algorithm that attempts to find dense areas of data points. 
- It is a centroid-based algorithm meaning that the goal is to locate the center points of each group/class, which works by updating candidates for center points to be the mean of the points within the sliding-window. 
 
Check out the graphic below for an illustration.

![Mean-Shifting Clustering](https://github.com/pradeepsinngh/Machine-Learning-Notes/blob/master/17%20Clustering/data/Mean-Shifting%20.gif)

- Consider a set of points in two-dimensional space like the above illustration. 
- Begin with a circular sliding window centered at a point C (randomly selected) and having radius r as the kernel. 
- Shift the mean: Mean shift is a hill climbing algorithm which involves shifting this kernel iteratively to a higher density region on each step until convergence.
- At every iteration the sliding window is shifted towards regions of higher density by shifting the center point to the mean of the points within the window (hence the name). The density within the sliding window is proportional to the number of points inside it. Naturally, by shifting to the mean of the points in the window it will gradually move towards areas of higher point density.
- We continue shifting the sliding window according to the mean until there is no direction at which a shift can accommodate more points inside the kernel.
- This process is done with many sliding windows until all points lie within a window. When multiple sliding windows overlap the window containing the most points is preserved. The data points are then clustered according to the sliding window in which they reside.

### Advantages:
- No need to select the number of clusters as mean-shift automatically discovers this. 
- The fact that the cluster centers converge towards the points of maximum density is also quite desirable as it is quite intuitive to understand and fits well in a naturally data-driven sense.

### Disdvantages:
- The drawback is that the selection of the window size/radius “r” can be non-trivial.
