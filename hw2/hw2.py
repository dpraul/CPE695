from tensorflow.contrib import learn
from sklearn import datasets, metrics


def train(hidden_units=(10, 20, 10)):
    iris = datasets.load_iris()
    classifier = learn.TensorFlowDNNClassifier(hidden_units=hidden_units, n_classes=3)
    classifier.fit(iris.data, iris.target)
    score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
    print("Hidden units: %s, Accuracy: %f" % (hidden_units, score))


def main():
    start = 10
    stop = 30
    step = 10

    stop += 1  # so python still checks the last value
    for i in xrange(start, stop, step):
        for j in xrange(start, stop, step):
            for k in xrange(start, stop, step):
                train(hidden_units=(i, j, k))
                print('')


if __name__ == '__main__':
    main()
