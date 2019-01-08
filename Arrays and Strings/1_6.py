def string_total_compression(s):
    d = {}
    for i in range(0, len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1

    st = ''
    for key in d:
        st += key + str(d[key])

    return(st)

def string_compression(s):

    current = '1'
    count = 0
    res = ''
    for i in range(0, len(s)):
        if s[i] != current:
            res += current + str(count)
            current = s[i]
            count = 1
        elif s[i] == current:
            count += 1
            if(i == len(s) - 1):
                res += current + str(count)
        else:
            pass
    return(res[2:])






if __name__ == "__main__":
    print(string_compression("aaaabbcccaannnn"))
