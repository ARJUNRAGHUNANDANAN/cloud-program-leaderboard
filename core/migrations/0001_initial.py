# Generated by Django 3.1.2 on 2020-10-04 17:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('qwiklabs_id', models.CharField(max_length=300)),
                ('quests_status', models.IntegerField()),
                ('quests', models.JSONField()),
                ('dp', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]