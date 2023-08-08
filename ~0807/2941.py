X = str(input())

# 크로아티아 알파벳을 리스트로 둔다
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for s in lst:
    # 만약 크로아티아 알파벳이 있으면 우리가 알기 쉬운 문자로 replace를 통해 바꾼다
    if s in X:
        X = X.replace(s, 'A')
    else:
        pass
print(len(X))