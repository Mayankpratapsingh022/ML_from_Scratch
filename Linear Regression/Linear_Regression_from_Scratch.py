# importing numpy
import numpy as np


class Linear_Regression():

  # initiating the parameters (learning rate and no of iterations )

  def __init__(self,learning_rate,no_of_iterations):

    self.learning_rate = learning_rate
    self.no_of_iterations = no_of_iterations







  def fit(self,X,Y):
    # number of training examples and number of features
    self.m , self.n  = X.shape # number of rows (m) & columns (n)

    # Initiating the weight and bias

    self.w = np.zeros(self.n) # createad an array of zeros with n elements
    self.b = 0
    self.X = X
    self.Y = Y

    # Implementing Gradient Descent

    for i in range(self.no_of_iterations):
      self.update_weights()






  def update_weights(self,):
    Y_prediction = self.predict(self.X)

    #calculate gradients
    dw = -(2 * (self.X.T).dot(self.Y - Y_prediction)) // self.m


    db = -2*np.sum(self.Y - Y_prediction)/self.m



    # updating the weights

    self.w = self.w - self.learning_rate*dw
    self.b = self.b - self.learning_rate*db







  def predict(self,X):
    return X.dot(self.w) + self.b # here w is a numpy array that's why dot product




