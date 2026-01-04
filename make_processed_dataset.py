import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
iris = load_iris()
X = iris.data        # features
y = iris.target      # labels
feature_names = iris.feature_names
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
processed_df = pd.DataFrame(X_scaled, columns=feature_names)
processed_df["species"] = y
processed_df.to_csv("processed_iris_dataset.csv", index=False)
