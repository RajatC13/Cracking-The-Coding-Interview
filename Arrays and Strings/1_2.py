def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return('False')

    sa = s1.split().sort()
    sb = s2.split().sort()

    return(sa == sb)

if __name__ == "__main__":
    print(check_permutation("assign", "ssgain"))
