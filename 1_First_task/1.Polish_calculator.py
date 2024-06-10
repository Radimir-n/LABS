def ipn(postf):
    res=[]
    for k in postf:
        if k.isdigit() or (k[0]=='-' and k[1:].isdigit()): # !!! 
            res.append(int(k))
        elif k=="+":
            k2=res.pop()
            k1=res.pop()
            res.append(k1+k2)
        elif k=="-":
            k2=res.pop()
            k1=res.pop()
            res.append(k1-k2)
        elif k=="*":
            k2=res.pop()
            k1=res.pop()
            res.append(k1*k2)
        elif k=="/":
            k2=res.pop()
            k1=res.pop()
            res.append(k1//k2)
        elif k=="~":
            k2=res.pop()
            res.append(-k2)
        elif k=="#":
            k2=res.pop()
            res.append(k2)
            res.append(k2)
        elif k=="@":
            k3=res.pop()
            k2=res.pop()
            k1=res.pop()
            res.append(k2)
            res.append(k3)
            res.append(k1)
        elif k=="!":
            k1=res.pop()
            p=1
            for i in range(2,k1+1):
                p*=i
            res.append(p)
    return res[0]   
def start():
    postf=input().split(" ")
    print(ipn(postf))
start()