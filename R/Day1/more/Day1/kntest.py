from sklearn.datasets import load_iris
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
iris =load_iris()


print(iris.feature_names)
print(iris.data)
print(iris.target)

X=iris.data
y=iris.target


from sklearn.neighbors import KNeighborsClassifier
knn1=KNeighborsClassifier(n_neighbors=1)

knn5=KNeighborsClassifier(n_neighbors=7)


from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


knn1.fit(X_train,y_train)

knn5.fit(X_train,y_train)


predictions1=knn1.predict(X_test)

predictions5=knn5.predict(X_test)

print(accuracy_score(y_test,predictions1))
print(confusion_matrix(y_test,predictions1))



print(accuracy_score(y_test,predictions5))
print(confusion_matrix(y_test,predictions5))

k_range =list(range(1,26))


print(range(1,26))
scores=[]

for k in range(1,26):
	knn=KNeighborsClassifier(n_neighbors=k)
	knn.fit(X_train,y_train)
	y_pred=knn.predict(X_test)
	scores.append(accuracy_score(y_test,y_pred))
	print("Accuracy Score of " + str(k) + " is  "  + str(accuracy_score(y_test,y_pred)))
	print(metrics.mean_absolute_error(y_test,y_pred))
	print(metrics.mean_squared_error(y_test,y_pred))
	print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#plt.plot(k_range,scores)
#plt.plot(range(1,20),range(1,20))
plt.plot(range(1,2),range(1,2))
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')
plt.show()

