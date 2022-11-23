def solution(A, K, L):
    # write your code in Python 3.8.10
    if (K+L > len(A)):
        return -1
    else:
        fin = []
        for i in range(len(A) - (K+L) + 1):
            Kval = A[i:K+i]
            for j in range(len(A) - (K+L) + 1):
                Lval = A[K+i+j:i+j+K+L]
                if len(Lval)>=L:
                    fin.append(sum(Kval) + sum(Lval))
        return (max(fin))

r = solution([1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1] , 5 , 4)
print(r)
r = solution([1, 1, 8, 8, 9, 5, 9, 2, 5, 4, 8, 1, 6, 8, 7, 2, 2, 7, 6, 2, 5, 7, 5, 9, 9, 9, 3, 8, 2, 4, 2, 3, 8, 8, 7, 4, 5, 5, 1, 1, 5, 7, 2, 5] , 6 , 8)
print(r)
r = solution([1,1,6,7,5,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9,9,9] , 5 , 4)
print(r)
