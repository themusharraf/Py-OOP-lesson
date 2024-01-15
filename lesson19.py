from dataclasses import dataclass, field


@dataclass
class Xodim:
    name: str
    age: int

    emp_id: int
    city: str = field(init=False, default="Tashkent", repr=True)


obj = Xodim("Alice", 18, 4456)
obj1 = Xodim("John", 19, 4459)

# __eq__ and __gt__
print(obj == obj1)
