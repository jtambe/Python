#Max Heap in python
# public functions : push , peek, pop
# private functions: _swap , _floatUp, _bubbleDown



class MinHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]

        # add value to the end of array and then float up
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)


    # add value to the end of array and then float up
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)


    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    # pop
    # swap last value with first value
    # check both children of first node and bubble it down to replace max of two children

    # 3 cases
    # 1. pop from array of only one element
    # 2. pop from empty array
    # 3. Generic case as above
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) -1) # swap first with last
            min = self.heap.pop()
            self.__bubbledown(1) # then bubbledown first value
        elif len(self.heap) == 2:
            min = self.heap.pop()
        else:
            min = False

        return min


    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 2 cases
    # 1. floating from top position. which means no floating up
    # 2. Generic case
    def __floatUp(self, index):
        # float up needs to check parent
        parent = index//2
        # base case for recursive function
        if index <= 1:
            return
        # if recently added value at index is smaller than parent, float it up and then do it for parent
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index,parent)
            self.__floatUp(parent)

    def __bubbledown(self, index): # maxheapify
        # bubbledown needs to check left and right children
        # get left, right and current index
        left = index * 2
        right = index * 2 + 1
        smallest = index

        # check if any of the child is smaller than current index
        if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
            smallest = left
        if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
            smallest = right

        # if any child was bigger than index, then swap it with smallest value and call bubbledown on it
        if smallest != index:
            self.__swap(index,smallest)
            self.__bubbledown(smallest)



m = MinHeap([12,58,75])
m.push(10)
print(str(m.heap))
#print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
print(str(m.pop()))



























