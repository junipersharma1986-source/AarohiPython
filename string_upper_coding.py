class IOString():
   def  _init_(self):
      self.strl= ""
   def get_string(self):
      self.strl=input("enter string:")
   def  print_string(self):
      print("result is: ",self.strl.upper())
strl=IOString() 
strl.get_string()
strl.print_string()
    