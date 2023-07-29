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


# 수가 문자열로 주어져 있을 때 (몇자리 수인지 모르는상태) 
# 각각을 피연산자인 수와 연산자인 기호로 분리해서 리스트로 만드는 작업
# exprStr -> 중위 표현식으로된 수식
def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


# 중위표기식 -> 후위표기식
def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        # 피연산자이면 리스트에 추가
        if type(token) is int:
            postfixList.append(token)
        
        # '('이면 스택에 push
        elif token == '(':
            opStack.push(token)
        
        # ')'이면 '('가 나올 때까지 pop
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop() # 열린 괄호 제거
        
        # +-*/ 연산자이면
        else:
            # 스택이 비어있을 경우 스택에 push
            if opStack.isEmpty():
                opStack.push(token)
            
            # 스택이 비어있지 않을 경우 비교
            else:
                # 스택에 값이 존재할 동안 반복
                while not opStack.isEmpty():
                    if prec[token] <= prec[opStack.peek()]:
                        postfixList.append(opStack.pop())
                    else:
                        break
                opStack.push(token)
    
    # 반복문을 다 돌고 스택이 빌 때까지 pop
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()
    
    for token in tokenList:
        if type(token) is int:
            valStack.push(token) 
        else:
            t1 = valStack.pop()
            t2 = valStack.pop()
            valStack.push(eval(f'{t2}{token}{t1}'))
    
    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val