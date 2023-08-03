while True:
    sentence = list(map(str, input()))
    # 온점이 나올 때 break
    if sentence[0] == '.':
        break

    # sentence를 돌리는데 (, [가 뜨면 뒤에서부터 돌려서 ), ]를 찾는다.
    for word in range(len(sentence) - 1):
        for nword in range(len(sentence) - 1, word, -1):
            if (sentence[word] == '(') and (sentence[nword] == ')'):
                sentence.remove('(')
                sentence.remove(')')
                sentence.append('a')
                sentence.append('a')
            if (sentence[word] == '[') and (sentence[nword] == ']'):
                sentence.remove('[')
                sentence.remove(']')                
                sentence.append('a')
                sentence.append('a')

    for w in sentence:
        if (w == '(') or (w ==')') or (w == '[') or (w == ']'):
            result = 'no'
            break
        else:
            result = 'yes'
    print(result)