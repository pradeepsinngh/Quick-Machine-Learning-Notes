# Convolutional Neural Networks:

### Inspiration for CNNs:
Neurons in the visual cortex have a small local receptive field, meaning they react only to visual stimuli located in a limited region of the visual field. The receptive fields of different neurons may overlap, and together they tile the whole visual fields. 

Also, some neurons react only to images of horizontal lines, while others react only to lines with different orientations. Some neurons have larger receptive fiels, and they react to more complex patters that are combinations of the lower level patterns. This observations led to the idea that the higher level neurons are based on the outputs of neighboring lower-level neurons. 

This powerful architecture, where you have neurons at different levels doing different work, lower level, mide level and higher level neurons are all used to decode difffernt and complex pattersn.

#### why not simply use a regular deep neural network with fully connected layers for image recognition tasks?
Unfortunately, although this works fine for small iamges (eg: MNSIT), it breaks down for larger images becuase of huge number of parameters it require. For eg: a 100 X 100 image has 10,000 pixels, and if the first layer has just 1,000 neurons (which already serverly restricts the amount of information transmitted to the next layer), this means a total 10 millions connections. And that's just the first layer. CNN solves this problem by partially connected layers.

### Convolutional Layer:
- Neurons in the first convolutional layer are not connected to every single pixel in the input image, but only to pixels in their receptive fields.
- In turn, neurons in the 2nd layer is only connected to pixels within a small rectangle in the 1st layer and so on..
- This architecture allows network to concentrate on the low-level features in the first hidden layers and assemnle them into higher-level features  in the next hidden layer and so on.
- This hierarchical structure is common in a real-world images, which is one of the reasons why CNNs works so well for image recognition.

### Zero Padding:
- Always zero pad the borders.
- If you zero pad the image, the N increase (size/ dimesnion of image).
- **Why zero pad?** 
    - To maintain the size of the image.
    - Also padding helps apply the filter on the edge/ corner regions.
    - If we don't pad we will quickly shrink the size of image.
   
 ```
 Output size: [(N - F) / Stride] + 1
 Eg: N = 7, F = 3, Stride = 1
 Therefore, O/P : [(7-3)/1}] + 1 = 5
 ```
 
### Filters/ Kernel:
A neurons weights can be represnted as a small image of the size of their receptive field, called filter or kernels. Neurons using these weights will ignore everything (0s) in their receptive field except for the places where it has 1s, since all inputs will be multipled by 0s will be zero and with 1s will be preserved. Now if all neurons in a layer use the same filter (weights) and you feed the network the input image, the layer will output a *feature map*, which highlights the areas in a image that are most similar to the filter.

During training, a CNN finds the most useful filters for its task, and it learns to combine them into more complex patterns.

Typically, we stack n filters of size a * b with every layers. So, for eg: if we have a filter of size (5 * 5 * 3) in a layer, we will have (5 * 5 * 3) + 1 = 76 parameters (where 1 is bias term). And, if have n filters, so we have n * 76 parameters.

**NOTE:** At every spatial location, we take a dot product between filter and the specific part of the image and we get 1 number out from there.

### Stacking Multiple Feature Maps:
A convolutional layer simultaneously applies multiple filters to inputs, making it capable of detecting multiple features anywhere in its inputs.

**NOTE:** The fact that all neurons in a feature map share the same parameters dramatically reduces the number of parameters in the model, but most importantly it means that once the CNN has learned to recognize a pattern in one location, it can recognize it in any other location. In contrast, once a regular DNN has learned to recognize a pattern in one location, it can recognize it only in that particular location.

 
### Pooling Layers:
Goal is to subsample (i.e. shrink) the input image in order to reduce the computational load, memory usage, and number of parameters; thereby limiting the risk of overfitting.
 
Just like in convolutional layers, each neuron in a pooling layer is connected to the outputs of a limited number of neurons in the previous layers, located with in a small rectangular receptive field, whose size, stride and padding type is needs to be decided as before. 

However, pooling layers has no weights; all it does is aggregate the inputs using an aggregation function such as max or mean. and, it acts spatially, doesn't do anything on depth.
 
### Hyperparameters:
- Number of filters
- Filter heights
- Width of filters
- Strides
- Padding
 
Use cross-validation to find the right hyperparameters values.


---------------------------------------------------------------------------------------------------------

## Some common CNN Architectures:

1. LeNet-5
2. Alex Net
3. Google Net
4. ResNet
5. VGG






