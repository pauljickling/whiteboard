# Generated by Django 2.1 on 2018-08-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0014_auto_20180819_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='language',
            field=models.CharField(choices=[('Psuedocode', 'Psuedocode'), ('C++', 'C++'), ('Go', 'Go'), ('Java', 'Java'), ('Javascript', 'Javascript'), ('Python', 'Python'), ('Ruby', 'Ruby'), ('Rust', 'Rust'), ('Writing', 'Writing')], default='Javascript', max_length=30),
        ),
    ]
