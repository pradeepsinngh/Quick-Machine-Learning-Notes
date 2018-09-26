# What is Machine Learning?

*"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance tasks in T, as measured by P, improves with experience E."* - Tom Mitchell

### How does one teach a computer program to learn from experience E with respect to some class of tasks T and measure its performance P?

We refer to such such programs that learn from experience as machine learning models: we create these models by feeding training data into a learning algorithm.

In order to do machine learning we need data, lots and lots of data. Data (at least in [supervised learning](https://github.com/jimmychimmyy/machine_learning_notes/blob/master/ssupervised_learning.md)) gives us two variables: x and y, where x is the input(s) to our machine learning problem and y is the output.

One way to understand machine learning is to think of it as searching for a function such that `f(x) = y` (**target function**). Since we do not know the form of `f(x)`, we try to find a hypothesis function `h(x)` that best approximates `f(x)` such that `h(x) ≈ f(x) = y`.

**Model == Hypothesis**

#### What are the different types of machine learning models/algorithms?

machine learning models can be broadly categorized into four groups
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning
4. Deep Learning

machine learning systems consist of three parts:
1. **Model** - this is what we as machine learning engineers want to build, this is the system that gives us some output
2. **Parameters** - consisting of parameters and hyperparameters; these effect the model's output
3. **Learner** - this is where the magic happens, this is where the parameters are adjusted

Which machine learning model you choose depends on the type of data that you have. There are two main types of data: **labeled** and **unlabeled**. When you have labeled data, you use supervised learning. When you have unlabeled data, you use unsupervised learning.

###### Something about labeled data

#### How does learning from experience E work?

Before getting into training, I think it is important to note how training data is fed into a machine learning model. Typically our data is arrange into matrices where each row is a single **instance** or example observations, and each column is a **feature** or variable. Therefore, you can think of a matrix as many instances arranged in rows.

###### add image for clarity

When we train a model, we are actually feeding this matrix row by row into model.

Think of your model as a hypothesis (a function) which maps input features (or independent variables) to some target feature (or dependent variable). There are two main types of relationships between the independent variables and the dependent variable: **linear** and **non-linear**.

###### something about linear and non-linear relationships

#### How can I tell if my data is linear or non-linear?

###### One method is to use train a perceptron classifier, which will converge if the data is linearly separable. In other words, if it gives 100% accuracy that means your data is linear?

#### What is the performance measure P and how is it measured?

There are many **evaluation metrics** for determining how the performance measure P but they need to be carefully selected based on the type of problem you are solving. For example, in a classification problem where we want to know where an instance is true or false, we can use the classification accuracy metric which is the simply percentage of correctly classified instances.

However, you must be careful in choosing your evaluation metric. The classification accuracy metric performs poorly in certain cases such as when the training data is skewed (e.g. 90% true, 10% false). When your training data is skewed, your model may decide to classify all instances as true since it appears most often. This would still give you a 90% classification accuracy, but would render our model useless.

Therefore in this case, another evaluation metric, a confusion matrix can be used to determine the performance of our model.

#### What is weight and bias?

Weights and biases are the parameters that your model "learn".

Weights and biases are randomachine learningy initialize before training and are adjusted during training to minimize the cost function.

#### What is a Cost Function? (a.k.a error or loss)

A cost function measures how close our predicted values are to the actual values. We want to minimize the cost function to minimize errors.

###### need to do more research on cost function

#### What is Optimization?



#### What is the process of applying machine learning?
1. Define the problem
2. Prepare data
3. Spot check algorithms
4. Improve results
5. Present results

#### Sources
1. https://machinelearningmastery.com
2. https://martechtoday.com/how-machine-learning-works-150366
3. https://docs.aws.amazon.com/machine-learning/latest/dg/training-ml-models.html
4. https://www.quora.com/How-can-I-know-if-my-problem-is-linear-or-non-linear-to-choose-the-appropriate-Machine-Learning-algorithm
5. https://www.quora.com/In-machine-learning-how-can-we-determine-whether-a-problem-is-linear-nonlinear
6. https://stats.stackexchange.com/questions/182329/how-to-know-whether-the-data-is-linearly-separable
7. https://towardsdatascience.com/machine-learning-fundamentals-via-linear-regression-41a5d11f5220
8. https://datascience.stackexchange.com/questions/19099/what-is-weight-and-bias-in-deep-learning
9. https://www.quora.com/What-is-hypothesis-in-machine-learning
