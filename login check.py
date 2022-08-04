uname = []
upass = []
x = str(input("enter the username : "))
uname.append(x)
y = str(input("enter the Password : "))
upass.append(y)
print(uname)
print(upass)
print("Please enter the login credentials")
a = str(input("enter the username : "))
b = str(input("enter the Password : "))
if(a == x and b == y):
    print("** connected successful **")
    print("** Hello *Guna*/*Melson* Welcome to the star world **")
    def pypart():
        n = int(input("Enter the value for star = "))
        for i in range(0, n):
            for j in range(0, i + 1):
                print("* ", end="")
            print("\r")
    pypart()
    print("** I think your Requirement is correct ok bye... **")
else:
    print("Enter the password correct")
    print("ponga thambii poiyu veliya parungaa..!")
