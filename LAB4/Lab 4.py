#Course: CS2302 - Spring 2019

#Author: Solomon Davis
#Lab Number: 4
#Instructor: Olac Fuentes
#Last Modified: March 24, 2019
#Due Date: March 15, 2019
#Description: This code will use b-trees to carry out specific tasks. These 
#tasks include commputing the height of the tree,extracting items from a b-tree
#into a sorted list, returning the minimum and maximum value, returning the 
#number of nodes at a specific depth, printing the values at a specific depth,
#returning the of full nodes and full trees, and lastly given the depth of a 
#specific key in the b-tree.

import time
import matplotlib.pyplot as plt

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    #Retutns the height of the B-tree
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
def Smallest(T):
    if T.isLeaf:
        return T.item[0]
    return Smallest(T.child[0])

def Largest(T):
    if T.isLeaf:
        return T.item[-1]
    return Largest(T.child[len(T.item)])

def SmallestAtDepth(T,d):
    #Returns the smallest value at the given depth d
    if T.isLeaf:            #If at depth d is the Btree is a leaf it returns the item with the smallest value
        return T.item[0]
    if d==0:                #If the depth is 0 the smallest value is then returned from the given values
        return T.item[0]
    return SmallestAtDepth(T.child[0],d-1) #return the left most child in the Btree until the function is in the correct depth

def LargestAtDepth(T,d):
    #Returns the largest value at the given depth d    
    if T.isLeaf:        #If at depth d is the Btree is a leaf it returns the item with the largest value
        return T.item[-1]
    if d==0:             #If the depth is 0 the largest value is then returned from the given values
        return T.item[-1]
    return LargestAtDepth(T.child[len(T.item)],d-1)  #return the right most child in the Btree until the function is in the correct depth


def NumItems(T):
    #count = 0
    if T.isLeaf:
        return len(T.item)
    for i in range(len(T.child)):
        NumItems(T.child[i])
        #count +=1
        #print(count)
        return NumItems(T.child[i]) + len(T.item) 

def FindDepth(T,k):
    if k != T.item:
        return FindDepth(T.item,k) + 1
    if k == T.item:
        return 0
    #for i in range(len(T.item)-1,-1,-1)
    if k>T.item:
        return FindDepth(T.item,k) + 1
    if k<T.item:
        return FindDepth(T.item,k) + 1
    
def PrintDescending(T):
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(T.item[i],end=' ')
    else:
        PrintDescending(T.child[len(T.item)])  
        for i in range(len(T.item)-1,-1,-1):
            print(T.item[i],end=' ')
            PrintDescending(T.child[i])
                    
            
def PrintItemsInNode(T,k):
    if T.child.item[i] == k:
        return -1
    if T.child.item[i] < k:
       return PrintItemsInNode(T,k)
    return PrintItemsInNode(T,k)

#def Height(T):
 #   if T.isLeaf:
  #      return 1
   # else:
    #    for i in range(len(T.item)):
     #       return 1 + Height(T.child[i])
        
def PrintAtDepth(T,d):
    #Prints all the values at the given depth in the b-tree
    if d == 0:
        for i in range(len(T.item)):
            print(T.item[i],end=' ')    #Print the item in the tree

    for i in range(len(T.child)):       #Loop that traverses through entire the Btree 
        PrintAtDepth(T.child[i],d-1)    #Calls back to the function until the funtion is in the correct depth
        
def NumberOfNodesAtDepth(T,d):
    #Count the number of nodes at a given a depth d
    global count
    if d == 0:
        count +=1       #Count that adds one when there is a value at a depth
    for i in range(len(T.child)):       #Loop that traverses through entire the Btree 
        NumberOfNodesAtDepth(T.child[i],d-1)    #Calls back to the function until the funtion is in the correct depth
    return count

    
def SortedList(T,L2):
    #Takes the values in the b-tree and puts it into a sorted list
    if T.isLeaf:
        for t in T.item:
            L2.append(t)                #Appends value from tree to list
    else:
        for i in range(len(T.item)):    #Loop that traverses through entire the Btree        
            SortedList(T.child[i],L2)
            L2.append(T.item[i])        #Appends value from tree to list
        SortedList(T.child[len(T.item)],L2)

def SearchDepth(T,k,count):
    # Returns Depth where k is, or -1 if k is not in the tree
    if k in T.item:      #If the value k is equal to the item in the Btree the count is returned
        return count
    if T.isLeaf:        #If the value k is not found in the Btree then -1 is returned
        return -1
    #count +=1
    return SearchDepth(T.child[FindChild(T,k)],k,count+1)
                      

def FullNodes(T):
    #Returns the number of full nodes in the b-tree
    global nodecount
    if T.isLeaf:
        if len(T.item) == 3:        
            nodecount +=1 
    if len(T.child) == 3:
        nodecount +=1   
    for i in range(len(T.child)):   #Loop that traverses through entire the Btree 
        FullNodes(T.child[i])
              

    return nodecount    #Returns the count of full nodes

def FullLeaves(T):
    #Returns the number of full leaves in the b-tree
    global leafcount
    if T.isLeaf:
        if len(T.item) == 3:    #If the length of the leaf is 3 the count adds 1 to the counter
            leafcount +=1    
    else:    
        for i in range(len(T.child)):   #Loop that traverses through entire the Btree 
              FullLeaves(T.child[i])    

    return leafcount     #Returns the count of full leaves

L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    Print(T)
    print('\n####################################')
PrintD(T,'')
L2 = []
#start_time = time.time()
SortedList(T,L2)
#end_time = time.time()
#running_time = start_time-end_time
#plt.plot(0,running_time,'o',color='k')
print(L2)
count = 0
leafcount = 0
nodecount = 0
#start_time1 = time.time()
print(SearchDepth(T,30,count))
#end_time1 = time.time()
#running_time1 = start_time1-end_time1
#ax.plot(x,y,color='k')
#plt.plot(1,running_time1,'o',color='k')
#start_time2 = time.time()
print(NumberOfNodesAtDepth(T,2))
#end_time2 = time.time()
#running_time2 = start_time2-end_time2
#plt.plot(2,running_time2,'o',color='k')
#start_time3 = time.time()
print(FullLeaves(T))
#end_time3 = time.time()
#running_time3 = start_time3-end_time3
#plt.plot(3,running_time3,'o',color='k')
#start_time4 = time.time()
print(FullNodes(T))
#end_time4 = time.time()
#running_time4 = start_time4-end_time4
#plt.plot(4,running_time4,'o',color='k')
#Print(T)    
#SearchAndPrint(T,60)
#SearchAndPrint(T,200)
#SearchAndPrint(T,25)
#SearchAndPrint(T,20)
#start_time5 = time.time()
PrintAtDepth(T,2)
#end_time5 = time.time()
#running_time5 = start_time5-end_time5
#plt.plot(5,running_time5,'o',color='k')
#print(FindDepth(T,60))
#start_time6 = time.time()
print(height(T))
#end_time6 = time.time()
#running_time6 = start_time6-end_time6
#plt.plot(6,running_time6,'o',color='k')
#seconds = range(0,1000)
#print(running_time)
#plt.plot(6,running_time,'o',color='k')
#plt.show()
#start_time7 = time.time()
print(SmallestAtDepth(T,1))
#end_time7 = time.time()
#running_time7 = start_time7-end_time7
#plt.plot(7,running_time7,'o',color='k')
#start_time8 = time.time()
print(LargestAtDepth(T,2))
#end_time8 = time.time()
#running_time8 = start_time8-end_time8
#plt.plot(8,running_time8,'o',color='k')
#PrintDescending(T)
#print(FindDepth(T,1))
#print PrintItemsInNode(T,30)
#plt.show()
