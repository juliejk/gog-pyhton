s,l = raw_input("String: "),raw_input("Letter: ")
def t():
    a = 0
    for i in range(len(s)):
        if s[i] == l.upper() or s[i] == l.lower():
            a += 1
    return a
print t()