# Classification:

### Binary Classification:
   - SVM and Linear classifier are strictly binary classifiers.
   - Whereas, Random Forest or Naive Bayes classifiers are capable of handling multiple classes directly.

#### Stratigies for Multiclass classification using Binary Classifiers: 
1. One vs All:
   - You train n number of binary classifier, where is number of classes.
   - Take scores from all classifiers and then take score from classifier which have highest score.
   - So, if you want to classify digits 0 to 9, you need 10 binary classifiers.
   
 2. One vs One:
   - Train a binary classifier for every pair classes. So, if you clasees 0 to 9, you need 1 classifier to classify 0s and 1s, one to classify 0s and 2s, one to classify, 0s and 3s,...and one to classify 1s and 2s,..etc.
   - So, if you N classes (10 classes: 0 to 9) you will need N * (N-1)/2 binary classifiers.
   - So, if you have 10 classes: 0 to 9, you will need 45 binary classifiers.
   
