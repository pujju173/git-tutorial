class CalculatorObject3():

  def __init__(self, a, b):

    self.a = a
    self.b = b


  def add(self):
    sum = self.a + self.b
    print('Sum =',sum)

  def subtract(self):
    diff = self.a - self.b
    print('Difference =', diff)