import math
class Area:
    def Display(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+                     welcome to area unit of meter                           +")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while True:
            print("0. if you interset to exit press 0")
            print("1.square_meter_to_square_kilometer")
            print("2.square_meter_to_square_mile")
            print("3.square_meter_to_square_yard")
            print("4.square_meter_to_square_foot")
            print("5.square_meter_to_square_inch")
            print("6.square_meter_to_hectare")
            print("7.square_meter_to_Acre")
            user_choice=int(input("Enter your choice:"))
            if user_choice!=0:
                converting_value=float(input("Enter the value to convert:"))
                SM=SquareMeter_to_change_value(converting_value)
            if user_choice==1:
                result=SM.square_meter_to_square_kilometer()
                print("result:",result)
            elif user_choice==2:
                result=SM.square_meter_to_square_mile()
                print("Result:",result)
            elif user_choice==3:
                result=SM.square_meter_to_square_yard()
                print("Result:",result)
            elif user_choice==4:
                result=SM.square_meter_to_square_foot()
                print("Result",result)
            elif user_choice==5:
                result=SM.square_meter_to_square_inch()
                print("Result:",result)
            elif user_choice==6:
                result=SM.square_meter_to_hectare()
                print("Result:",result)
            elif user_choice==7:
                result=SM.square_meter_to_acre()
                print("Result:",result)
            elif user_choice==0:
                print("****************************************************")
                print("*                Thank You                         *")
                print("****************************************************")
                break
            else:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$                 You Enter Wrong choice             $")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
class SquareMeter_to_change_value(Area):
    def __init__(self,value):
        self.value=value
    def square_meter_to_square_kilometer(self):
        result=self.value/4047
        result=f"{result:.2f}"
        return result
    def square_meter_to_square_mile(self):
        result=self.value/2.59*math.e+6
        result=f"{result:.2f}"
        return result
    def square_meter_to_square_yard(self):
        result=self.value*1.196
        result=f"{result:.2f}"
        return result
    def square_meter_to_square_foot(self):
        result=self.value*10.764
        return result
    def square_meter_to_square_inch(self):
        result=self.value*1550
        return result
    def square_meter_to_hectare(self):
        result=self.value/10000
        result=f"{result:.2f}"
        return result
    def square_meter_to_acre(self):
        result=self.value/4047
        result=f"{result:.2f}"
        return result
