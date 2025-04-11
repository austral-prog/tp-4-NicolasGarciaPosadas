def leap_year():
    year = input("Ingrese un año: ")
    year = int(year)
    if year%4 == 0 and year%400 ==0:
        print(f"El año {year} es bisiesto")
    else:print(f"El año {year} no es bisiesto")

