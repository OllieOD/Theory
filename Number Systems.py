import time 
def BruteForce(n):
    start = time.time()
    total = 0
    for i in range(n+1):
        total = total + i
    print(total)
    end = time.time()
    print((end-start)*1000)


def Formula(n):
    start =time.time()
    total = (n*(n+1))/ 2
    print(total)
    end = time.time()
    print((end-start)*1000 )


def Pi(n):
    total = 0 
    for i in range(n+1):
        c =2
        if ((i+1)%2) == 0:
            total = 3+ (4/ (c)*(c+1)*(c+2))
        else:
            total = total - (4/ (c)*(c+1)*(c+2))
        c= c+3
    print(total)
            
Pi(10403098989)
        
            

    
        