import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report


# Load the images and labels
X = []
y = []
for label in ['car', 'truck']:
    for file in os.listdir('data'):
        img = cv2.imread('data/')
        X.append(img)
        y.append(label)
X = np.array(X)
y = np.array(y)

# Preprocess the images
X = X / 255.0

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Extract features from the images using a pre-trained CNN
# (You can use any other method to extract features)
X_train = extract_features(X_train)
X_test = extract_features(X_test)

# Train a support vector machine classifier
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))