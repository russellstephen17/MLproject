# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:22:14 2020

@author: srussel1
"""

import pandas as pd
from skimage import io
import os
import glob
import numpy as np
from skimage import color, exposure, transform
import shutil
"C:/Users/srussel1/Documents/AI_Course/MachineLearning/IndividualAssignment/gtsrbGermanTrafficSign/Test.csv"
test_csv = 'C:/Users/srussel1/Documents/AI_Course/MachineLearning/IndividualAssignment/gtsrbGermanTrafficSign/Test.csv'
test = pd.read_csv('C:/Users/srussel1/Documents/AI_Course/MachineLearning/IndividualAssignment/gtsrbGermanTrafficSign/Test.csv', sep=',', decimal='.')
path = 'gdrive/My Drive/ML project/TrafficSigns'
# Load test dataset
X_test = []
y_test = []
i = 0
for file_name, class_id in zip(list(test['Path']), list(test['ClassId'])):
    #img_path = os.path.join('GTSRB/Final_Test/Images/', file_name)
    img_path = os.path.join('C:/Users/srussel1/Documents/AI_Course/MachineLearning/IndividualAssignment/gtsrbGermanTrafficSign/', file_name)
    new_path1 = os.path.join('C:/Users/srussel1/Documents/AI_Course/MachineLearning/IndividualAssignment/gtsrbGermanTrafficSign/NewTest/', str(class_id)+'/')
    new_path2 = os.path.join(new_path1 , file_name)
    shutil.copy2(img_path, new_path2) 
    #X_test.append(preprocess_img(io.imread(img_path)))
    #img= io.imread(img_path) #preprocess_img(io.imread(img_path))
    #img = transform.resize(img, (IMG_SIZE, IMG_SIZE))
    #X_test.append(img)
   # y_test.append(class_id)
print(new_path1)
#X_test = np.array(X_test)
#y_test = np.array(y_test)