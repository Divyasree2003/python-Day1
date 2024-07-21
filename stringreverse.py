


def check(s):
    rev=' '
    for i in s:
        rev=i+rev
    return rev
s='sri devi is engineering college'
print("reverse of string is:",check(s))
# OR#
def check(s):
    s=s.split()
    s=list(reversed(s))
    print(s)
    for i in s:
        rev=i[::-1]
        
    return rev

s='sri devi is engineering college'
print("reverse of string is:",check(s))
