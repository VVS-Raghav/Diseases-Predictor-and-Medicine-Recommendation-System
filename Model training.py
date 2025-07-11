import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("Training.csv")

X = df.drop(columns=["prognosis"])
y = df["prognosis"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

joblib.dump(le, "label_encoder.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

model = RandomForestClassifier(
    n_estimators=200, max_depth=15, random_state=42, class_weight="balanced"
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

joblib.dump(model, "disease_model.pkl")

with open("symptoms_list.txt", "w") as f:
    for col in X.columns:
        f.write(col + "\n")

print("\nModel and encoders saved successfully.")