def is_unique(s):
    string = s
    a = []
    for s in string:
        if s not in a:
            a.append(s)
        else:
            return('False')
    return('True')

if __name__ == "__main__":
    print(is_unique('Nirbhay'))
