import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.Sequential([ # this function calls for the creation of the model object and sequences the developed layers inside the input/output layers. 
    keras.layers.Dense(units=1, input_shape=(1,)) # this generates the linear function layer for the linear regression (y = mx + [mn * xn ...] + b). Every input passes through this layer and an output is generated.
])

model.compile( # compiles the model with the Stochastic Gradient Descent and uses MSE as loss type.
    optimizer = "sgd",
    loss = "mean_squared_error"
)

x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9]) # simple database

model.fit(x, y, epochs=100, verbose=0) # here, internally keras does guess w and b -> calculate error -> adjust w and b -> repeat 100 times (gradient descent)
model.save("my_model.keras") # saving the model locally

model = keras.models.load_model("my_model.keras") # loading the saved model
print(model.predict(np.array([5]))) # making a prediction