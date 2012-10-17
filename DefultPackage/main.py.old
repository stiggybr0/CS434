import sys
import random


'''
Created on Sep 28, 2012

@author: James Cunningham & Andy Miller
'''


'''
Function: main
Purpose: Check usage and execute menu()
Input: N/A
Output: N/A
'''

def main():
    if(len(sys.argv) != 3):
        print "Incorrect number of arguments."
        print "Usage: python main.py tn-train.txt tn-test.txt" 
        sys.exit()
    menu()
    
    
'''
Function: p_train
Purpose: static training algorithm
Input: number of epochs to train with and pointer to training file.
Output: trained weight vector
'''
    
def p_train(num_epochs, training_data):
    w = [0] * 2                                             #weight vector
    wold = [-1] * 2                                         #vector for keeping track of changed weights
    counter = 0
    train_data = open(training_data, "rt")
    
    while (counter < num_epochs and wold[0] != w[0] and wold[1] != w[1]):
        y = []                                              #vector for keeping track of class labels
        x1 = []                                             #column 1
        x2 = []                                             #column 2            
        u = []                                              
        wold[0] = w[0]
        wold[1] = w[1]
        for i, line in enumerate(train_data):               #perceptron algorithm
            a, b, c = [float(x) for x in line.split()]      #split the data from file to separate lists
            y.append(a)
            x1.append(b)
            x2.append(c)
            u.append((w[0] * x1[i]) + (w[1] * x2[i]))
            if(y[i]*u[i] <= 0):
                temp_x1 = y[i] * x1[i]
                temp_x2 = y[i] * x2[i]
                w[0] = w[0] + temp_x1
                w[1] = w[1] + temp_x2  
        counter = counter + 1
    return w


'''
Function: p_train_random
Purpose: random training algorithm
Input: number of epochs to train with and pointer to training file.
Output: trained weight vector
'''

def p_train_random(num_epochs, training_data):

    w = [0] * 2
    wold = [-1] * 2
    counter = 0
    train_data = open(training_data, "rt")
    
    while (counter < num_epochs and wold[0] != w[0] and wold[1] != w[1]):
        y = []                                              #class labels list
        x1 = []                                             #column 1
        x2 = []                                             #column 2
        u = []
        wold[0] = w[0]
        wold[1] = w[1]
        ranlist = []
        for count, fline in enumerate(train_data):
            ranlist.append(fline)
        i=0
        random.shuffle(ranlist)                             #shuffle the data each epoch
        for line in ranlist:                                #perceptron algorithm
            a, b, c = [float(x) for x in line.split()]      #split the data from file to separate lists
            y.append(a)
            x1.append(b)
            x2.append(c)
            u.append((w[0] * x1[i]) + (w[1] * x2[i]))
            if(y[i]*u[i] <= 0):
                temp_x1 = y[i] * x1[i]
                temp_x2 = y[i] * x2[i]
                w[0] = w[0] + temp_x1
                w[1] = w[1] + temp_x2  
            i = i + 1
        counter = counter + 1
    return w
       
       
'''
Function: p_classify
Purpose: classifies a test example given a weight vector      
Input: One example, one weight vector
Output: 1 or -1 classification
'''
                 
def p_classify(x, w):
    if(len(w) != 2):                                        #error checks
        print "cannot classify x with this weight vector: wrong size"
        sys.exit()
    elif(len(x) != 2):
        print "cannot classify with this test example vector: wrong size"
        sys.exit()
    if(((w[0] * x[0]) + (w[1] *x[1])) > 0):                 #determine what side of the boundary
        return 1
    else:
        return -1


'''
Function: run_classify
Purpose: helper function to execute the classify function and keep track of accuracy
Input: weight vector, pointer to test data file
Output: number of correctly classified test examples
'''

def run_classify(w, testing_data):
    test_data = open(testing_data, "rt")
    y_data = []
    y_classified = []
    x1 = []
    x2 = []
    correct = 0
    for i, line in enumerate(test_data):
        a, b, c = [float(x) for x in line.split()]
        y_data.append(a)
        x1.append(b)
        x2.append(c)   
        x = [x1[i], x2[i]]
        classed = p_classify(x,w)
        y_classified.append(classed)
        if(a == classed):
            correct = correct + 1
    return correct


'''
Function: menu
Purpose: handle user input, output to text files, calculate accuracies
Input: N/A
Output: write to files.
'''

def menu():
    training_data = sys.argv[1]
    testing_data = sys.argv[2]
    count = 0
    while count == 0:
        print """
What would you like to do?
0) Exit
1) Write f(epochs)
2) Write Random vs Static"""
        action = raw_input("> ")
        if action == str(1):
            print "-------------------------------------------------"
            percents = []
            pfile = open('percentages.txt', 'w+')
            for num_epochs in range(1,101):
                w = p_train(num_epochs, training_data)
                percent = run_classify(w,testing_data)                  #calculate static accuracies
                fline = str(num_epochs) + ", " + str(percent) + """     
"""                                                                     
                pfile.write(fline)                                      #output to file
            print "Written to percentages.txt."
            print "-------------------------------------------------"
            pfile.close()
            
        elif action == str(2):
            print "-------------------------------------------------"
            print "Written to percentages_random.txt"
            percents = []
            pfile = open('percentages_random.txt', 'w+')
            for num_epochs in range(1,101):
                w = p_train(num_epochs, training_data)
                percent = run_classify(w,testing_data)
                w = p_train_random(num_epochs, training_data)
                rpercent = run_classify(w,testing_data)                 #calculate random accuracies
                fline = str(num_epochs) + ", " + str(percent) + ", " + str(rpercent) + """
"""                                                                     
                pfile.write(fline)                                      #output to file
            print "-------------------------------------------------"
            pfile.close()
            
        elif action == str(0):
            sys.exit()
        else:
            print "Invalid input. Try again ....."
            
            
if __name__ == '__main__':
    main()