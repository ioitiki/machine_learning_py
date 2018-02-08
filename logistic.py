from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

print iris.keys()
print iris.target_names
print iris.feature_names
print iris.data[:3]
print iris.target[:3]
print iris.data.shape
print iris.target.shape
