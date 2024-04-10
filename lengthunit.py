import math
class Length:
    def Display(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+                     welcome to length unit of meter                         la sal+")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while True:
            print("0.If you Interset to exit press 100")
            print("*********************************This unit of meter*****************************************************")
            print("1.Meter to Centimeter")
            print("2.Meter to kilometer")
            print("3.meter to millymeter")
            print("4.Meter to micrometer")
            print("5.meter to nanometer")
            print("6.meter to mile")
            print("7,meter to Yard")
            print("8.meter to foot")
            print("9.meter to Inch")
            print("10.meter to nautical mile")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!This is unit oh Kilometer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("11.kiloMeter to Centimeter")
            print("12.kilometer to kilometer")
            print("13.kilometer to millymeter")
            print("14.kilometer to micrometer")
            print("15.kilometer to nanometer")
            print("16.kilometer to mile")
            print("17.kilometer to Yard")
            print("18.kilometer to foot")
            print("19.kilometer to Inch")
            print("20.kilometer to nautical mile")
            print("@@@@@@@@@@@@This is unit of Centimeter@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("21.CentiMeter to meter")
            print("22.Centimeter to kilometer")
            print("23.Centimeter to millymeter")
            print("24.Centimeter to micrometer")
            print("25.Centimeter to nanometer")
            print("26.Centimeter to mile")
            print("27.Centimeter to Yard")
            print("28.Centimeter to foot")
            print("29.Centimeter to Inch")
            print("30.Centimeter to nautical mile")
            print("@@@@@@@@@@@@This is unit of Millimeter@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("31.MilliMeter to meter")
            print("32.Millimeter to kilometer")
            print("33.Millimeter to centimeter")
            print("34.Millimeter to micrometer")
            print("35.Millimeter to nanometer")
            print("36.Millimeter to mile")
            print("37.Millimeter to Yard")
            print("38.Millimeter to foot")
            print("39.Millimeter to Inch")
            print("40.Millimeter to nautical mile")
            print("@@@@@@@@@@@@This is unit of Micrometer@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("41.micrometer to meter")
            print("42.micrometer to kilometer")
            print("43.micrometer to centimeter")
            print("44.micrometer to millimeter")
            print("45.micrometer to nanometer")
            print("46.micrometer to mile")
            print("47.micrometer to Yard")
            print("48.micrometer to foot")
            print("49.micrometer to Inch")
            print("50.micrometer to nautical mile")
            print("@@@@@@@@@@@@This is unit of Nanometer@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("51.nanometer to meter")
            print("52.nanometer to kilometer")
            print("53.nanometer to centimeter")
            print("54.nanometer to micrometer")
            print("55.nanometer to millimeter")
            print("56.nanometer to mile")
            print("57.nanometer to Yard")
            print("58.nanometer to foot")
            print("59.nanometer to Inch")
            print("60.nanometer to nautical mile")
            print("@@@@@@@@@@@@This is unit of Mile@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("51.mile to meter")
            print("52.mile to kilometer")
            print("53.mile to centimeter")
            print("54.mile to micrometer")
            print("55.mile to nanometer")
            print("56.mile to millimeter")
            print("57.mile to Yard")
            print("58.mile to foot")
            print("59.mile to Inch")
            print("60.mile to nautical mile")
            user_choice=int(input("Enter your choice:"))
            if user_choice!=0:
                changing_value = float(input("enter the valu:"))
                M=Meter_To_change_unit(changing_value)
                N=Kilometer_to_change_vale(changing_value)
                C=Centimeter_to_change_vale(changing_value)
                MI=Millimeter_to_change_vale(changing_value)
                MIC=Micrometer_to_change_vale(changing_value)
                Nano=Nanometer_to_change_vale(changing_value)
                MIL=Mile_to_change_vale(changing_value)
            if user_choice==1:
               result=M.meter_to_centimeter()
               print("Answer of given value:",result)
            elif user_choice==2:
                result=M.meter_to_kilometer()
                print("Answer of given value:",result)
            elif user_choice==3:
                result=M.meter_to_millymeter()
                print("Answer of given value:",result)
            elif user_choice==4:
                result=M.meter_to_micrometer()
                print("Answer of given value:",result)
            elif user_choice==5:
                result=M.meter_to_nanometer()
                print("Answer of given value:",result)
            elif user_choice==6:
                result=M.meter_to_mile()
                print("Answer of given value:",result)
            elif user_choice==7:
                result=M.meter_to_yard()
                print("Answer of given value:",result)
            elif user_choice==8:
                result=M.meter_to_foot()
                print("Answer of given value:",result)
            elif user_choice==9:
                result=M.meter_to_inch()
                print("Answer of given value:",result)
            elif user_choice==10:
                result=M.meter_to_nautical_mile()
                print("Answer of given value:",result)
            if user_choice==11:
               result=N.kilometer_to_meter()
               print("Answer of given value:",result)
            elif user_choice==12:
                result=N.kilometer_to_centimeter()
                print("Answer of given value:",result)
            elif user_choice==13:
                result=N.kilometer_to_millymeter()
                print("Answer of given value:",result)
            elif user_choice==14:
                result=N.kilometer_to_micrometer()
                print("Answer of given value:",result)
            elif user_choice==15:
                result=N.kilometer_to_nanometer()
                print("Answer of given value:",result)
            elif user_choice==16:
                result=N.kilometer_to_mile()
                print("Answer of given value:",result)
            elif user_choice==17:
                result=N.kilometer_to_yard()
                print("Answer of given value:",result)
            elif user_choice==18:
                result=N.kilometer_to_foot()
                print("Answer of given value:",result)
            elif user_choice==19:
                result=N.kilometer_to_inch()
                print("Answer of given value:",result)
            elif user_choice==20:
                result=N.kilometer_to_nautical_mile()
                print("Answer of given value:",result)
            elif user_choice==21:
               result=C.centimeter_to_kilometer()
               print("Answer of given value:",result)
            elif user_choice==22:
                result=C.centimeter_to_meter()
                print("Answer of given value:",result)
            elif user_choice==23:
                result=C.centimeter_to_millymeter()
                print("Answer of given value:",result)
            elif user_choice==24:
                result=C.centimeter_to_micrometer()
                print("Answer of given value:",result)
            elif user_choice==25:
                result=C.centimeter_to_nanometer()
                print("Answer of given value:",result)
            elif user_choice==26:
                result=C.centimeter_to_mile()
                print("Answer of given value:",result)
            elif user_choice==27:
                result=C.centimeter_to_yard()
                print("Answer of given value:",result)
            elif user_choice==28:
                result=C.centimeter_to_foot()
                print("Answer of given value:",result)
            elif user_choice==29:
                result=C.centimeter_to_inch()
                print("Answer of given value:",result)
            elif user_choice==30:
                result=C.centimeter_to_nautical_mile()
                print("Answer of given value:",result)
            elif user_choice==31:
               result=MI.millimeter_to_kilometer()
               print("Answer of given value:",result)
            elif user_choice==32:
                result=MI.millimeter_to_meter()
                print("Answer of given value:",result)
            elif user_choice==33:
                result=MI.millimeter_to_centimeter()
                print("Answer of given value:",result)
            elif user_choice==34:
                result=MI.millimeter_to_micrometer()
                print("Answer of given value:",result)
            elif user_choice==35:
                result=MI.millimeter_to_nanometer()
                print("Answer of given value:",result)
            elif user_choice==36:
                result=MI.millimeter_to_mile()
                print("Answer of given value:",result)
            elif user_choice==37:
                result=MI.millimeter_to_yard()
                print("Answer of given value:",result)
            elif user_choice==38:
                result=MI.millimeter_to_foot()
                print("Answer of given value:",result)
            elif user_choice==39:
                result=MI.millimeter_to_inch()
                print("Answer of given value:",result)
            elif user_choice==40:
                result=MI.millimeter_to_nautical_mile()
                print("Answer of given value:",result)
            elif user_choice==41:
               result=MIC.micrometer_to_kilometer()
               print("Answer of given value:",result)
            elif user_choice==42:
                result=MIC.micrometer_to_meter()
                print("Answer of given value:",result)
            elif user_choice==43:
                result=MIC.micrometer_to_centimeter()
                print("Answer of given value:",result)
            elif user_choice==44:
                result=MIC.micrometer_to_millimeter()
                print("Answer of given value:",result)
            elif user_choice==45:
                result=MIC.micrometer_to_nanometer()
                print("Answer of given value:",result)
            elif user_choice==46:
                result=MIC.micrometer_to_mile()
                print("Answer of given value:",result)
            elif user_choice==47:
                result=MIC.micrometer_to_yard()
                print("Answer of given value:",result)
            elif user_choice==48:
                result=MIC.micrometer_to_foot()
                print("Answer of given value:",result)
            elif user_choice==49:
                result=MIC.micrometer_to_inch()
                print("Answer of given value:",result)
            elif user_choice==50:
                result=MIC.micrometer_to_nautical_mile()
                print("Answer of given value:",result)
            elif user_choice==51:
               result=Nano.nanometer_to_kilometer()
               print("Answer of given value:",result)
            elif user_choice==52:
                result=Nano.nanometer_to_meter()
                print("Answer of given value:",result)
            elif user_choice==53:
                result=Nano.nanometer_to_centimeter()
                print("Answer of given value:",result)
            elif user_choice==54:
                result=Nano.nanometer_to_millimeter()
                print("Answer of given value:",result)
            elif user_choice==55:
                result=Nano.nanometer_to_micrometer()
                print("Answer of given value:",result)
            elif user_choice==56:
                result=Nano.nanometer_to_mile()
                print("Answer of given value:",result)
            elif user_choice==57:
                result=Nano.nanometer_to_yard()
                print("Answer of given value:",result)
            elif user_choice==58:
                result=Nano.nanometer_to_foot()
                print("Answer of given value:",result)
            elif user_choice==59:
                result=Nano.nanometer_to_inch()
                print("Answer of given value:",result)
            elif user_choice==60:
                result=Nano.nanometer_to_nautical_mile()
                print("Answer of given value:",result)
            elif user_choice==61:
               result=MIL.mile_to_kilometer()
               print("Answer of given value:",result)
            elif user_choice==62:
                result=MIL.mile_to_meter()
                print("Answer of given value:",result)
            elif user_choice==63:
                result=MIL.mile_to_centimeter()
                print("Answer of given value:",result)
            elif user_choice==64:
                result=MIL.mile_to_millimeter()
                print("Answer of given value:",result)
            elif user_choice==65:
                result=MIL.mile_to_micrometer()
                print("Answer of given value:",result)
            elif user_choice==66:
                result=MIL.mile_to_nanometer()
                print("Answer of given value:",result)
            elif user_choice==67:
                result=MIL.mile_to_yard()
                print("Answer of given value:",result)
            elif user_choice==68:
                result=MIL.mile_to_foot()
                print("Answer of given value:",result)
            elif user_choice==69:
                result=MIL.mile_to_inch()
                print("Answer of given value:",result)
            elif user_choice==70:
                result=MIL.mile_to_nautical_mile()
                print("Answer of given value:",result)
            elif user_choice==0:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^                  Thanks for visiting my unit converter                         ^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                break
            else:
                if user_choice>100:
                    print("##################################################################################")
                    print("#                   you enter wrong choice                                       #")
                    print("##################################################################################")
class Meter_To_change_unit(Length):
    def __init__(self,value):
        self.value=value
    def meter_to_centimeter(self):
        result_value=self.value*100
        return result_value
    def meter_to_kilometer(self):
        result_value=self.value//1000
        return result_value
    def meter_to_millymeter(self):
        result_value=self.value*1000
        return result_value
    def meter_to_micrometer(self):
        result_value=self.value*math.e+6
        result_value=f"{result_value:.2f}"
        return result_value
    def meter_to_nanometer(self):
        result_value=self.value*math.e+9
        result_value=f"{result_value:.2f}"
        return result_value
    def meter_to_mile(self):
        result_value=self.value//1609
        return result_value
    def meter_to_yard(self):
        result_value=self.value*1.094
        result_value=f"{result_value:.2f}"
        return result_value
    def meter_to_foot(self):
        result_value=self.value*3.281
        return result_value
    def meter_to_inch(self):
        result_value=self.value*39.37
        return result_value
    def meter_to_nautical_mile(self):
        result_value=self.value//1852
        return result_value
class Kilometer_to_change_vale(Meter_To_change_unit,Length):
    def __init__(self,value):
        self.value=value
    def kilometer_to_centimeter(self):
        result_value=self.value*100000
        return result_value
    def kilometer_to_meter(self):
        result_value=self.value*1000
        return result_value
    def kilometer_to_millymeter(self):
        result_value=self.value*math.e+6
        result_value=f"{result_value:.2f}"
        return result_value
    def kilometer_to_micrometer(self):
        result_value=self.value*math.e+9
        result_value=f"{result_value:.2f}"
        return result_value
    def kilometer_to_nanometer(self):
        result_value=self.value*math.e+12
        result_value=f"{result_value:.2f}"
        return result_value
    def kilometer_to_mile(self):
        result_value=self.value/1.609
        result_value=f"{result_value:.2f}"
        return result_value
    def kilometer_to_yard(self):
        result_value=self.value*1094
        return result_value
    def kilometer_to_foot(self):
        result_value=self.value*3281
        return result_value
    def kilometer_to_inch(self):
        result_value=self.value*39370
        return result_value
    def kilometer_to_nautical_mile(self):
        result_value=self.value//1.852
        result_value=f"{result_value:.2f}"
        return result_value
class Centimeter_to_change_vale(Meter_To_change_unit, Length):
        def __init__(self, value):
            self.value = value

        def centimeter_to_meter(self):
            result_value = self.value / 100
            return result_value

        def centimeter_to_kilometer(self):
            result_value = self.value / 100000
            return result_value

        def centimeter_to_millymeter(self):
            result_value = self.value * 10
            return result_value

        def centimeter_to_micrometer(self):
            result_value = self.value * 100000
            return result_value

        def centimeter_to_nanometer(self):
            result_value = self.value * math.e + 7
            result_value = f"{result_value:.2f}"
            return result_value

        def centimeter_to_mile(self):
            result_value = self.value / 160900
            result_value = f"{result_value:.2f}"
            return result_value

        def centimeter_to_yard(self):
            result_value = self.value / 91.44
            return result_value

        def centimeter_to_foot(self):
            result_value = self.value /30.48
            return result_value

        def centimeter_to_inch(self):
            result_value = self.value / 2.54
            return result_value

        def centimeter_to_nautical_mile(self):
            result_value = self.value / 185200
            result_value = f"{result_value:.2f}"
            return result_value


class Millimeter_to_change_vale(Meter_To_change_unit, Length):
    def __init__(self, value):
        self.value = value

    def millimeter_to_meter(self):
        result_value = self.value / 1000
        return result_value

    def millimeter_to_kilometer(self):
        result_value = self.value*math.e+6
        result_value=f"{result_value:.2f}"
        return result_value

    def millimeter_to_centimeter(self):
        result_value = self.value / 10
        return result_value

    def millimeter_to_micrometer(self):
        result_value = self.value * 1000
        return result_value

    def millimeter_to_nanometer(self):
        result_value = self.value * math.e + 6
        result_value = f"{result_value:.2f}"
        return result_value

    def millimeter_to_mile(self):
        result_value = self.value / 1.609*math.e+6
        result_value = f"{result_value:.2f}"
        return result_value

    def millimeter_to_yard(self):
        result_value = self.value / 914.4
        return result_value

    def millimeter_to_foot(self):
        result_value = self.value / 304.8
        return result_value

    def millimeter_to_inch(self):
        result_value = self.value / 25.4
        return result_value

    def millimeter_to_nautical_mile(self):
        result_value = self.value / 1.852*math.e+6
        result_value = f"{result_value:.2f}"
        return result_value
class Micrometer_to_change_vale(Meter_To_change_unit, Length):
    def __init__(self, value):
        self.value = value

    def micrometer_to_meter(self):
        result_value = self.value / math.e+6
        result_value=f"{result_value:.2f}"
        return result_value

    def micrometer_to_kilometer(self):
        result_value = self.value/math.e+9
        result_value=f"{result_value:.2f}"
        return result_value

    def micrometer_to_centimeter(self):
        result_value = self.value / 10000
        return result_value

    def micrometer_to_millimeter(self):
        result_value = self.value / 1000
        return result_value

    def micrometer_to_nanometer(self):
        result_value = self.value * 1000
        return result_value

    def micrometer_to_mile(self):
        result_value = self.value / 1.609*math.e+9
        result_value = f"{result_value:.2f}"
        return result_value

    def micrometer_to_yard(self):
        result_value = self.value / 914400
        result_value=f"{result_value:.2f}"
        return result_value

    def micrometer_to_foot(self):
        result_value = self.value / 304800
        result_value=f"{result_value:.2f}"
        return result_value

    def micrometer_to_inch(self):
        result_value = self.value / 25400
        result_value= f"{result_value:.2f}"
        return result_value

    def micrometer_to_nautical_mile(self):
        result_value = self.value / 1.852*math.e+9
        result_value = f"{result_value:.2f}"
        return result_value
class Nanometer_to_change_vale(Meter_To_change_unit, Length):
    def __init__(self, value):
        self.value = value

    def nanometer_to_meter(self):
        result_value = self.value / math.e+9
        result_value=f"{result_value:.2f}"
        return result_value

    def nanometer_to_kilometer(self):
        result_value = self.value/math.e+12
        result_value=f"{result_value:.2f}"
        return result_value

    def nanometer_to_centimeter(self):
        result_value = self.value / math.e+7
        result_value=f"{result_value:.2f}"
        return result_value

    def nanometer_to_millimeter(self):
        result_value = self.value / math.e +6
        result_value=f"{result_value:.2f}"
        return result_value

    def nanometer_to_micrometer(self):
        result_value = self.value / 1000
        result_value=f"{result_value:.2f}"
        return result_value

    def nanometer_to_mile(self):
        result_value = self.value / 1.609*math.e+12
        result_value = f"{result_value:.2f}"
        return result_value

    def nanometer_to_yard(self):
        result_value = self.value / 9.144*math.e+8
        result_value=f"{result_value:.2f}"
        return result_value

    def nanometer_to_foot(self):
        result_value = self.value / 3.048*math.e+8
        result_value=f"{result_value:.2f}"
        return result_value

    def nanometer_to_inch(self):
        result_value = self.value / 2.54*math.e+7
        result_value= f"{result_value:.2f}"
        return result_value

    def nanometer_to_nautical_mile(self):
        result_value = self.value / 1.852*math.e+12
        result_value = f"{result_value:.2f}"
        return result_value
class Mile_to_change_vale(Meter_To_change_unit, Length):
    def __init__(self, value):
        self.value = value

    def mile_to_meter(self):
        result_value = self.value *1609
        result_value=f"{result_value:.2f}"
        return result_value

    def mile_to_kilometer(self):
        result_value = self.value*1.609
        return result_value

    def mile_to_centimeter(self):
        result_value = self.value * 160900
        return result_value

    def mile_to_millimeter(self):
        result_value = self.value * 1.609* math.e +6
        result_value=f"{result_value:.2f}"
        return result_value

    def mile_to_micrometer(self):
        result_value = self.value * 1.609*math.e+9
        result_value=f"{result_value:.2f}"
        return result_value

    def mile_to_nanometer(self):
        result_value = self.value / 1.609*math.e+12
        result_value = f"{result_value:.2f}"
        return result_value

    def mile_to_yard(self):
        result_value = self.value * 1760
        return result_value

    def mile_to_foot(self):
        result_value = self.value * 5280
        return result_value

    def mile_to_inch(self):
        result_value = self.value * 63360
        return result_value

    def mile_to_nautical_mile(self):
        result_value = self.value / 1.151
        result_value = f"{result_value:.2f}"
        return result_value