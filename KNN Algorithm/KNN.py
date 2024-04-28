from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

all_documents = businessGraphsList + foodGraphsList + healthGraphsList
labels=[]
X_train, X_test, y_train, y_test = train_test_split(all_documents, labels, test_size=0.2, random_state=42)

# Initialize KNN classifier

knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
knn_classifier.fit(X_train, y_train)

# Predict on the test set
predictions = knn_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)