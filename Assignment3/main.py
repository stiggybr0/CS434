import sys
import csv
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
    while len(cluster_head) < kmeans:
        selected_point = graph_data[random.randint(0, len(graph_data))]
        if selected_point not in cluster_head:
            seed = []
            seed.append(selected_point)
            cluster_head.append(seed)
            
    #print cluster_head
    return cluster_head       
    
'''
Function:cluster_assign
Purpose: Add all points to cluster group
Input: cluster_head, graph_data, kmeans
Output: cluster_array
'''
def cluster_assign(cluster_head, graph_data, kmeans):
    cluster_array = [0]*kmeans
    for i in range(0,kmeans):
        cluster_array[i] = []
        
    closest = 10000000000000
    cluster_index = -1
    for point in graph_data:
        for i, head in enumerate(cluster_head):
            #print head[0][0]
            
            #distance formula!
            xd = float(head[0][0])-float(point[0])
            yd = float(head[0][1])-float(point[1])
            if (xd == 0 and yd == 0):
                cluster_index = i
                cluster_array[cluster_index].append(point)
                
            distance = (xd**2.0 + yd**2.0)**.5
            if distance < closest:
                closest = distance
                cluster_index = i
            
        #print closest
        cluster_array[cluster_index].append(point)
        closest = 100000000000000
    
    for cluster in cluster_array:
        if len(cluster) == 1:
            print"Unfilled!"
        
    return cluster_array

'''
Function: compute_centroids
Purpose: finds the average of each cluster
Input: cluster_array
Output: centroid_head
'''
def compute_centroids(cluster_array):
    centroid_head= []
    for cluster in cluster_array:
        head = []
        headholder = []
        xavg = 0.0
        yavg = 0.0
        #print cluster
        for point in cluster:
            if len(point) is 2:
                xavg = xavg + float(point[0])
                yavg = yavg + float(point[1])
            
        if len(cluster) > 0:
            xavg = xavg/float(len(cluster))
            yavg = yavg/float(len(cluster))
        head.append(xavg)
        head.append(yavg)
        headholder.append(head)
        centroid_head.append(headholder)

    #print centroid_head
    return centroid_head

'''
Function:compute_sse
Purpose:Find the sse for the given clusters and centroids
Input: cluster_array, centroid_head
Output: total_sse
'''
def compute_sse(cluster_array, centroid_head):
    sse = 0
    total_sse = 0
    for i, centroid in enumerate(centroid_head):
        for point in cluster_array[i]:
            xd = float(centroid[0][0])-float(point[0])
            yd = float(centroid[0][1])-float(point[1])
            distance = (xd**2.0 + yd**2.0)**.5
            sse = sse + distance**2
        total_sse = total_sse + sse
        sse = 0
            
    #print total_sse        
    return total_sse

'''
Function: converge_sse
Purpose:repeats clustering and writes total_sse(s) to sses.txt
Input: total_sse, centroid_head, graph_data, kmeans
Output: sses.txt
'''
def converge_sse(total_sse, centroid_head, graph_data, kmeans):
    old_sse = total_sse + 1
    ssefile = open('sses.txt', 'w+')
    while (old_sse > total_sse):
                old_sse = total_sse
                cluster_array = cluster_assign(centroid_head, graph_data, kmeans)
                centroid_head = compute_centroids(cluster_array)
                total_sse = compute_sse(cluster_array, centroid_head)
                #print total_sse
                ssefile.write(str(total_sse)+"\n")
                
                

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
            print "Finding seeds."
            cluster_head = init_clusters(graph_data, kmeans)
            print "Filling in first clusters."
            cluster_array = cluster_assign(cluster_head, graph_data, kmeans)
            print "Computing centroids."
            centroid_head = compute_centroids(cluster_array)
            print "Computing first SSE."
            total_sse = compute_sse(cluster_array, centroid_head)
            print "Converging."
            converge_sse(total_sse, centroid_head, graph_data, kmeans)
                                                                               
            print "-------------------------------------------------"
              
        elif action == str(0):
            sys.exit()
        else:
            print "Invalid input. Try again ....."
            
            
if __name__ == '__main__':
    main()