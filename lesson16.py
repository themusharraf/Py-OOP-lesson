from dataclasses import dataclass, field


@dataclass
class Person:
    # type hinting
    name: str
    age: int
    address: str
    city: str = field(default="The City", init=True)


odam = Person("Akbar", 45, "Tashkent")
print(odam.city)
