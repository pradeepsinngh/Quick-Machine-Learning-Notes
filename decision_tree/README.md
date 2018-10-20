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

