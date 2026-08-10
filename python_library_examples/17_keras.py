from keras import Sequential
from keras.layers import Dense

model = Sequential([
    Dense(8, activation="relu", input_shape=(4,)),
    Dense(1, activation="sigmoid")
])

model.summary()
