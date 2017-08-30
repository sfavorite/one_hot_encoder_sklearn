from sklearn.preprocessing import LabelEncoder

# Categorical data
data = ["red", "blue", "green", "black"]

# Set up a label encoder
le = LabelEncoder()

# Fit the data
le.fit(data)

print(le.classes_)

transformed_cat = le.transform(data)
print(transformed_cat)

le.inverse_transform(transformed_cat)
