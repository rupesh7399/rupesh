basic = 1500
bonus = 200
commision = 0.02
numberof = int(input("Enter the number of inputs sold:"))
price = float(input("Enter a total prices:"))

tbonus = (bonus * numberof)
comm = (commision * numberof * price)
print("Bonus        = %6.2f" % tbonus)
print("Commision    = %6.2f" % comm)
print("Gross salary = %6.2f" % (basic + tbonus + comm))
