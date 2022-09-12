import numpy as np

def mat_inpu(x,y,l):
    
    for i in range(x):  
        # taking input for the row from the user  
        q = list(map(int, input().split()))  
        # appending the 'single_row' to the 'example_matrix'  
        l.append(q)

def mat_pri(x,y,l,m):
    print()
    print(m)
    for i in range(x):
        for j in range(y):
            print(l[i][j], end=" ")
        print()

def Need_Mat_create(x,y,l1,l2):
    #l1- allocation matrix
    #l2- max matrix
    #l3- need matrix
    d=(x,y)
    l3=np.zeros(d)
    for i in range(x):
        for j in range(y):
            l3[i][j]+=l2[i][j] - l1[i][j] 
    return l3

def check(i):
    for j in range(r):
        if(Need_Matrix[i][j]>available[j]):
            return 0
    return 1

p=int(input("enter number of processes: "))
r=int(input("enter number of resources: "))
Allocation_Matrix=[]
Max_matrix=[]
Need_Matrix=[]
available=[]
visited = np.zeros((p,),dtype=int)
Sequence = np.zeros((p,),dtype=int)



#input for available
print("Enter availablity row wise: ")
for i in range(r):
    x=int(input())
    available.append(x)


#input for allocation matrix
print("\nFor allocation: ")
mat_inpu(p,r,Allocation_Matrix)
mat_pri(p,r,Allocation_Matrix,"The allocation matrix is- ")


#input for Max matrix
print("\nFor Max: ")
mat_inpu(p,r,Max_matrix)
mat_pri(p,r,Allocation_Matrix,"The Max matrix is- ")

#creating need matrix
Need_Matrix = Need_Mat_create(p,r,Allocation_Matrix,Max_matrix)
mat_pri(p,r,Need_Matrix,"The Need Matrix is- ")

#creting Safe sequence
count = 0
while( count < p ):
    temp=0
    for i in range( p ):
        if( visited[i] == 0 ):
            if(check(i)):
                Sequence[count]=i;
                count+=1
                visited[i]=1
                temp=1
                for j in range(r):
                    available[j] += Allocation_Matrix[i][j] 
    if(temp == 0):
        s="unsafe"
        break
    else:
        s="safe"

print(s)
if s=="safe":
    print("the sequence of Processes is: ",Sequence)
else:
    print("safe")

#Banker's Algorithm by Aadi Juvekar