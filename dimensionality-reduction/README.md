### Why do we need to reduce dimensionality of our dataset?

Many Machine Learning problems involve thousands or even millions of features for each training instances. Now, training your model over millions of features for each training instances is gonna make your training slow and it makes harder for your model to find good solution. This is what referred to as *Curse of dimensionality*.

It is often possible to reduce the number of features considerably, turning an intractable problem into a tractable one. Let's see an example: 

Consider MNIST dataset, all the images in MNSIT have white pixels on the border (as subject is centered), so we can completely drop these pixels as they dont carry any information. Also, two neighbouring pixels are often highly correlated: you can merge these two pixels into a single pixel (eg, by taking the mean of the two pixel intensities), you will not lose much information.

### Dimensionality reduction for Visualization:
Apart from speeding up training, dimensionality reduction is also used for data visualization. Reducing the number of dimensions down to two (or three) makes it possible to plot a high-dimensional training set and often gain some important 
insights by visually detecting patterns, such as clusters.

## Limitations of dimensionality reduction:

### Does reducing dimension leads to lose of infomrtaion?

1. Yes, reducing dimensions does lose some information (just like compressing an image JPEG can degrade its quality), so even though it will speed up training it may also make our system perform slightly worse.

2. It makes machine learning pipeline more complex and thus harder to maintain.

## What should be your approach?
In general,  you should try to train your model with orginal dataset before considering dimensionality reduction. If training is too slow, then only consider dimensionality reduction. In some case however, dimensionality reduction can help you filter out some noise and some unnecessary details and thus result in higher performace. But in general it won't; it will just speed up training.


## Main approaches in Dimensionality Reduction:
1. Projection
2. Manifold Learning
