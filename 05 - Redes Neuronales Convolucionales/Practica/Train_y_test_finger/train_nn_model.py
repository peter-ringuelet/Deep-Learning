import numpy as np


import glob
from skimage import io

from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

IMG_SIZE = (64, 64)

def import_data(img_list):
    img_data = []
    label_data = []
    
    img_count = len(img_list)
    for i in range(0,img_count):
        img = img_list[i]
        img_read = io.imread(img)
        img_read = img_read/img_read.max() # normaliza pixeles entre 0 y 1
        img_data.append(img_read)          # agrega a lista de imágenes a procesar
        label_data.append(img[-6])         # extrae cant. dedos del nombre del archivo
        # muestra progreso en la carga
        if i % 100 == 0:
            print("\rCargando imágenes: %6.2f%%" % (100*i/img_count), end="")
    print("\rCargando imágenes: 100.00%%\n")
        
    return np.array(img_data), np.array(label_data)


def build_model():
    model = Sequential()

    model.add(Input(shape=IMG_SIZE))
    model.add(Flatten())
    model.add(Dense(256, activation = 'tanh'))
    #model.add(Dense(32, activation = 'tanh'))
    model.add(Dropout(0.30))
    model.add(Dense(6, activation = 'softmax'))

    model.summary()
    return model


EPOCAS = 15
LOTES  = 128

# lista de archivos a procesar
train_img_list = glob.glob("data/train/*.png")

# carga las imagenes a partir de los nombres de archivos
xtrain, ytrain = import_data(train_img_list)

# conviertes el id de la clase en "one hot encoding": 3 => [0,0,0,1,0,0]
ytrain = to_categorical(ytrain, num_classes = 6)

# separa los datos y clase en grupo de entrenamiento y validacion
x_train, x_val, y_train, y_val = train_test_split(xtrain, ytrain, test_size = 0.20, random_state = 7, shuffle = True)

# obtiene la arquitectura para el modelo y lo compila
model = build_model()
model.compile('SGD', loss = 'categorical_crossentropy', metrics = ['accuracy'])


# entrena el modelo y guarda la historira del progreso    
H = model.fit(x = x_train, y = y_train, batch_size = LOTES, epochs = EPOCAS, validation_data = (x_val, y_val))

# dibuja accuracy del progreso del entrenamiento
N = np.arange(0, EPOCAS)
accuracy = np.array(H.history["accuracy"])
val_accuracy = np.array(H.history["val_accuracy"])

plt.figure()
#plt.plot(N, H.history["loss"], label="train_loss")
#plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, 100*accuracy, label="train_acc")
plt.plot(N, 100*val_accuracy, label="val_acc")
plt.title("Efectividad de Entrenamiento")
plt.xlabel("Época #")
plt.ylabel("Efectividad")
plt.legend(loc="lower right")


# evalua el modelo con los datos de validacion
pred = model.evaluate(x_val, y_val, batch_size = LOTES)

print("\nEfectividad del modelo con datos de validación: %6.2f%%" % (pred[1]*100))



