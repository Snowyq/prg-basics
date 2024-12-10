class Phone():
  def __init__(self, producent, model, screen):
    self.producent = producent
    self.model = model
    self.screen = screen
    self.is_on = False
  
  def turn_on(self):
    self.is_on = True
  
  def turn_of(self):
    self.is_on = False
  
  def call(self, number):
    print('calling', number)

  