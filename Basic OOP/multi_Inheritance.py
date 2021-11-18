class Person:
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name


class TeamMember(Person):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.salary = kwargs.get('salary', 0)
        self.jobtitle = kwargs.get('jobtitle', 'N/A')


class Architect(TeamMember):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.certificates = kwargs.get('certificates', [])
        self.jobtitle = 'Architect'


class TeamLeader(TeamMember):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.soft_skills = kwargs.get('soft skills', [])
        self.jobtitle = 'TeamLeader'

    def __str__(self):
        return 'TL'


class CTO(TeamLeader, Architect):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.projects = kwargs.get('projects')
        self.soft_skills += ['Leadership', 'EQ']
        self.certificates += ['ITIL', 'PMA']
        self.jobtitle = 'CTO'


cto = CTO(
    first_name='Jake',
    last_name='Smith',
    salary=250000
)

print(cto.jobtitle)