# Generated by Django 2.2.4 on 2019-08-11 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestant', '0002_contestant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='category',
            field=models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('General Secretary', 'General Secretary'), ('Assistant General Secretary', 'Assistant General Secretary'), ('Treasurer', 'Treasurer'), ('Financial Secretary', 'Financial Secretary'), ('Librarian', 'Librarian'), ('Sports Director', 'Sports Director'), ('P.R.O', 'P.R.O'), ('Null', 'Null')], default='Null', max_length=120),
        ),
    ]
