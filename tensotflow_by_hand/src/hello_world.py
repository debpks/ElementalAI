import tensorflow as tf

# Design a Neural Network
model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,),name='input_layer'),
    tf.keras.layers.Dense(units=1,name='output_layer')
])

# Compile the model
print('Compiling the model')
model.compile(optimizer='adam',loss='mse')
print('Model Summary')
model.summary()

x = [1,2,3,4,5,6,7,8,9,10]
y = [2*x+1 for x in x]
print('Y',y)

print(tf.config.list_physical_devices('GPU'))
with tf.device('/GPU:0'):
    model.fit(x,y,epochs=5000)
print(model.predict([11]))
print(2*11+1)
