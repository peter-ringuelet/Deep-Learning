import numpy as np
import glob
from skimage import io, transform
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
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

def vshift_images(images, shift=0.1):
    d = int(IMG_SIZE[0]*shift)
    for i in range(0,len(images)):
        img = images[i].copy()
        e = np.empty_like(img)
        if d >= 0:
            e[:d] = img[0,0]
            e[d:] = img[:-d]
        else:
            e[d:] = img[0,0]
            e[:d] = img[-d:]
        images[i] = e
    return images

def hshift_images(images, shift=0.1):
    d = int(IMG_SIZE[0]*shift)
    for i in range(0,len(images)):
        img = images[i].copy()
        e = np.roll(img, d, axis=1)

        if d >= 0:
            pass
        else:
            pass
        images[i] = e
    return images

def rotate_images(images, angle):

    for i in range(0,len(images)):
        img = images[i].copy()
        img = transform.rotate(img, angle)
        images[i] = img
    return images
    


# obtiene la arquitectura para el modelo y lo compila
model = load_model("fingers_count_model.h5")

# lista de archivos a procesar
train_img_list = glob.glob("data/test/*.png")

# carga las imagenes a partir de los nombres de archivos
x_test, y_test = import_data(train_img_list)

# conviertes el id de la clase en "one hot encoding": 3 => [0,0,0,1,0,0]
y_test = to_categorical(y_test, num_classes = 6)


plt.close("all")

print("\nEfectividad del modelo con datos de prueba:")
# evalua el modelo con los datos de validacion

pred = model.evaluate(x_test, y_test, verbose = False)
print(" - sin desplazamiento alguno............: %6.2f%%" % (pred[1]*100))
plt.figure()
plt.imshow(x_test[0], cmap="gray")

shift = -0.2
x_shift = vshift_images(x_test, shift)
pred = model.evaluate(x_shift, y_test, verbose = False)
print(" - Desplazado verticalmente   %6.1f%%...: %6.2f%%" % (100*shift, pred[1]*100))
plt.figure()
plt.imshow(x_shift[0], cmap="gray")

shift = 0.2
x_shift = vshift_images(x_test, shift)
pred = model.evaluate(x_shift, y_test, verbose = False)
print(" - Desplazado verticalmente   %6.1f%%...: %6.2f%%" % (100*shift, pred[1]*100))
plt.figure()
plt.imshow(x_shift[0], cmap="gray")

shift = 0.2
x_shift = hshift_images(x_test, shift)
pred = model.evaluate(x_shift, y_test, verbose = False)
print(" - Desplazado horizontalmente %6.1f%%...: %6.2f%%" % (100*shift, pred[1]*100))
plt.figure()
plt.imshow(x_shift[0], cmap="gray")

shift = -0.2
x_shift = hshift_images(x_test, shift)
pred = model.evaluate(x_shift, y_test, verbose = False)
print(" - Desplazado horizontalmente %6.1f%%...: %6.2f%%" % (100*shift, pred[1]*100))
plt.figure()
plt.imshow(x_shift[0], cmap="gray")

angle = 15 # grados
x_rot = rotate_images(x_test, angle)
pred = model.evaluate(x_rot, y_test, verbose = False)
print(" - Rotado en grados %6.1f%%.............: %6.2f%%" % (angle, pred[1]*100))
plt.figure()
plt.imshow(x_rot[0], cmap="gray")


