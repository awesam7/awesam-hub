light = input("light:")

if light.isdigit():
    print(int(light))
elif (light == "red" ):
    print("stop")
elif (light =="green"):  
    print("go")
elif (light == "yellow"):
    print("wait")

else :
    print("broken")