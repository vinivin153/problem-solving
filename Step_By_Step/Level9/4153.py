while True:
    s = list(map(int, input().split()))
    if sum(s) == 0:
        break
    else:
        s.sort()
        if s[0] ** 2 + s[1] ** 2 == s[2] ** 2:
            print("right")
        else:
            print("wrong")

# while True:
#     s = list(map(int, input().split()))
#     if sum(s) == 0:
#         break
#     else:
#         z = max(s)
#         s.remove(z)
#         y = min(s)
#         s.remove(y)
#         x = s[0]
#         if x ** 2 + y ** 2 == z ** 2:
#             print("right")
#         else:
#             print("wrong")