from .base import Base

class Derived(Base):
    def __init__(self, id=None, name=None):
        super().__init__(id)
        self.name = name

instance1 = Derived()
instance2 = Derived()
print(instance1.id)
print(instance2.id)