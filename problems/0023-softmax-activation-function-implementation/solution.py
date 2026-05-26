import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    m=[]
    e=[0]*len(scores)
    t=False
    sum=0
    max=-10000
    j=0
    for i in range(len(scores)):
        if(scores[i]<1000):
            g=math.e**scores[i]
            m.append(g)
            sum+=g
        else:
            if(scores[i]>max):
                max=scores[i]
                j=i
            t=True
    d=[]
    if(t==True):
        e[j]=1.0
        return e
    else:
        for i in range(len(scores)):
            d.append(m[i]/sum)
        return d
    pass