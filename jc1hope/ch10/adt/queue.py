# increment r to enqueue
#increment f to dequeue

QueueArray = [None for _ in range (4)]

F = 0
R = -1
maxsize = len(QueueArray)
queuelen = 0

def enqueue(Element):
    global R, queuelen
    if queuelen == maxsize:
        print("Cannot enqueue, queue is full")
    else:
        if R == (maxsize - 1):
            R = 0
            QueueArray[R] = Element
            print(QueueArray[R])
            
        else:
            R += 1
            queuelen += 1
            QueueArray[R] = Element

def dequeue():
     global F, queuelen
     if queuelen == 0:
         print("Cannot dequeue, queue empty")
     else:
         F += 1
         print(QueueArray[F])
         queuelen -= 1

print(QueueArray)
