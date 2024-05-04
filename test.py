import pandas as pd
df = pd.read_csv('attribute.csv')
from sklearn.tree import DecisionTreeClassifier
X = df.drop(['name'], axis=1)
y = df['name']

clf = DecisionTreeClassifier()

clf.fit(X, y)

print("Think of a character or person and answer the following questions (yes/no):")
current_data = {}
for feature in X.columns:
    answer = input(f"Is the character/person {feature}? ").lower()
    current_data[feature] = True if answer == 'yes' else False


current_X = pd.DataFrame([current_data])
prediction = clf.predict(current_X)

if len(prediction) == 1:
    print(f"Is it {prediction[0]}?")