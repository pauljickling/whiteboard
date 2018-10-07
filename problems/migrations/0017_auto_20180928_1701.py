# Generated by Django 2.1 on 2018-09-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0016_auto_20180907_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='category',
            field=models.CharField(choices=[('All', 'All'), ('Arrays and Strings', 'Arrays and Strings'), ('Linked Lists', 'Linked Lists'), ('Stacks and Queues', 'Stacks and Queues'), ('Trees and Graphs', 'Trees and Graphs'), ('Bit Manipulation', 'Bit Manipulation'), ('Object Oriented Design', 'Object Oriented Design'), ('Recursion and Dynamic Programming', 'Recursion and Dynamic Programming'), ('System Design and Scalability', 'System Design and Scalability'), ('Sorting and Searching', 'Sorting and Searching'), ('Testing and Debugging', 'Testing and Debugging')], default='All', max_length=100),
        ),
    ]