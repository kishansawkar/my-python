#multiple inheritance
class A:
  def function(self):
    print("day 1")
class B:
  def function(self):
    print("day 2")
class C(A,B):
  def function(self):
    print("just chill")
obj=C()
obj.function()
obj=A()
obj.function()
obj=B()
obj.function()
