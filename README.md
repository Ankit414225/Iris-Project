# Iris-Project
This project performs multi-class classification on the Iris dataset using Logistic Regression and a Multi-Layer Perceptron (MLP).

## Dataset_description:
Iris Dataset contains 150 samples of flower from three different species.
It contains 4 morphological features that includes:
  1. Sepal length
  2. Sepal width
  3. Petal length
  4. Petal width
## Preprocessing:
1. Train test split(80-20)
2. Feature scaling using Standard Scalar
3. No data leakage(As scalar fit only on training data)
## Model used:
1. Logistic Regression(Baseline)
2. Non linear Model(Pipeline)
## Evaluation
Models were evaluated using:
1. Accuracy
2. Precision
3. Recall
4. F1-score
5. Confusion Matrix

## Result
The MLP achieved 100% test accuracy and reduced confusion between Versicolor and Virginica compared to Logistic Regression.

## Conclusion
Non-linear models such as MLP can better capture complex decision boundaries in structured tabular data.
