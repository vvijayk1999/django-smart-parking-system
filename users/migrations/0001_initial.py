# Generated by Django 3.0.4 on 2020-03-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField()),
                ('email', models.TextField()),
                ('v_id', models.TextField(max_length=10)),
                ('password', models.TextField()),
                ('password2', models.TextField()),
            ],
        ),
    ]
