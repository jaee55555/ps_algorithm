import sys

T = int(sys.stdin.readline())
room = [i for i in range(15)]
apartment = [room]
for i in range(14):
    apartment.append([0 for j in range(15)])
# print(apartment)
for t in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    for k in range(1, K+1):
        temp = apartment[k-1]
        # print(temp)
        for n in range(1,N+1):
            understage = temp[1:n+1]
            # print("아랫층= ",understage)
            # print("아랫층 합= ", sum(understage))
            apartment[k][n] = sum(understage)
    # print(K,"층 ", N, "호는 ",apartment[K][N])
    print(apartment[K][N])


