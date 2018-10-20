# Ensemble Learning
 
### Why ensemble learning? Why does it work?
Suppose you ask a complex question to thousands of people, then generate their answer. In many cases you will find that this aggregated answer is better than an expert's answer. This is called the **wisdom of the crowd**.

Similarly, if you aggregate the predictions of a group of predictiors (classifer/ regressors), you will often get better predictions than with the best indiviual predictor. 

A group of predictior is called an **ensemble**; thus this technique is called **ensemble learning**, and an Ensemble Learning algorithm is called an **Ensemble Method**.

For eg: Random forest, is an ensemble of decision trees. Most popular Ensemble methods are bagging, boosting, stacking.

## Hard Voting Classifier (Why does ensemble methods with many weak classifier often achieves high accuracy then the best classifier in the ensemble)?

Hard Voting Classifier: A simple way to crete better classifier is to aggregate the predictions of many classifiers and predict the class that gets the most votes. This majority-vote classifier is called a hard voting classifier.

And, surprisingly, this voting classifier often achieves a higher accuracy then the best classifier in the ensemble. In fact, even if each classifier is a *weak learner* (meaning it does only slightly better than random guessing), the ensemble cas still be a *strong learner* (achieving high accuracy), provided there are sufficient number of waek learners and they are sufficiently diverse.

#### How is this possible? [Clue: Law of large numbers]
**Analogy**
- You have a biased coin that has 51% chance of getting head and 49% chance of getting tail.
- You toss it 1,000 times, you will generally get 510 heads and 490 tails (majority heads)
- If you do math, you will find out that prob. of getting majority of head after 1,000 tosses is euqall to 75% (approx).
- The more you toss, higher the prob. of getting majority of head. 
- In fact, after 10,000 tosees, this goes till 97%.
- This is due to *law of large numbers*: as you keep tossing the coin, the ratio of heads getss closer and closer to the prob. of heads (51%).

**Similarly**
- Suppose you build a ensemble containing 1,000 classifiers that are individually correct only 51% of the time (barely better than random guessing).
- If you predict the majority voted class, you can hope for up to 75% accuracy!
- However, this is only true if all classifiers are perfectly independent, making uncorrelated erros, whcih is clearly not the case since they are trained on the same data. so, they are liekly to make kind of erros.
- So, there will be many majority votes for the wrong class, reducing the ensemble's accuracy.

## Assumptions for Ensemble Learning:
- Many weak learners -- sufficeiently large numbers
- sufficiently diverse.
- All classifiers should be independent, making uncorrelated errors.

