def prime(n):
    flag = 0
    if n < 2:
        flag = 0
    if n == 2:
        flag = 1
    for i in range(2, int(n/2)):
#         print i
#         print n
        if n%i == 0:
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    for j in range(100):
        pri = prime(j)
        print j, pri
        print '*'*78
    print pri