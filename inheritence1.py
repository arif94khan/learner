class employee:
   def __init__(self, name, payrate):
     self.name = name
     self.payrate = payrate
   def __str__(self):
      return self.name + ", " +str(self.payrate)
   def pay(self, hoursworked):
      return self.payrate * hoursworked
class manager(employee):
   def __init__(self, name, payrate, issalaried):
     employee.__init__(self, name, payrate)
     self.salaried = issalaried
   def __str__(self):
     retStr = employee.__str__(self)
     retStr += "Salaried:" + str(self.salaried)
     return retStr
   def pay(self, hoursworked):
     if self.salaried:
       return self.payrate
     else:
       return self.payrate * hoursworked

e1 = employee("John Jones", 10.00)
print(e1)
print("Gross pay:" +str(e1.pay(40)))
m1 = manager("Jane Smith", 1200, True)
print(m1)
print("Gross pay:" +str(m1.pay(40)))
m2 = manager("Jim Brown", 20.00, False)
print(m2)
print("Gross pay:" +str(m2.pay(40)))
