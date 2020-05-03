import random
import math

def isPowerOf2(n):
    return math.log(n, 2).is_integer()


def row_filling(n):
    teams = [(0, 0) for i in range(2 * n - 1)]
    p = 2
    ossz = n
    while n >= 1:
        k = p // 2 - 1
        for i in range(n):
            pos = k + p * i
            if k == 0:
                teams[pos] = (i + 1, ossz // n - 1)
            else:
                x = teams[pos - p // 4]
                x = (x[0], x[1] + 1)
                y = teams[pos + p // 4]
                y = (y[0], y[1] + 1)
                teams[pos] = x if random.randint(0, 1) == 0 else y

        p *= 2
        n //= 2

    return teams

numOfTeams = int(input("Adja meg a csapatok számát (2 hatványa): "))
while(isPowerOf2(numOfTeams) == False):
    numOfTeams = int(input("Nem 2 hatványa, adjon meg egy másik számot: "))


file = open("agrajz.txt", "w")
teams = row_filling(numOfTeams)
for i in teams:
    for j in range(i[1] * 2 - 1):
        file.write("\t")

    if i[1] == 0:
        file.write("Team{}--\n".format(i[0]))
    elif 2 ** i[1] == numOfTeams:
        file.write("|-->Team{}\n".format(i[0]))
    else:
        file.write("|-->Team{}--\n".format(i[0]))