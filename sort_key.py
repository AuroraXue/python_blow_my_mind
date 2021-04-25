#https://www.hackerrank.com/challenges/most-commons/problem

if __name__ == '__main__':
    s = input()
    dt = {}
    for i in s:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1

    ls_rt = sorted(dt, key = lambda c: (-dt[c], c))[:3] ## check the key and lambda function!
    for i in ls_rt:
        print(i, dt[i])
