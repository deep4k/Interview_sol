# Name: Deepak Buddha

import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.pipeline import Pipeline

def build_model(nodes, X, Y, epoch_num, batch_num):
    model = Sequential()
    # normal weights used with zero to 0.05 sd guassian random values
    model.add(Dense(nodes, input_dim=X.shape[1], activation='relu', use_bias=True))
    model.add(Dense(nodes, activation='relu', use_bias=True))
    model.add(Dense(1, activation='linear'))
    model.summary()
	# Compile model
    #  Adaptive Moment Estimation (Adam) that  uses adaptive learning rates
    model.compile(loss='mse', optimizer='adam', metrics=['mse', 'mae'])
    history = model.fit(X, Y, epochs=epoch_num, batch_size=batch_num, verbose=1, validation_split = 0.1)
    
    #Plotting loss function
    #print(history.history.keys())
    # "Loss"
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()
    
    return model
    
def make_prediction(model, X):
    Y = model.predict(X)
    pd.DataFrame(Y, columns=['y']).to_csv('test_predicted.txt', index=False)
   
def main():
    # load dataset
    n = 4 # num nodes
    X_train= pd.read_csv("train_data.txt", delim_whitespace=True)
    Y_train = pd.read_csv("train_truth.txt", delim_whitespace=True)
    X_test = pd.read_csv("test_data.txt", delim_whitespace=True)

    #print(X_train)  
    epoch_num = int(X_train.shape[0] / (n*n))
    batch_num = int(epoch_num/n)
    model = build_model(n, X_train, Y_train, epoch_num, batch_num)
    make_prediction(model, X_test)

main()
    




