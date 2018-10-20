# Decision Tree:

- they can perform both classification and regression (just like SVM).
- they can even perform multioutput tasks.
- they are powerful algorithms, that can fit complex datasets.
- fundamental components of random forest.

**Good Points:**
- they require very little data preparation.
- they don't require feature scaling or centering at all.


## How does Decision tree make prediction?

**Eg:** Iris dataset
- start at root node (depth 0, at the top): Ask question? whether the flower's petal length smaller than 2.45 cm.
- If it is then you move down to the root's left child node (depth 1, left). In this case, it is leaf node (i.e. it doesn't have any children nodes), so it doesn't ask any question?
- You could simply predcited class for that node and the Decision tree predictics that your flower is an Iris - Setosa.
- Suppose, you want to find another flower, whose petal length is greater than 2.45cm. You must move down to the right child node (depth 1, right), which is not a leaf node, so it ask another questions: is petal width smaller than 1.75cm?
- If it is, then your flower is most likely an Iris-Versicolor (depth 2, left). 
- If not, it is liekly an Iris-Virginca (depth2, right).

#### Types of nodes:
- Root Node: starting point, depth = 0
- Leaf Node: node which doesn't have any nodes further or connections
- Child Node: connected to other nodes and might have leaf nodes going down.

#### Attributes of a Node:
1. **Samples:** how many training instances it applies to.?
2. **Value:** tells how many training instances of each class this node applies to.
3. **Gini:** measures it's impurity: a node is pure (gini= 0)if all training instances it applies to belong to the same class.

## The CART Training Algorithm:
- Algorithm first split the datasets into two subsets using a single feature k and a threshold tk (eg: petal length).
- How does it search for k and tk?
  - It searches for the pair (k,tk) that produces the purest subsets (weighted by their size).
- CART cost function:
- Once it has successfully split the training set in two, it splits the subsets using the same logic,
- then the subsets,
- and so on, recursively.
- It stop recursing once it reaches the maximum depth (defined by max_depth hyperparameter), or if it cannot find a split that will reduce impurity.

- CART is greedy algo.
- It greedily search for an optimum split at the top level, then repeats the process at each level.
- It does not check whether or not the split will lead to the lowest possible impurity several levels down.
- A greedy algorithm often produces a reasonably good solution, but it is not guranteed to be the optimal solution.
- Unfortunately, finding the optimal tree is known to be NP-Complete problem: it require O(exp(m)) time, making it intractable even for a small training set. This is why we settle for a reasonably good solution.


## Hyperparameter:
- max_depth:
- min_samples_splits:
- min_samples_leaf:
- min_weigth_fraction_leaf:
- max_leaf_nodes:

## Computational Complexitiy:
- Decision trees are generally approximately balanced, so transversing the DT requires going through roughly O(log2(m)) nodes.
- Since, each node only requires checking the value of one feature, the overall prediction complexitiy is O(log2(m)), independent of the numbers of features.
- So, predictions are very fast, even when dealing with large datasets.

- However, the training algo. compares all features on all samples at each node. this results in a training complexity of O(n * m * log(m)).
- This slow down the training process.





















