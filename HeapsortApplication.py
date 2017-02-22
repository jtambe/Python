

import heapq


def ApplyHeapQueue(a):

    return 0



def main():
    # a = [1,22,45,12,32,18,9,7,56,14,26]
    stack = []
    heap = []
    #print(a.index(45))
    # print(a)
    # a = a[:0]+a[1:]
    # print(a)
    # a = "1 21"
    # print(a.split(" "))

    noOfQueries = input()
    for i in range(int(noOfQueries)):
        print("give your query")
        query = input()
        if query == '2':
            if len(stack) > 0:
                val = stack.pop()
                heapIndex = heap.index(val)
                heap = heap[:heapIndex] + heap[heapIndex+1:]
                print((stack))
                print((heap))
        if query == '3':
            if(len(heap) > 0):
                heap = sorted(heap)
                print(heap[-1])
        if query.__contains__("1"):
            val = int(query.split(" ")[1])
            stack.append(val)
            heap.append(val)


if __name__ == "__main__":
    main()

#1 val = push val in stack
#2 pop stack
#3 get max in stack