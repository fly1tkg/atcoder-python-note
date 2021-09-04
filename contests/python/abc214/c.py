N = int(input())

S = list(map(int, input().split()))
T = list(map(int, input().split()))

receive_times = {}
pass_times = {}

for i in range(N):
  if T[i]-1 in receive_times:
    receive_times[T[i]-1].append((i, S[i],))
  else:
    receive_times[T[i]-1] = [(i, S[i],)]


state = [False] * N
ansset = [False] * N
ans = [10 ** 9] * N

for t in range((10 ** 9) +1):
  # print(t, receive_times[t])
  if t in receive_times:
    for s, pass_time in receive_times[t]:
      state[s] = True
      ansset[s] = True
      ans[s] = min(ans[s], t)
      if pass_time+t in pass_times:
        pass_times[pass_time+t].append(s)
      else:
        pass_times[pass_time+t] = [s]
  
  if t in pass_times:
    for p in pass_times[t]:
      # print(t, p)
      state[p] = False
      if p == N - 1:
        state[0] = True
        ansset[0] = True
        ans[0] = min(ans[0], t)
        if S[0]+t in pass_times:
          pass_times[S[0]+t].append(0)
        else:
          pass_times[S[0]+t] = [0]
      else:
        state[p+1] = True
        ansset[p+1] = True
        ans[p+1] = min(ans[p+1], t)
        if S[p+1]+t in pass_times:
          pass_times[S[p+1]+t].append(p+1)
        else:
          pass_times[S[p+1]+t] = [p+1]
  
  if all(ansset):
    break

for a in ans:
  print(a+1)
  

