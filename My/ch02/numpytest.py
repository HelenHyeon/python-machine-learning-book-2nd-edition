"""
넘파이(Numpy)는 수치 데이터를 다루는 파이썬 패키지입니다.
Numpy의 핵심이라고 불리는 다차원 행렬 자료구조인 ndarray를 통해 벡터 및 행렬을 사용하는 선형 대수 계산에서 주로 사용됩니다.
Numpy는 편의성뿐만 아니라, 속도면에서도 순수 파이썬에 비해 압도적으로 빠르다는 장점이 있습니다."""

import numpy as np #Numpy의 경우, 주로 np라는 명칭으로 임포트하는 것이 관례입니다.

"""
Numpy의 주요 모듈은 아래와 같습니다.
1. np.array() # 리스트, 튜플, 배열로 부터 ndarray를 생성
2. np.asarray() # 기존의 array로 부터 ndarray를 생성
3. np.arange() # range와 비슷
4. np.linspace(start, end, num) # [start, end] 균일한 간격으로 num개 생성
5. np.logspace(start, end, num) # [start, end] log scale 간격으로 num개 생성"""



# np.array()
a = np.array([1, 2, 3, 4, 5]) #리스트를 가지고 1차원 배열 생성
print(type(a))
print(a)
# array() 안에 하나의 리스트만 들어가므로 리스트의 리스트를 넣어야 합니다.
b = np.array([[10, 20, 30], [ 60, 70, 80]]) 
print(b) #출력
# 행렬의 차원 및 크기를 ndim 속성과 shape 속성으로 출력할 수 있습니다.
print(a.ndim) #차원 출력
print(a.shape) #크기 출력
print(b.ndim) #차원 출력
print(b.shape) #크기 출력



# np.array 초기화
"""
위에서는 리스트를 가지고 ndarray를 생성했지만, ndarray를 만드는 다양한 다른 방법이 존재합니다.
zeros()는 해당 배열에 모두 0을 삽입하고, ones()는 모두 1을 삽입합니다.
full()은 배열에 사용자가 지정한 값을 넣는데 사용하고,
eye()는 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성합니다."""
A = np.zeros((2,3)) # 모든값이 0인 2x3 배열 생성.
print(A)
B = np.ones((2,3)) # 모든값이 1인 2x3 배열 생성.
print(B)
C = np.full((2,2), 7) # 모든 값이 특정 상수인 배열 생성. 이 경우에는 7.
print(C)
D = np.eye(3) # 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성.
print(D)
E = np.random.random((2,2)) # 임의의 값으로 채워진 배열 생성
print(E)



# np.arange()
"""
np.arange()는 지정해준 범위에 대해서 배열을 생성합니다.
np.arange()의 범위 지정 방법은 다음과 같습니다.

numpy.arange(start, stop, step, dtype)
a = np.arange(n) # 0, ..., n-1까지 범위의 지정.
a = np.arange(i, j, k) # i부터 j-1까지 k씩 증가하는 배열."""
F = np.arange(10) #0부터 9까지
print(F)
G = np.arange(1, 10, 2) #1부터 9까지 +2씩 적용되는 범위
print(G)



# reshape()
# 0부터 n-1 까지의 숫자를 생성하는 arange(n) 함수에 배열을 다차원으로 변형하는 reshape()를 통해 배열을 생성합니다.
H = np.array( np.arange(30) ).reshape( (5,6) )
print(H)



# Numpy 슬라이싱
"""
ndarray를 통해 만든 다차원 배열은 파이썬의 리스트처럼 슬라이스(Slice) 기능을 지원합니다.
슬라이스 기능을 사용하면 원소들 중 복수 개에 접근할 수 있습니다."""
I = np.array([[1, 2, 3], [4, 5, 6]])
J = I[0:2, 0:2]
print(J)
# 다차원 배열을 슬라이싱하기 위해서는 각 차원 별로 슬라이스 범위를 지정해줘야 합니다.
J = I[0, :] # 첫번째 행 출력
print(J)
J = I[:, 1] # 두번째 열 출력
print(J)



# Numpy 정수 인덱싱(integer indexing)
# 정수 인덱싱은 원본 배열로부터 부분 배열을 구합니다.
K = np.array([[1,2], [4,5], [7,8]])
print(K)
L = K[[2, 1],[1, 0]] # K[[row2, row1],[col1, col0]]을 의미함.
print(L) # [8 4] (2열 1행, 1열 0행)



# Numpy 연산
"""
Numpy를 사용하면 배열간 연산을 손쉽게 수행할 수 있습니다.
+, -, *, /의 연산자를 사용할 수 있으며,
또는 add(), subtract(), multiply(), divide() 함수를 사용할 수도 있습니다."""
x = np.array([1,2,3])
y = np.array([4,5,6])
M = x + y # 각 요소에 대해서 더함
print(M)
# M = np.add(x, y)와 동일함
M = x - y # 각 요소에 대해서 빼기
print(M)
# M = np.subtract(x, y)와 동일함
M = y * x # 각 요소에 대해서 곱셈
print(M)
# M = np.multiply(y, x)와 동일함
M = 60 / x # 각 요소에 대해서 나눗셈
print(M)
# M = np.divide(60, x)와 동일함
"""위에서 *를 통해 수행한 것은 요소별 곱이었습니다.
Numpy에서 벡터와 행렬의 곱 또는 행렬곱을 위해서는 dot()을 사용해야 합니다."""
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.dot(a, b)
print(c)