import sys
import csv
import math
import random

'''
Created on Oct 30, 2012

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
        print "Usage: python main.py cluster-data.csv kmeans-num" 
        sys.exit()
        
    menu()
    
'''
Function:init_graph
Purpose: adds raw input into list to build graph.
Input: raw sys.arg
Output: Array of points
'''

def init_graph(cluster_data):
    graph_data=[]
    cluster_file = csv.reader(open(cluster_data, "rt"))
    for line in cluster_file:
        graph_data.append(line)
        
    #print graph_data  
    return graph_data  
    
'''
Function:init_clusters
Purpose: adds cluster lists into central array with random clustered data.
Input: graph_data, kmeans
Output: cluster_head
'''
def init_clusters(graph_data, kmeans):
    init_clusters = [0] * kmeans
    cluster_head = []
    while len(cluster_head) < 3:
        selected_point = graph_data[random.randint(0, len(graph_data))]
        if selected_point not in cluster_head:
            cluster_head.append(selected_point)
    return cluster_head       
    #print cluster_head
    
'''
Function:first_cluster
Purpose: Add all points to first cluster group
Input: cluster_head
Output: cluster_array
'''
def first_cluster(cluster_head, graph_data):
    cluster_array = cluster_head
    closest = 0
    
    for point in graph_data:
        if point not in cluster_head:
            for i in
    
    
'''
Function: menu
Purpose: handle user input, output to text files, calculate accuracies
Input: N/A
Output: write to files.
'''

def menu():
    cluster_data = sys.argv[1]
    kmeans = int(sys.argv[2])
    count = 0
    while count == 0:
        print """
What would you like to do?
0) Exit
1) See work so far"""
        action = raw_input("> ")
        if action == str(1):
            print "-------------------------------------------------"
            print "Initializing graph."
            graph_data = init_graph(cluster_data)
            init_clusters(graph_data, kmeans)
                                                                               
            print "-------------------------------------------------"
              
        elif action == str(0):
            sys.exit()
        else:
            print "Invalid input. Try again ....."
            
            
if __name__ == '__main__':
    main()