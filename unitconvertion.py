from lengthunit import Length
from area import Area
if __name__=="__main__":
    print("-------------------------------------------------------------------------------")
    print("|                 welcome to unit converter                                   |")
    print("_______________________________________________________________________________")
    while True:
        print("1.Length")
        print("2.Area")
        print("3.Data transfer Rate")
        print("4.Digital Storage")
        print("5.Energy")
        print("6.Frequancy")
        print("7.Fuel Economy")
        print("8.Mass")
        print("9.plane Angel")
        print("10.presure")
        print("11.speed")
        print("12.Temparature")
        print("13.Time")
        print("14.Volume")
        user=int(input("Enter your choice:"))
        if user==1:
            lenth=Length()
            lenth.Display()
        elif user==2:
            area=Area()
            area.Display()
        elif user==0:
            print("::::::::::::::::::::::::::::::::::::::::::::::::")
            print(":            Thank You                         :")
            print("::::::::::::::::::::::::::::::::::::::::::::::::")
            break
        else:
            print("Enter user choice is wrong")
