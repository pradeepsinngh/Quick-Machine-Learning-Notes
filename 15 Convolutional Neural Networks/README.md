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
