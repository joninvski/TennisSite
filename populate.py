from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage

from tennis.people.models import *
from tennis.competition.models import *
from tennis.sport.models import *
from tennis.organizations.models import *

import datetime


############ ADMIN #############
u = User.objects.create(
    username='admin',
    first_name='',
    last_name='',
    email='',
    is_superuser=True,
    is_staff=True,
    is_active=True
)

u.set_password('naosei')
u.save()

#################################

joao = Person()
joao.name = "Joao Trindade"
joao.birthday = datetime.date(2005, 12, 12)
joao.gender = 'M'
joao.email = 'trindade.joao@gmail.com'
joao.phoneNumber = '935613910'
joao.height = 32
joao.weight = 123
joao.save()

guerra = Person()
guerra.name = "Pedro Guerra"
guerra.birthday = datetime.date(1995, 12, 12)
guerra.gender = 'M'
guerra.email = 'guerra@gmail.com'
guerra.phoneNumber = '932222222'
guerra.height = 32
guerra.weight = 123
guerra.save()

guido = Person()
guido.name = "Guido Esteves"
guido.birthday = datetime.date(2002, 07, 22)
guido.gender = 'M'
guido.email = 'guido@gmail.com'
guido.phoneNumber = '932222190'
guido.height = 32
guido.weight = 123
guido.save()

manel = Person()
manel.name = "Manel Esteves"
manel.birthday = datetime.date(2001, 11, 12)
manel.gender = 'M'
manel.email = 'manelEsteves@gmail.com'
manel.phoneNumber = '931021292'
manel.height = 32
manel.weight = 123
manel.save()

joaquina = Person()
joaquina.name = "Joaquina Lurdes"
joaquina.birthday = datetime.date(1981, 01, 22)
joaquina.gender = 'F'
joaquina.email = 'jakina@gmail.com'
joaquina.phoneNumber = '913131291'
joaquina.height = 32
joaquina.weight = 123
joaquina.save()

##############################################

clubMember = ClubStudent()
clubMember.person =joao
clubMember.save()

clubMember = ClubStudent()
clubMember.person = guerra
clubMember.save()

clubMember = ClubStudent()
clubMember.person = guido
clubMember.save()

schoolMember = SchoolStudent()
schoolMember.person = manel
schoolMember.number = 213
schoolMember.save()

schoolMember = SchoolStudent()
schoolMember.person = joaquina
schoolMember.number = 32
schoolMember.save()

##############################################

escada = Competition()
escada.startDate = datetime.date(1995, 7, 22)
escada.endDate = datetime.date(1995, 8, 10)
escada.name = "Torneio Escada"
escada.save()

escolar = Competition()
escolar.startDate = datetime.date(1975, 2, 23)
escolar.endDate = datetime.date(1975, 2, 11)
escolar.name = "Torneio Escolar"
escolar.save()

##############################################

joaoComp = Competitor()
joaoComp.gamesPlayed = 3
joaoComp.gamesWon = 3
joaoComp.gamesTied = 2
joaoComp.gamesLost = 1
joaoComp.person = joao
joaoComp.competition = escada
joaoComp.rank = 1
joaoComp.save()

guerraComp = Competitor()
guerraComp.gamesPlayed = 3
guerraComp.gamesWon = 3
guerraComp.gamesTied = 2
guerraComp.gamesLost = 1
guerraComp.person = guerra
guerraComp.competition = escada
guerraComp.rank = 2
guerraComp.save()

##############################################

matchA = SingleMatch()
matchA.date = datetime.date(2005, 12, 12)
matchA.competition = escada
matchA.competitorA = joaoComp
matchA.competitorB = guerraComp
matchA.save()

matchB = SingleMatch()
matchB.date = datetime.date(2003, 1, 2)
matchB.competition = escada
matchB.competitorA = joaoComp
matchB.competitorB = guerraComp
matchB.save()

##############################################

setResultA1 = SetResult()
setResultA1.order = 1
setResultA1.match = matchA
setResultA1.games = 6
setResultA1.competitor = joaoComp
setResultA1.save()

setResultA2 = SetResult()
setResultA2.order = 1
setResultA2.match = matchA
setResultA2.games = 3
setResultA2.competitor = guerraComp
setResultA2.save()

setResultA3 = SetResult()
setResultA3.order = 2
setResultA3.match = matchA
setResultA3.games = 5
setResultA3.competitor = joaoComp
setResultA3.save()

setResultA5 = SetResult()
setResultA5.order = 3
setResultA5.match = matchA
setResultA5.games = 7
setResultA5.competitor = joaoComp
setResultA5.save()

setResultA4 = SetResult()
setResultA4.order = 2
setResultA4.match = matchA
setResultA4.games = 7
setResultA4.competitor = guerraComp
setResultA4.save()

setResultA6 = SetResult()
setResultA6.order = 3
setResultA6.match = matchA
setResultA6.games = 5
setResultA6.competitor = guerraComp
setResultA6.save()

setResultB1 = SetResult()
setResultB1.order = 1
setResultB1.match = matchB
setResultB1.games = 1
setResultB1.competitor = guerraComp
setResultB1.save()

setResultB2 = SetResult()
setResultB2.order = 1
setResultB2.match = matchB
setResultB2.games = 6
setResultB2.competitor = joaoComp
setResultB2.save()

setResultB3 = SetResult()
setResultB3.order = 2
setResultB3.match = matchB
setResultB3.games = 4
setResultB3.competitor = guerraComp
setResultB3.save()

setResultB4 = SetResult()
setResultB4.order = 2
setResultB4.match = matchB
setResultB4.games = 6
setResultB4.competitor = joaoComp
setResultB4.save()

##############################################

cocacola = Company()
cocacola.name = "Coca-Cola Ltd"
cocacola.address = "Rua manel da esquina n. 5 dto"
cocacola.isbn = "13213213231"
cocacola.save()

pepsi = Company()
pepsi.name = "Pepsi Ltd"
pepsi.address = "Rua joaquim esteves n. 5"
pepsi.isbn = "133952131"
pepsi.save()

bobadelense = Company()
bobadelense.name = "Bobadelense"
bobadelense.address = "Rua da Bobadela n.123 2650-123"
bobadelense.isbn = "132222222"
bobadelense.save()
