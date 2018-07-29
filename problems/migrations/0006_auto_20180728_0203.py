# Generated by Django 2.0.6 on 2018-07-28 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_auto_20180723_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='problem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='problems.Problem'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='category',
            field=models.CharField(choices=[('Non_Coding', 'Non-Coding'), ('Arrays and Strings', 'Arrays and Strings'), ('Linked Lists', 'Linked Lists'), ('Stacks and Queues', 'Stacks and Queues'), ('Trees and Graphs', 'Trees and Graphs'), ('Bit Manipulation', 'Bit Manipulation'), ('Math and Logic Puzzles', 'Math and Logic Puzzles'), ('Object Oriented Design', 'Object Oriented Design'), ('Recursion and Dynamic Programming', 'Recursion and Dynamic Programming'), ('System Design and Scalability', 'System Design and Scalability'), ('Sorting and Searching', 'Sorting and Searching'), ('Testing', 'Testing'), ('Javascript', 'Javascript')], default='Non_Coding', max_length=100),
        ),
    ]