cases = int(input())
def find_coin(a,b):
    for i in range(len(b)):
        mean=(sum(b[i])/len(b[i]))
        if (mean in b[i]):
            print(b[i].index(mean)+1)
        else:
            print("Impossible")
b=[]
for i in range(cases):
    a = int(input())
    data_set = list(map(int, input().split()))
    b.append(data_set)
find_coin(a,b)
