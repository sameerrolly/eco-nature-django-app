# Generated by Django 4.0.3 on 2022-04-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_myres_remove_energy_author_remove_energy_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='myhelp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='myrev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='health',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='technology',
            name='description',
            field=models.TextField(),
        ),
    ]
