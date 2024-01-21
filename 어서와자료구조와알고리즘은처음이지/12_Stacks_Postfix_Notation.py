class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for op in S:
        if op in prec: # 1) prec 속 연산자일 때
            if opStack.isEmpty():
                opStack.push(op)
            else:
                if prec[op] > prec[opStack.peek()] or op == '(':
                    opStack.push(op)
                else:
                    while not opStack.isEmpty():
                        if prec[opStack.peek()] >= prec[op]:
                            answer += opStack.pop()
                        else: break
                    opStack.push(op)
                    
        elif op == ')': # 2) 닫힌 괄호일 때
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop() # 열린 괄호 pop
            
        else: # 3) 문자일 때
            answer += op
            
    while not opStack.isEmpty():
        answer += opStack.pop()
        
    return answer