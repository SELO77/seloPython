# yield를 만나는 순간 Context(환경)를 포함한 제너레이터라는 객체를 반환.
# 이 제네레이터 객체는 이터레이터 프로토콜을 제공하며, 따라서 iterable(순환가능) 하다

for i in range(5):
  print(i, end= ",") # 0,1,2,3,4,

def custom_range(end):
  i = 0
  while i < end:
    yield i
    i += 1

print()
result = custom_range(5)
print(result) # <generator object custom_range at 0x1017c5a98>

# custom_range() 함수는 내장함수인 range() 함수를 제너레이터를 이용해 구현한 예입니다.
# 위와 같이 구현된 함수를 코루틴 함수라 합니다. 코루틴? 제너레이터? 개념을 처음 접하신 분은 이해가
# 어려우실 수 있습니다. 여기서는 하나만 기억하고 넘어갑시다. yield가 선언된 함수는 yield를 만나는
# 순간 제너레이터라는 객체를 반환한다!! 그리고 왜 제너레이터는 순환가능한 것인가?
# 아래 코드를 보면서 궁금증을 풀어봅시다.


# generator는 순환 가능!! 왜?
for i in result:
  print(i, end=',') # 0,1,2,3,4,
print()
print(list(custom_range(5))) # [0, 1, 2, 3, 4]
print([i for i in custom_range(5)]) # [0, 1, 2, 3, 4]

generator = custom_range(2)
print(next(generator)) # 0
print(next(generator)) # 1

# 아래코드는 리스트의 인덱스 에러와 같이 더이상 진입점이 없으므로 예외를 발생시킨다.
# print(next(generator)) # raise Exception StopIteration


# 위에서 generator 변수에 대입된 custom_range(2) 함수는 yield 키워드에서 값을 반환하고,
# 다음 next()에 의해 호출될 때까지 해당 라인을 진입점으로 기억해둡니다. 이러한 진입점이 여러 개인
# 함수를 코루틴(coroutine) 이라하며, 기존에 우리가 주로 사용하는 코드를 순서대로 실행하다가
# return 코드를 만나고 최종 값을 리턴하면서 context를 잃는 방식을 서브루틴(subroutine)이라고 합니다.

# 결론은 첫째줄에 말씀드렸는데요. "yield를 만나는 순간 Context(환경)를 포함한 제너레이터라는 객체를 반환."
# 결국 제너레이터라는 객체는 코루틴이라는 함수가 진입점을 여러 곳 갖고 있기때문에 호출되는 순서에 따라
# Context(환경)이 달라지게 됩니다. 이로 인해 iterable(순환가능) 할 수 밖에 없는 숙명을 띠게 됩니다.


