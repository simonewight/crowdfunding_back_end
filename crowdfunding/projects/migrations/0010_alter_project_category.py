# Generated by Django 5.1 on 2024-12-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Arts', 'Arts'), ('Film', 'Film'), ('Games', 'Games'), ('Music', 'Music'), ('Food', 'Food'), ('Publishing', 'Publishing'), ('Fashion', 'Fashion'), ('Design', 'Design'), ('Other', 'Other')], default='Technology', max_length=100),
        ),
    ]