#Adding elements to queue at the rear end
def enqueue(data):
        queue.insert(0,data)
 #Removing the front element from the queue
def dequeue(): 
    if len(queue)>0:
        return queue.pop() 
    return ("Queue Empty!") 
#To display the elements of the queue
def display():
    print("Elements on queue are:");
    for i in range(len(queue)):
        print(queue[i])
 # executable code
queue=[] 
enqueue(5) 
enqueue(6)
enqueue(9)
enqueue(5)
enqueue(3)
print("Queue before popping element: ")
display() 
print("\nPopped Element is: "+str(dequeue()))
print("Queue after popping element: ") 
display()
