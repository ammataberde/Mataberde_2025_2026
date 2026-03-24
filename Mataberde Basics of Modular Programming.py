speed = float(input("Input Average Speed (km/h): "))
time = 42.195/speed
hours = int(time)
minutes = int((time - hours) * 60)



print ("At" , speed, "km/h it will take" , hours, "hours and" , minutes, "minutes to finish the marathon")
