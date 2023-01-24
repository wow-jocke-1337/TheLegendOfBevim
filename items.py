from Classes import*


class Greatsword():
   def __init__(self,name,klass,str_mod,dex_mod,int_mod):
       self.name = name 
       self.klass = klass
       self.str_mod = str_mod
       self.dex_mod = dex_mod
       self.int_mod = int_mod
   
   def __repr__(self):
       return f"{self.name} ({self.klass})"


class Axe():
   def __init__(self,name,klass,str_mod,dex_mod,int_mod):
       self.name = name 
       self.klass = klass
       self.str_mod = str_mod
       self.dex_mod = dex_mod
       self.int_mod = int_mod
   
   def __repr__(self):
       return f"{self.name} ({self.klass})"

class Bow():
   def __init__(self,name,klass,str_mod,dex_mod,int_mod):
       self.name = name 
       self.klass = klass
       self.str_mod = str_mod
       self.dex_mod = dex_mod
       self.int_mod = int_mod
   
   def __repr__(self):
       return f"{self.name} ({self.klass})"

class Magical_Staff():
   def __init__(self,name,klass,str_mod,dex_mod,int_mod):
       self.name = name 
       self.klass = klass
       self.str_mod = str_mod
       self.dex_mod = dex_mod
       self.int_mod = int_mod
   
   def __repr__(self):
       return f"{self.name} ({self.klass})"


class Healing_potion():
    def __init__(self,name,klass):
        self.name = name
        self.klass = klass
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"


class Mana_potion():
    def __init__(self,name,klass) -> None:
        self.name = name
        self.klass = klass
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"


class Arrows():
    def __init__(self,name,klass,amount):
        self.name = name
        self.klass = klass
        self.amount = amount

    def __repr__(self):
        return f"{self.name} ({self.klass}({self.amount}))"