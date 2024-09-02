def linearEquationTwo(array1,array2):
    a,b,c,d,e,f = array1[0],array1[1],array1[2],array2[0],array2[1],array2[2]
    try:
        #formula to find y and x, derived mathematically
        y = ((a*f)-(d*c))/((a*e)-(d*b))
        x = (c-(b*y))/a
        
        #format float to 3 decimal points
        y = "{:.3f}".format(y)
        x = "{:.3f}".format(x)

        return x,y
    except ZeroDivisionError:
        return "Inconsistent System or Dependant System"