from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
from tensorflow.keras.callbacks import TensorBoard,ModelCheckpoint
import pickle
import tensorflow as tf
import time
import os
from keras.datasets import cifar10
(train_features, train_labels), (test_features, test_labels) = cifar10.load_data()

print(train_features.shape)

train_features= train_features/255.0


dense_layers = [3]
layer_d_sizes = [64]
conv_layers = [3]
layer_c_sizes = [32, 24]
conv_sizes = [7, 5, 1]
#drop_outs = [0.2, 0.5, 0.7]
zzz=0
for dense_layer in dense_layers:
    for layer_d_size in layer_d_sizes:
        for conv_layer in conv_layers:
          for layer_c_size in layer_c_sizes:
            for conv_size in conv_sizes:

              NAME = "conv_size-{}-adam-{}-conv-with-{}-nodes-and-{}-dense-with-{}-nodes-{}".format(conv_size,conv_layer, layer_c_size, dense_layer, layer_d_size, int(time.time()))
              print(NAME)
              # zzz=zzz+1
              # if(zzz<11):
              #   continue

              model = Sequential()
              layer_c_sizes

              model.add(Conv2D(layer_c_size, (3, 3), input_shape=train_features.shape[1:]))
              model.add(Activation('relu'))
              #model.add(Dropout(drop_out))
              model.add(Conv2D(layer_c_size, (3, 3)))
              model.add(Activation('relu'))
              model.add(MaxPooling2D(pool_size=(2, 2)))

              for l in range(conv_layer-1):
                  model.add(Conv2D(layer_c_size, (3, 3)))
                  model.add(Activation('relu'))
                  #model.add(Conv2D(layer_c_size, (3, 3)))
                  #model.add(Activation('relu'))
                  model.add(MaxPooling2D(pool_size=(2, 2)))

              #model.add(Dropout(drop_out))
              model.add(Flatten())

              for _ in range(dense_layer):
                  model.add(Dense(layer_d_size))
                  model.add(Activation('relu'))

              model.add(Dense(10))
              model.add(Activation('softmax'))

              tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

              checkpoint_path = "checkpoints/weights-{epoch:02d}-{val_loss:.2f}.hdf5"
              #filepath_c = os.path.dirname(checkpoint_path)
              cp_callback = ModelCheckpoint(checkpoint_path, monitor='val_loss', verbose=1, save_best_only=False, save_weights_only=False, mode='auto', period=5)


              model.compile(loss='sparse_categorical_crossentropy',
                            optimizer='adam',
                            metrics=['accuracy'],
                            )


              model.fit(train_features, train_labels,
                        batch_size=200,
                        epochs=20,
                        validation_split=0.2,
                        callbacks=[tensorboard,cp_callback])
              model.save(NAME)