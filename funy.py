def rever(v):
    
    reve=""
    for char in v :
        reve = char + reve
    return(reve)

k=input("enter string:") 
print(rever(k))  

