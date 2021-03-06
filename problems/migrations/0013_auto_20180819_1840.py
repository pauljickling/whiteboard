# Generated by Django 2.1 on 2018-08-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0012_auto_20180819_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='category',
            field=models.CharField(choices=[('All', 'All'), ('Non Coding', 'Non Coding'), ('Arrays and Strings', 'Arrays and Strings'), ('Linked Lists', 'Linked Lists'), ('Stacks and Queues', 'Stacks and Queues'), ('Trees and Graphs', 'Trees and Graphs'), ('Bit Manipulation', 'Bit Manipulation'), ('Math and Logic Puzzles', 'Math and Logic Puzzles'), ('Object Oriented Design', 'Object Oriented Design'), ('Recursion and Dynamic Programming', 'Recursion and Dynamic Programming'), ('System Design and Scalability', 'System Design and Scalability'), ('Sorting and Searching', 'Sorting and Searching'), ('Testing', 'Testing'), ('Javascript', 'Javascript')], default='All', max_length=100),
        ),
    ]
