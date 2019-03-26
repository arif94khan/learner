balance=5000
rate=1.02
year=1
while year<=10:
    balance=balance*rate
    print("Year:" +str(year) + ":" + str(balance))
    year=year+1
