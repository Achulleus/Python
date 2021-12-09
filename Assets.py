from enum import Enum, auto


class Sex(Enum):
    Indeterminable = 0,
    Male = auto(),
    FeMale = auto()


class Department(Enum):
    NoDepartment = 0,
    EconomicalEngineering = auto(),
    BiomedicalEngineering = auto(),
    ElectricalEngineering = auto(),
    MechanicalEngineering = auto()


class Person:
    def __init__(self, dep: Department = Department.EconomicalEngineering, sex: Sex = Sex.Male):
        self.dep = dep
        self.sex = sex


class Mitarbeiter(Person):
    def __init__(self, dep: Department = Department.BiomedicalEngineering, sex: Sex = Sex.FeMale):
        super().__init__(dep, sex)


class Gruppenleiter(Mitarbeiter):
    def __init__(self, dep: Department = Department.MechanicalEngineering, sex: Sex = Sex.Male):
        super().__init__(dep, sex)