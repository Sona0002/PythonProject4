# Generated by Django 4.2.2 on 2023-06-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
