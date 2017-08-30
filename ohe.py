#!/usr/bin/env python
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Categorical data
data = np.array(["red", "blue", "green", "black"])
print(data)

# Set up a label encoder
le = LabelEncoder()

# Fit the data
transformed_cat = le.fit_transform(data)
print(transformed_cat)


# Initialize an Encoder and fit the data
enc = OneHotEncoder()
enc.fit_transform(transformed_cat.reshape(-1, 1)).toarray()

# Print the new values
print(enc.feature_indices_)
