from dataclasses import dataclass, field


@dataclass
class Xodim:
    name: str
    age: int

    emp_id: int
    city: str = field(init=False, default="Tashkent", repr=True)


obj = Xodim("Alice", 18, 4456)
print(obj)
