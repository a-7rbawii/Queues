import sys

def initialiseQueue():
    queue = [None for i in range(10)]
    return queue

def enQueue(item):
    global qLength
    global rear
    if qLength < len(myQueue):
        if rear < len(myQueue) - 1:
            rear = rear + 1
        else:
            rear = 0
        qLength = qLength + 1
        myQueue[rear] = item
        print("Item enqueued ✅")
    else:
        print("⚠ Queue is full ⚠")

def deQueue():
    global qLength
    global front
    if qLength == 0:
        print("⚠Queue is empty, cannot dequeue⚠")
    else:
        deqItem = myQueue[front]
        myQueue[front] = None
        if front == len(myQueue) - 1:
            front == 0
        else:
            front = front + 1
    qLength = qLength - 1

def display():
    print("--------------------------")
    print("Current stack:{}".format(myQueue))
    print("--------------------------")

def menu():
    while qLength <= len(myQueue):
        print("Choose procedure to perform on the stack:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        option = int(input())

        if option == 1:
            item = int(input("Input the item to enqueue\n"))
            enQueue(item)
        elif option == 2:
            deQueue()
        elif option == 3:
            display()
        elif option == 4:
            sys.exit()
        else:
            print("Invalid option")

myQueue = initialiseQueue()
front = 0
rear = -1
qLength = 0

menu()