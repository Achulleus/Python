import Assets as a


class Company:

    def __init__(self):
        self.persons = []
        self.department_counters = {}
        [self.department_counters.setdefault(i, 0) for i in a.Department]

    def add_person(self, p: a.Person):
        if not isinstance(p, a.Person):
            raise Exception()
        self.persons.append(p)
        self.department_counters[p.dep] += 1

    def add_persons(self, l: list):
        for p in l:
            self.add_person(p)

    def get_all_persons(self):
        return self.persons

    def get_all_mitarbeiter(self):
        ms = [m for m in self.persons if isinstance(m, a.Mitarbeiter)] #List-Coprehansion
        #for m in self.persons:
            #if isinstance(m, a.Mitarbeiter):
                #ms.append(m)
        return ms

    def get_all_gruppenleiter(self):
        gs = []
        for g in self.persons:
            if isinstance(g, a.Gruppenleiter):
                gs.append(g)
        return gs

    def get_departments(self):
        return a.Department

    def get_department_with_most_employees(self):
        return max(self.department_counters, key=self.department_counters.get)

    def get_gender_amount(self, s: a.Sex):
        if not isinstance(s, a.Sex):
            raise Exception()
        gs = []
        for g in self.persons:
            if g.sex == s:
                gs.append(g)
        return gs

    def get_gender_percentage(self, s: a.Sex):
        return 100 * len(self.get_gender_amount(s)) / len(self.persons)

    def get_persons_by_department(self, dep: a.Department):
        if not isinstance(dep, a.Department):
            raise Exception()
        es = []
        for e in self.persons:
            if e.dep == dep:
                es.append(e)
        return es


if __name__ == '__main__':
    employees = [a.Person(), a.Person(), a.Person(), a.Mitarbeiter(), a.Mitarbeiter(), a.Mitarbeiter(),
                 a.Gruppenleiter(), a.Gruppenleiter(), a.Gruppenleiter()]
    c = Company()
    c.add_persons(employees)

    print(f'Number of all persons: {len(c.get_all_persons())}\n'
        f'Number of all Mitarbeiter: {len(c.get_all_mitarbeiter())}\n'
        f'Number of all Gruppenleiter {len(c.get_all_gruppenleiter())}')
    print(f'Number of all departments: {len(c.get_departments())}')
    print(f'Department with most employees: {c.get_department_with_most_employees()}')
    print(f'Percentage of females males: {c.get_gender_percentage(a.Sex.FeMale):{3}.{6}}%')
