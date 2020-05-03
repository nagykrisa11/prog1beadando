def reverse(n):
    d=0
    rev=0
    while(n>0):
        d=n%10
        n=int(n/10)
        rev = rev * 10 + d
    return rev

x = input('Enter two numbers: ')
inp1 = x.split(',')
f = reverse(int(inp1[0]))
s = reverse(int(inp1[1]))
ossz = f + s
fordOssz = reverse(ossz)
print('Forditott = {},{} Osszeg = {} ForditottOsszeg = {}'.format(f,s,ossz,fordOssz))
