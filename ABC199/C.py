N = int(input())
S = list(str(input()))
Q = int(input())

forward = S[0:N]
back = S[N:2*N]

for _ in range(Q):
    T,A,B = input().split() 

    if T == "1":
        A = int(A)-1
        B = int(B)-1

        if A < N and B < N:
            tmpA = forward[A]
            forward[A] = forward[B]
            forward[B] = tmpA
        elif A < N and B >= N:
            tmpA = forward[A]
            forward[A] = back[B-N]
            back[B-N] = tmpA
        elif A >= N and B < N:
            tmpA = back[A-N]
            back[A-N] = forward[B]
            forward[B] = tmpA
        elif A >= N and B >= N:
            tmpA = back[A-N]
            back[A-N] = back[B-N]
            back[B-N] = tmpA


    else:
        tmp = forward
        forward = back
        back = tmp


S = forward + back
S = "".join(S)

print(S)