import sys
import string
from sys import stdout
from time import sleep
import subprocess
import math


'''
Created on Sep 28, 2012

@author: James Cunningham & Andy Miller
'''

def main():
    if(len(sys.argv) != 3):
        print "Incorrect number of arguments."
        print "Usage: python main.py tn-train.txt tn-test.txt" 
        sys.exit()
    menu()
    
def p_train(num_epochs, training_data):

    w = [0] * 2
    u = []
    train_data = open(training_data, "rt")
    
    for counter in num_epochs:
        y = []
        x1 = []
        x2 = []
        for i, line in enumerate(train_data):
            a, b, c = [float(x) for x in line.split()]
            y.append(a)
            x1.append(b)
            x2.append(c)
            u.append((w[0] * x1[i]) + (w[1] * x2[i]))
            if(y[i]*u[i] <= 0):
                temp_x1 = y[i] * x1[i]
                temp_x2 = y[i] * x2[i]
                w[0] = w[0] + temp_x1
                w[1] = w[1] + temp_x2  
        return w
                        
def p_classify(x, w):
    if(len(w) != 2):
        print "cannot classify x with this weight vector: wrong size"
        sys.exit()
    elif(len(x) != 2):
        print "cannot classify with this test example vector: wrong size"
        sys.exit()
    if(((w[0] * x[0]) + (w[1] *x[1])) > 0):
        return 1
    else:
        return -1


def run_classify(w, testing_data):
    test_data = open(testing_data, "rt")
    y_data = []
    y_classified = []
    x1 = []
    x2 = []
    for i, line in enumerate(test_data):
        a, b, c = [float(x) for x in line.split()]
        y_data.append(a)
        x1.append(b)
        x2.append(c)   
        x = [x1[i], x2[i]]
        y_classified.append(p_classify(x,w))
    print "here is how we classified the test data: "
    print y_classified


def menu():
    training_data = sys.argv[1]
    testing_data = sys.argv[2]
    count = 0
    while count == 0:
        print """
What would you like to do?
0) Exit
1) Train & Classify"""
        action = raw_input("> ")
        if action == str(1):
            print "-------------------------------------------------"
            print "How many epochs would you like to train with?"
            num_epochs = raw_input("> ")
            print "-------------------------------------------------"
            print "Training with " + num_epochs + " epochs of " + training_data + " then classifying data in " + testing_data
            w = p_train(num_epochs, training_data)
            run_classify(w,testing_data)
            print "-------------------------------------------------"
        elif action == str(0):
            sys.exit()
        else:
            print "Invalid input. Try again ....."
            
            
if __name__ == '__main__':
    main()