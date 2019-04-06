#!/usr/bin/env python3
from random import choice, randint
import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr.settings')

import django
django.setup()

from faker import Faker

from portal.models import Event, PersonStatus, Person


Event.objects.all().delete()
PersonStatus.objects.all().delete()

fire_event = Event(name='fire_sale')
fire_event.save()

missing_status = PersonStatus(name='missing')
missing_status.save()

safe_status = PersonStatus(name='safe')
safe_status.save()

# to do: create 30 Person objects using Faker
for _ in range(1,30):
	fake = Faker()
	id_number = randint(1,100000000)
	first_name = fake.first_name()
	last_name = fake.last_name()
	other_name = fake.first_name()
	event = Event.objects.get(name='fire_sale')
	status_number = choice([0, 1, 2])
	print(status_number)
	if status_number != 2:
		person_status = PersonStatus.objects.all()[status_number]
		print(person_status)
	else:
		person_status = None
	mobile = fake.phone_number()
	email = fake.email()
	description = fake.text()

	p = Person(id_number=id_number, first_name=first_name, last_name=last_name, other_name=other_name, 
		event=event, status=person_status,email=email, mobile=mobile, description=description)
	print(p)
	p.save()
	