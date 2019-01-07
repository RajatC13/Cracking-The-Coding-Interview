def urlify(s):
    return s.replace(' ', '%20')

def urlify1(s):
    s = list(s)
    a = []

    for c in s:
        if c == ' ':
            a.append('%20')
        else:
            a.append(c)
    return ''.join(a)

if __name__ == "__main__":
    print(urlify("A big brown fox jumped over a lazy dog"))
    print(urlify1("A big brown fox jumped over a lazy dog"))
