# searching string using brute force method

def bf_match(txt: str, pat: str) -> int:
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0
    
    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('enter text: ')
    s2 = input('enter pattern: ')

    idx = bf_match(s1, s2)

    if idx == -1:
        print("the pattern doesn't exist")
    else:
        print(f'the {(idx + 1)} text is the same')