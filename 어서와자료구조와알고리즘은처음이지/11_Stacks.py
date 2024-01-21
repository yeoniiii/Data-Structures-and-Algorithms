#!/usr/bin/env python
# coding: utf-8

# # 스택 Stacks
# : 자료 data elemet 를 보관할 수 있는 선형 구조
# - 단 넣을 때에는 한 쪽 끝에서 밀어 넣어야 하고 → 푸시 `push` 연산
# - 꺼낼 때에는 같은 쪽에서 뽑아 꺼내야 하는 제약이 있음 → 팝 `pop` 연산
# - 후입선출 LIFO (Last-In First-Out) 특징을 가지는 선형 자료구조
# - 발생 가능 오류 2가지
#   - 비어 있는 스택에서 데이터 원소를 꺼내려 할 때 ➡️ 스택 언더플로우 stack underflow
#   - 꽉 찬 스택에 데이터 원소를 넣으려 할 때 그림 ➡️ 스택 오버플로우 stack overflow

# ## 스택의 추상적 자료구조 구현
# #### 1. 배열 array을 이용하여 구현
# - Python 리스트와 메서드들을 이용

# In[2]:


class ArrayStack:

	def __init__(self): # Constructor Method
			self.data = [] # 빈 스택을 초기화

	def size(self):
			return len(self.data) # 스택의 크기를 리턴

	def isEmpty(self):
			return self.size() == 0 # 스택이 비어 있는지 판단

	def push(self, item):
			self.data.append(item) # 데이터 원소를 추가

	def pop(self):
			return self.data.pop() # 데이터 원소를 삭제, 리턴

	def peek(self):
			return self.data[-1] # 스택의 꼭대기 원소 반환


# #### 2. 연결 리스트 linked list를 이용하여 구현
# - 양방향 연결 리스트 이용

# In[3]:


from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList

class LinkedListStack:

	def __ini__(self):
		self.data = DoublyLinkedList() # 비어있는 dl로 초기화

	def size(self):
		return self.data.getLength()

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		node = Node(item)
		self.data.insertAt(self.size() + 1, node)

	def pop(self):
		return self.data.popAt(self.size())

	def peek(self):
		return self.data.getAt(self.size()).data


# #### 3. 라이브러리

# In[10]:


from pythonds.basic.stack import Stack
S = Stack() # Stack 초기화
dir(S)[-10:] # method 보기 


# ## 연습 문제
# 소괄호: ( )
# 
# 중괄호: { }
# 
# 대괄호: [ ]
# 
# 를 포함할 수 있는 수식을 표현한 문자열 `expr` 이 인자로 주어질 때, 이 수식의 괄호가 올바르게 여닫혀 있는지를 판단하는 함수 `solution()` 을 완성하세요. 이 함수는 수식의 괄호가 유효하면 `True` 를, 그렇지 않으면 `False` 를 리턴합니다.
# 
# 스택을 활용하여 수식 내의 괄호 여닫음의 유효성을 검사하는 알고리즘에 대해서는 동영상 강의 내용을 참고하세요.

# In[ ]:


def solution(expr):
	match = {
		')': '(',
		'}': '{',
		']': '[',
	}
	S = ArrayStack()
	for c in expr:
		if c in '({[':
			S.push(c)
		elif c in match:
			if S.isEmpty():
				return False
			else:
				t = match[c]
				if t != S.pop():
					return False
	return S.isEmpty()

