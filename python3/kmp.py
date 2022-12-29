def find_pattern(l: str, p: str) -> int:
    c = 0
    for li, _ in enumerate(l[:len(l) - len(p) + 1]):
        for pi, _ in enumerate(p):
            if l[li + pi] != p[pi]:
                break
            if pi == len(p) - 1:
                c += 1

    return c


# https://www.youtube.com/watch?v=JoF0Z7nVSrA
def kmp(l: str, p: str) -> int:
    lps = [0] * len(p) # Longest prefix-suffix
    pvlps, i = 0, 1
    while i < len(p):
        if p[i] == p[pvlps]:
            lps[i] = pvlps + 1
            pvlps += 1
            i += 1
        elif pvlps == 0:
            lps[i] = 0
            i += 1
        else:
            pvlps = lps[pvlps - 1]

    c = 0
    li, pi = 0, 0
    while li < len(l):
        if l[li] == l[pi]:
            li, pi = li + 1, pi + 1
        elif pi == 0:
            li += 1
        else:
            pi = lps[pi - 1]

        if pi == len(p) - 1:
            c += 1

    return c


l, p = "AAAXAAAAX", "AAAA"
l, p = "HelloHelloHello", "Hello"
print(find_pattern(l, p))
print(kmp(l, p))

