# search string using KMP method

def kmp_match(txt: str, pat: str) -> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)

    # skip table
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] == pp
        else:
            pp = skip[pp]
    
    # search string
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    
    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('enter text: ')
    s2 = input('enter pattern: ')

    idx = kmp_match(s1, s2)

    if idx == -1:
        print("the pattern doesn't exist")
    else:
        print(f'the {(idx + 1)} text is the same')