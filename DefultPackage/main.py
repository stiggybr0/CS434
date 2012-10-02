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
    if(len(sys.argv) != 1):
        print "Incorrect number of arguments."
        print "Usage: python main.py" 
        sys.exit()

if __name__ == '__main__':
    main()
    

def file_length(fi):
    with open(fi) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def p_train(num_epochs, training_data):
   
    num_examples = file_length(training_data)
    y = []
    x1 = []
    x2 = []
    w = [0] * 2
    u = []
    train_data = open(training_data, "rt")
    
    for line in train_data:
        i = 0
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
        
        i += 1     
    return w
                        
        
        
        
        
    
    
def p_classify():
    '''to-do'''















'''--------------------------------------'''


x = 0
while x == 0:
    print """
What would you like to do?
0) Exit
1) Train & Classify"""
    action = raw_input("> ")
    if action == str(1):
        print "-------------------------------------------------"
        print "What file would you like to train with?"
        training_data = raw_input("> ")
        print "How many epochs would you like to train with?"
        num_epochs = raw_input("> ")
        print "Training with " + num_epochs + " epochs of " + training_data + " then classifying."
        p_train(num_epochs, training_data)
        p_classify()
        print "-------------------------------------------------"
    elif action == str(0):
        sys.exit()
    else:
        print "Invalid input. Try again ....."