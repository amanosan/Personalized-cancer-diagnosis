import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


def plot_conf_mat(y_test, y_pred, labels):
    """
    Function to plot the Confusion Matrix, Precision and Recall Matrices.
    Parameters:
        - y_test : The actual dependent variable.
        - y_pred : The predicted values of dependent variable.
        - labels : (list, tuple, set) of all the unique values of dependent variable.
    """

    C = confusion_matrix(y_true=y_test, y_pred=y_pred)

    # getting the recall matrix:
    # divide each element in the cell by the sum of elements in its column
    # true positives / true positives + false negatives
    A = ((C.T) / C.sum(axis=1)).T

    # getting the precision matrix:
    # divide each element in the cell by the sum of elements in its row
    # true positives / true positives + false positives
    B = (C / C.sum(axis=0))

    print("CONFUSION MATRIX")
    plt.figure(figsize=(15, 7))
    sns.heatmap(C, annot=True, cmap='viridis', fmt=".3f")
    plt.title(label='Confusion Matrix')
    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")
    plt.xticks(labels)
    plt.yticks(labels)
    plt.show()

    print('-' * 120)
    print("PRECISION MATRIX")
    plt.figure(figsize=(15, 7))
    sns.heatmap(B, cmap='viridis', annot=True, fmt='.3f')
    plt.title("Precision Matrix")
    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")
    plt.xticks(labels)
    plt.yticks(labels)
    plt.show()

    print('-' * 120)
    print("RECALL MATRIX")
    plt.figure(figsize=(15, 7))
    sns.heatmap(A, annot=True, cmap='viridis', fmt='.3f')
    plt.title('Recall Matrix')
    plt.xlabel('Predicted Class')
    plt.ylabel('Actual Class')
    plt.xticks(labels)
    plt.yticks(labels)
    plt.show()
