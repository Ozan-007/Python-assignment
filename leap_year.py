year = int(input("Enter a four digit year: "))

if year % 4 == 0:
      if year % 100 == 0:
            if year % 100 == 0 and year % 400 == 0:
                  print(f"{year} is a leap year!!!")
            else:
                  print(f"{year} not a leap year")
      else:
            print(f"{year} is a leap year!!!")
else:
      print(f"{year} is not a leap year")



#https://github.com/Ozan-007/Python-assignment