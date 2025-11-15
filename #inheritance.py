# inheritance
class parent():
  def function(self):
    print("i am good")
class child(parent):
  def function(self):
    print("i am bad")
obj=parent()
obj.function()
