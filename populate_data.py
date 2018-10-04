import os
import django
import random
from faker import Faker
from first_app.models import Topic,webpage,accessRecord
import pdb

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_prject.settings')

pdb.set_trace()
django.setup()

fakegen=Faker()

topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()

    return t


def populate(N=5):
    for entry in range(N):
        top=add_topic()

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg=webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


        accrec=accessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('populating')
    populate(20)
    print('populating complete')