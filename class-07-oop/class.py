#OOP
class Car:
  def __init__(self, brand, model, year, fipe, offer):
    self.brand = brand
    self.model = model
    self.year = year
    self.fipe = fipe
    self.offer = offer

  def info(self):
    return (self.brand, self.model, self.year)
  
  def sale(self):
    if self.offer >= self.fipe:
      return "Carro vendido!"
    else:
      return "Nem a pau juvenal!"
  
myCar = Car("Toyota", "Sw4", "2024", "38000", "37000")
myCar2 = Car("Chevrolet", "Celta", "2000", "2000", "20001")

# print(myCar.brand)
print(myCar2.info())
print(myCar2.sale())

