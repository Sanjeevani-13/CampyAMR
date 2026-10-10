import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


train_data = pd.read_csv("train_features.csv")
val_data = pd.read_csv("val_features.csv")


X_train = train_data.drop(columns=["Genome ID", "Label"])
y_train = train_data["Label"]

X_val = val_data.drop(columns=["Genome ID", "Label"])
y_val = val_data["Label"]


model = RandomForestClassifier()
model.fit(X_train, y_train)


preds = model.predict(X_val)


print("Accuracy:", accuracy_score(y_val, preds))
print("\nClassification Report:\n", classification_report(y_val, preds))


cm = confusion_matrix(y_val, preds)

print("Confusion Matrix:\n", cm)

sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# ==============================
# TEST DATA EVALUATION
# ==============================
test_data = pd.read_csv("test_features.csv")

X_test = test_data.drop(columns=["Genome ID", "Label"])
y_test = test_data["Label"]

test_preds = model.predict(X_test)


print(f"\nTest Accuracy: {accuracy_score(y_test, test_preds)*100:.2f}%")
print("\nTest Classification Report:\n", classification_report(y_test, test_preds))
print("\nTest Confusion Matrix:\n", confusion_matrix(y_test, test_preds))


# ==============================
# FEATURE IMPORTANCE
# ==============================
importances = model.feature_importances_
feature_names = X_train.columns

feat_df = pd.DataFrame({
    "kmer": feature_names,
    "Importance": importances
})

# Sort by importance
feat_df = feat_df.sort_values(by="Importance", ascending=False)

# Top 20 important k-mers
top_kmers = feat_df.head(20)

print("\nTop 20 Important k-mers:\n")
print(top_kmers)

# Plot
plt.figure()
plt.barh(top_kmers["kmer"], top_kmers["Importance"])
plt.xlabel("Importance Score")
plt.title("Top 20 Important k-mers")
plt.gca().invert_yaxis()
plt.show()

# ==============================
# HOTSPOT APPROXIMATION
# ==============================

# Select top 10 strongest k-mers
hotspot_kmers = top_kmers.head(10)

print("\nPotential Mutation Hotspots (kmers):\n")
print(hotspot_kmers["kmer"].tolist())