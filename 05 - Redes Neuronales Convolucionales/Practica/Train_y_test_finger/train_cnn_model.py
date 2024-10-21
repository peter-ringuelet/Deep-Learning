import numpy as np

import tensorflow as tf
from skimage import io
 
import glob

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Dropout, Flatten

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

IMG_SIZE = (64, 64)

def import_data(img_list):
    #train_img_data = []
    img_data = []
    #train_label_data = []
    label_data = []
    
    # for img in train_img_list:
    #     img_read = Image.open(img)
    #     #img_read = transform.resize(img_read, IMG_SIZE, mode = 'constant')
    #     train_img_data.append(img_read)
    #     train_label_data.append(img[-5])

    for img in img_list:
        #img_read = Image.open(img)
        img_read = io.imread(img)
        img_read = img_read/img_read.max()
        #img_read = transform.resize(img_read, IMG_SIZE, mode = 'constant')
        img_data.append(img_read)
        label_data.append(img[-6])
        
    #return np.array(train_img_data), np.array(test_img_data), np.array(train_label_data), np.array(test_label_data)
    return np.array(img_data), np.array(label_data)


def build_model():
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (*IMG_SIZE, 1), activation = 'relu'))
    model.add(MaxPool2D((2,2)))   
    
    model.add(Conv2D(64, (3,3), activation = 'relu'))
    model.add(MaxPool2D((2,2)))
    
    model.add(Conv2D(128, (3,3), activation = 'relu'))
    model.add(MaxPool2D((2,2))) 
    
    model.add(Flatten())
    
    model.add(Dropout(0.40))
    model.add(Dense(128, activation = 'relu'))
    model.add(Dropout(0.40))
    model.add(Dense(6, activation = 'softmax'))
    
    model.summary()
    
    return model


EPOCAS = 10
LOTES  = 128

train_img_list = glob.glob("resized/train/*.png")
test_img_list = glob.glob("resized/test/*.png")

print(len(train_img_list), len(test_img_list), sep = '\n')

xtrain, ytrain = import_data(train_img_list)

xtrain = xtrain.reshape(xtrain.shape[0], *IMG_SIZE, 1)

ytrain = tf.keras.utils.to_categorical(ytrain, num_classes = 6)

print(xtrain.shape, ytrain.shape)

x_train, x_test, y_train, y_test = train_test_split(xtrain, ytrain, test_size = 0.20, random_state = 7, shuffle = True)

model = build_model()

model.compile('SGD', loss = 'categorical_crossentropy', metrics = ['accuracy'])
H = model.fit(x = x_train, y = y_train, batch_size = LOTES, epochs = EPOCAS, validation_data = (x_test, y_test))

# plot the training loss and accuracy
N = np.arange(0, 10)
plt.figure()
#plt.plot(N, H.history["loss"], label="train_loss")
#plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, 100*H.history["accuracy"], label="train_acc")
plt.plot(N, 100*H.history["val_accuracy"], label="val_acc")
plt.title("Efectividad de Entrenamiento")
plt.xlabel("Época #")
plt.ylabel("Efectividad")
plt.legend(loc="lower right")



pred = model.evaluate(x_test, y_test, batch_size = LOTES)

print("Efectividad del modelo con datos de prueba: %6.2f%%" % (pred[1]*100))



