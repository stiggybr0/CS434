import sys
import csv
import math

'''
Created on Oct 16, 2012

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
        print "Usage: python main.py monks-1-train.csv monks-1-test.csv" 
        sys.exit()
    menu()
    
    
'''
Function: value_init
Purpose: static training algorithm
Input: CSV of monk data.
Output: 2d array with values and probabilities.
'''
    
def value_init(csvname):
    datamap = []
    classline = []
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    line5 = []
    line6 = []
    
    csvmap = csv.reader(open(csvname))
    
    for row in csvmap:
        classify, x1, x2, x3, x4, x5, x6 = [int(x) for x in row] 
        classline.append(classify)
        line1.append(x1)
        line2.append(x2)
        line3.append(x3)
        line4.append(x4)
        line5.append(x5)
        line6.append(x6)

    datamap.append(classline)
    datamap.append(line1)
    datamap.append(line2)
    datamap.append(line3)
    datamap.append(line4)
    datamap.append(line5)
    datamap.append(line6)

    return datamap

'''
Function: entropy_calc
Purpose: Calculate entropies of each data set
Input: datamap of initialized CSVs
Output: appended entropies
'''

def entropy_calc(datamap):
    counter = 0
    entropylist = []
    entropyval = 0.0
    pos = []
    neg = []
    monkset = []
    monkamount = 0
    prob = []
    countmore = 0
    totalentropy = -.5* math.log(.5, 2) - .5* math.log(.5, 2)    
    infolist = [0] * 6
    entropymap  = []
    probstats = []
    itemcount = []
    itemmap = []
    
    for  list in datamap:
        if (counter == 0):
            monkset = list
            for item in monkset:
                if(item == 1):
                    monkamount = monkamount + 1
        else:
            if(counter == 1 or counter == 2 or counter == 4):
                pos = [0] * 3
                prob = [0] * 3
                neg = [0] * 3
                itemcount = [0] * 3
            elif(counter == 3 or counter == 6):
                pos = [0] * 2
                prob = [0] * 2
                neg = [0] * 2
                itemcount = [0] * 2
            elif(counter == 5):
                pos = [0] * 4
                prob = [0] * 4
                neg = [0] * 4
                itemcount = [0] * 4
            else:
                print "Sanity Check: Failed!"
            
            for i, item in enumerate(list):
                if (monkset[i] == 1):
                    pos[item-1] = pos[item-1] + 1
                    
                else:
                    neg[item-1] = neg[item-1] + 1
                
                #itemcount[item-1] = itemcount[item-1] + 1
            
            for i in range(len(pos)):
                itemcount[i] = pos[i] + neg[i]
            
            itemmap.append(itemcount)
            
            for i in range(len(prob)):
                probpair= [0] * 2
                probpair[0] = float(pos[i])/(float(pos[i])+float(neg[i]))
                probpair[1] = float(neg[i])/(float(pos[i])+float(neg[i]))
                countmore = countmore + 1
                prob[i] = probpair
           
            countmore = 0
            probstats.append(prob)
            for item in prob:
                if (item[0] != 1.0 and item[0] != 0.0):
                    entropyval = 0.0 - item[0]*(math.log(item[0], 2)) - item[1]*(math.log(item[1], 2))
                
                else:
                    entropyval = 0.0
                
                entropylist.append(entropyval)
                entropyval = 0.0
            entropymap.append(entropylist)
            entropylist = []
        counter = counter + 1
        
        for i, row in enumerate(entropymap):
            infolist[i] = totalentropy
            itemrow = itemmap[i]
            entropyrow = entropymap[i]
            for j, item in enumerate(row):
                infolist[i] = infolist[i] - itemrow[j]/124.0*entropyrow[j]
            
    print infolist
    return prob
'''
Function: stump_creator
Purpose: take entropies and create single featured decision stump
Input: entropylist
Output: decisionstump
'''

def info_gain(datamap, entropylist):
    
    
    return
    
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
1) See work so far"""
        action = raw_input("> ")
        if action == str(1):
            print "-------------------------------------------------"
            dmap = value_init(training_data) 
            entropylist = entropy_calc(dmap)
            gainlist = info_gain(dmap, entropylist)
                                                                               
            print "-------------------------------------------------"
              
        elif action == str(0):
            sys.exit()
        else:
            print "Invalid input. Try again ....."
            
            
if __name__ == '__main__':
    main()