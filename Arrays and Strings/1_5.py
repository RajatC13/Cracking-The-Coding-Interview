def main(s1, s2):

    if(len(s1) == len(s2)):
        return(one_replace(s1, s2))
    elif (len(s1) + 1 == len(s2)):
        return(one_insert(s1, s2))
    elif (len(s1) - 1 == len(s2)):
        return(one_insert(s2, s1))
    else:
        return('Flase')

def one_replace(s1, s2):
    flag = False
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if flag:
                return('Flase')
            flag = True
    return('True')

def one_insert(s1, s2):
    i = 0
    j = 0
    while(i < len(s1) and j < len(s2)):
        if s1[i] != s2[j]:
            if(i != j):
                return('False')
            j += 1
        else:
            i += 1
            j += 1
    return('True')


if __name__ == "__main__":
    print(main("assit", "assign"))
