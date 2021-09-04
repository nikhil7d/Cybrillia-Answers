def isPal(s):
    return s == s[::-1]

str=input()
ans = isPal(str)
 
if ans:
    print("True")
else:
    print("False")