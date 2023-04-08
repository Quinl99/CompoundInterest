N = int(input("Enter Inital Deposit: "))
rate= float(input("Enter APY: "))
yr = int(input("Enter period of years: "))
n = int(input("Periods per year: "))
cal = N * (((1 + ((rate/100.0)/n)) ** (n*yr)))
amtmade = (cal- N)


print ("The Calculated amount:", ("%.2f" % cal), "based on", yr,"years")
print("Total earnings: ", ("%.2f" % amtmade))