# def avg(a,b,c):
#     return ((a+b+c)/3)

# print(avg(1,4,5))


# def oddev(n):
#     if (n%2==0):
#         print("even")
#     else:
#         print("odd")
#     return n
# print(oddev(5))

# lp = int(input("give number"))
# c=1
# while lp>0:
#     print(lp)
#     lp-=1

# def summ(n):
#     if n == 0 :
#         return 0
#     return n + summ(n-1) 

# print(summ(5))

# abc_list = ["sam", 2, 3]


# def funclist():
#     for i in abc_list:
#         print(i)
#     return i

# funclist()



# f = open("call.py","r")
# data = f.read()
# print(data)
# f.close()

linlist = [1,2,4,5,5,6,7,8,9,9]

for i in range (len(linlist)):
    for j in range(i+1, len(linlist)):
        if linlist[i] == linlist[j]:
            print("duplicate" + str(linlist[i]))
            break
