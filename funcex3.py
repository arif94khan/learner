def tax(amount):
   if amount <= 240:
      return 0
   elif amount > 240 and amount <= 480:
        return amount * .15
   else:
        return amount * .28

def netpay(grosspay):
    return grosspay - tax(grosspay)
print("Enter gross pay:")
gp = int (raw_input())
print("Net pay is" + str (netpay(gp)))
