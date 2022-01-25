# Replace로 진행하면 string을 발견시마다 반복문을 돌고,
# 새롭게 구성되는 문자열에 다시 반복을 돌려야 하지만
# stack을 사용하면 폭발 문자열을 없앤 뒤 바로 이어서 생성되는 폭발 문자열을 바로 제거할 수 있기 때문에
# 반복을 한번만 돌아도 된다.

string = input()    # 전체 문자열
bomb = input()      # 폭발 문자열

lastChar = bomb[-1] # 폭발 문자열의 마지막 글자
stack = []
length = len(bomb)  # 폭발 문자열의 길이

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)