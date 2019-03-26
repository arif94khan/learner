class account:
    def __init__(self, accnumber, balnce):
        self.accnumber = accnumber
        self.balnce = balnce
    def __str__(self):
       return "Acount number:"  + str(self.accnumber) + "\n" \
              "Balance:" + str(self.balance)

    def deposit(self, amount):
        self.balance += amount


class checking(account):
  def __init__(self, accnumber, balance, fee):
      account.__init__(self, accnumber, balance)
      self.fee = fee

  def __str__(self):
      retStr = "Acount type: checking \n";
      retStr += account.__str__(self)
      return retStr

  def getfee(self):
    return self.fee

  def withdraw(self, amount):
    if amount > self.balance:
      print ("Insufficient balnce")
    else:
      self.balance = self.balance - amount - self.fee

class savings(account):
    def __init__(self, accnumber, balnce):
        account.__init__(self, accnumber, balnce)

    def __str__(self):
         retStr = "Acount type: Savings \n"
         retStr = account.__str__(self)
         return retStr

    def withdraw(self, amount):
      if amount > self.balnce:
        print("Insufficients balnce")
      else:
        self.balnce = self.balance - amount

ca = checking("123", 500, .50)
print(ca)
ca.withdraw(100)
print(ca)
ca.deposit(200)
print(ca)
sa = savings("456", 1000)
print(sa)
sa.withdraw(250)
print(sa)
sa.deposit(125)
print(sa)
accounts = [ca, sa]
print("Displaying all accounts:")
for i in range (0, len(accounts)):
    print(acounts[i])
