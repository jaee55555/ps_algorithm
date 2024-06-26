def find_word(idx, start):
    global vow
    global con

    if idx == L:
        words_list.sort()
        for i in range(L):
            if words_list[i] in nec_word:
                vow += 1
            else:
                con += 1
        if vow > 0 and con > 1:
            w = ""
            for i in range(L):
                w += words_list[i]
            print(w)
        vow = con = 0
        return

    for x in range(start, C):
        if visit[x] == 0:
            visit[x] = 1
            words_list[idx] = words[x]
            find_word(idx + 1, x)
            visit[x] = 0
    visit[start] = 1


L, C = map(int, input().split())
words = input().split()
words.sort()
words_list = [0] * L
nec_word = {"a", "e", "i", "o", "u"}
visit = [0] * C
vow = 0
con = 0

find_word(0, 0)
