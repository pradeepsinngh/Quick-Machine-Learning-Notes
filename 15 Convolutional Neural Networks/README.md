# Convolutional Neural Networks:

### Inspiration for CNNs:
Neurons in the visual cortex have a small local receptive field, meaning they react only to visual stimuli located in a limited region of the visual field. The receptive fields of different neurons may overlap, and together they tile the whole visual fields. 

Also, some neurons react only to images of horizontal lines, while others react only to lines with different orientations. Some neurons have larger receptive fiels, and they react to more complex patters that are combinations of the lower level patterns. This observations led to the idea that the higher level neurons are based on the outputs of neighboring lower-level neurons. 

This powerful architecture, where you have neurons at different levels doing different work, lower level, mide level and higher level neurons are all used to decode difffernt and complex pattersn.

#### why not simply use a regular deep neural network with fully connected layers for image recognition tasks?
Unfortunately, although this works fine for small iamges (eg: MNSIT), it breaks down for larger images becuase of huge number of parameters it require. For eg: a 100 X 100 image has 10,000 pixels, and if the first layer has just 1,000 neurons (which already serverly restricts the amount of information transmitted to the next layer), this means a total 10 millions connections. And that's just the first layer. CNN solves this problem by partially connected layers.

### Convolutional Layer:

