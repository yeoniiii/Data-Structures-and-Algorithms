class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
    
    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount: # k번째 노드 없음
            return None
        i = 1
        curr = self.head # 첫번째 노드
        while i < pos:
            curr = curr.next
            i += 1
        return curr
    
    def traverse(self):
        answer = []
        curr = self.head
        while curr != None:
            answer.append(curr.data)
            curr = curr.next
        return answer
    
    def get_length(self):
        return self.nodeCount
    
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount  + 1: # 맨 마지막에 삽입
                prev = self.tail
            else:
                prev = self.getAt(pos - 1) # 삽입 위치 이전 노드
            newNode.next = prev.next
            prev.next = newNode
        
        if pos == self.nodeCount + 1: # 맨 마지막에 삽입
            self.tail = newNode
        
        self.nodeCount += 1
        return True
    
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        if pos == 1:
            r = self.head
            if self.nodeCount == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        else:
            prev = self.getAt(pos - 1)
            r = prev.next
            if pos == self.nodeCount:
                prev.next = None
                self.tail = prev
            else:
                prev.next = r.next

        self.nodeCount -= 1
        return r.data

    def concat(self, L):
        self.tail.next = L.head
        if L.tail: # L.tail != None
            self.tail = L.tail
        self.tail = L.tail
        self.nodeCount += L.nodeCount