import numpy as np
from os import listdir
from os.path import isfile, join
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score
import cv2

x = []
y = []

#load all the images and convert them
files_name = [f for f in listdir('images') if isfile(join('images', f))
              and f != '.DS_Store']
for name in files_name:
    try:
        #load the image
        img = cv2.imread(join('images', name))
        #blur to remove details
        img = cv2.blur(img, (5, 5))
        # OpenCV TreshBinary
        retval, img = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
        #convert to binary
        image_as_array = np.ndarray.flatten(np.array(img))
        #add our image to the dataset
        x.append(image_as_array)
        #retrieve the direction from the filename
        y.append(name.split('_')[1].split('.')[0])
    except Exception as inst:
        print(name)
        print(inst)

#split for testing
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

#scale the data
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

clf = MLPClassifier(solver='lbfgs', alpha=100.0, random_state=1, hidden_layer_sizes=50)
clf.fit(x, y)

predicted = cross_val_predict(clf, x, y, cv2=5, verbose=2, n_jobs=8)
print('CV: ', accuracy_score(y, predicted))
