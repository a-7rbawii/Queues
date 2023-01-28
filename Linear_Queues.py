import sys

def initialiseQueue():
    queue = [None for i in range(10)]
    return queue

def enQueue(item):
    global basePointer
    if basePointer == len(myQueue):
        print("⚠Queue is full, cannot enqueue⚠")
    else:
        myQueue[basePointer] = item
        basePointer = basePointer + 1
        print("Item enqueued ✅")

def deQueue():
    global topPointer
    global basePointer
    if topPointer == basePointer:
        print("⚠Queue is empty, cannot dequeue⚠")
    else:
        deqItem = myQueue[topPointer]
        myQueue[topPointer] = None
        topPointer = topPointer + 1
        print("Item {} dequeued ✅".format(deqItem))
        return deqItem

def display():
    print("--------------------------")
    print("Current stack:{}".format(myQueue))
    print("--------------------------")

def menu():
    while topPointer <= len(myQueue):
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
topPointer = 0
basePointer = 0

menu()