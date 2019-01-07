def check_permutation_pallindrome(s):
    oddflag = 0
    s.replace(' ','')
    chars = list(s)
    b = {}
    for c in chars:
        if c in b.keys():
            b[c] += 1
        else:
            b[c] = 1

    for v in list(b.values()):
        if v % 2 == 1:
            oddflag += 1

    if len(s) % 2 == 1 and oddflag == 1:
        return('True')
    elif len(s) % 2 == 0 and oddflag == 0:
        return('True')
    else:
        return('Flase')





if __name__ == "__main__":
    print(check_permutation_pallindrome("ababab"))
