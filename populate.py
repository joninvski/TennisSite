from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage

from tennis.people.models import *
from tennis.competition.models import *
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
joao.name = "João Trindade"
joao.birthday = datetime.date(2005, 12, 12)
joao.gender = 'M'
joao.email = 'trindade.joao@gmail.com'
joao.phoneNumber = '935613910'
joao.save()


guerra = Person()
guerra.name = "Pedro Guerra"
guerra.birthday = datetime.date(1995, 12, 12)
guerra.gender = 'M'
guerra.email = 'guerra@gmail.com'
guerra.phoneNumber = '932222222'
guerra.save()

guido = Person()
guido.name = "Guido Esteves"
guido.birthday = datetime.date(2002, 07, 22)
guido.gender = 'M'
guido.email = 'guido@gmail.com'
guido.phoneNumber = '932222190'
guido.save()

manel = Person()
manel.name = "Manel Esteves"
manel.birthday = datetime.date(2001, 11, 12)
manel.gender = 'M'
manel.email = 'manelEsteves@gmail.com'
manel.phoneNumber = '931021292'
manel.save()

joaquina = Person()
joaquina.name = "Joaquina Lurdes"
joaquina.birthday = datetime.date(1981, 01, 22)
joaquina.gender = 'F'
joaquina.email = 'jakina@gmail.com'
joaquina.phoneNumber = '913131291'
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
schoolMember.save()

schoolMember = SchoolStudent()
schoolMember.person = joaquina
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
