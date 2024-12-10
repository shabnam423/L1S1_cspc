#2.a
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

X = data[:, :2] 
y = data[:, 2]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_train = knn.predict(X_train)
y_pred_test = knn.predict(X_test)

#2b
print("Confusion Matrix - Train:")
print(confusion_matrix(y_train, y_pred_train))

print("Confusion Matrix - Test:")
print(confusion_matrix(y_test, y_pred_test))

#2c
print("Training Accuracy:", accuracy_score(y_train, y_pred_train))
print("Testing Accuracy:", accuracy_score(y_test, y_pred_test))

#2d
for n in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(X_train, y_train)
    print(f"n_neighbors={n}, Train Accuracy={accuracy_score(y_train, knn.predict(X_train))}, Test Accuracy={accuracy_score(y_test, knn.predict(X_test))}")