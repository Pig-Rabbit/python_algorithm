# search string using BM method(the length of string is 0~255)

def bm_match(txt: str, pat: str) -> int:
    skip = [None] * 256

    # skip table
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # search
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
            else len(pat) - pp
    return -1

if __name__ == '__main__':
    s1 = input('enter text: ')
    s2 = input('enter pattern: ')

    idx = bm_match(s1, s2)

    if idx == -1:
        print("the pattern doesn't exist")
    else:
        print(f'the {(idx + 1)} text is the same')