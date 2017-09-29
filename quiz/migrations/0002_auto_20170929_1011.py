# Generated by Django 2.0a1 on 2017-09-29 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.Quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
