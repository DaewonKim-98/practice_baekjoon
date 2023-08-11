while True:
    sentence = list(map(str, input()))
    # 온점이 나올 때 break
    if sentence[0] == '.':
        break
    
    stack = []
    # sentence를 돌리는데 
    for word in sentence:
        result = 'yes'
        # (, [가 뜨면 1, 2 추가
        if word == '(':
            stack.append(1)
        elif word == '[':
            stack.append(2)
        
        elif word == ')':
            # ) 가 들어오는데 스택이 비어 있으면 균형을 이루지 않으므로 종료
            if len(stack) == 0:
                result = 'no'
                break
            else:
                if stack[-1] == 1:
                    stack.pop()
                # ) 가 들어오는데 앞에 (가 없으면 종료
                else:
                    result = 'no'
                    break

        elif word == ']':
            # ) 가 들어오는데 스택이 비어 있으면 균형을 이루지 않으므로 종료
            if len(stack) == 0:
                result = 'no'
                break
            else:
                if stack[-1] == 2:
                    stack.pop()
                # ) 가 들어오는데 앞에 (가 없으면 종료
                else:
                    result = 'no'
                    break
    
    # for문이 다 끝나면 stack은 비어 있어야 하는데 아니면 no
    if stack:
        result = 'no'
    print(result)