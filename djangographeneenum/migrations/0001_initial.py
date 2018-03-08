# Generated by Django 2.0.3 on 2018-03-08 18:02

from django.db import migrations, models
import djangographeneenum.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('vanilla_enum', models.CharField(choices=[(djangographeneenum.models.VanillaEnum(1), djangographeneenum.models.VanillaEnum(1)), (djangographeneenum.models.VanillaEnum(2), djangographeneenum.models.VanillaEnum(2)), (djangographeneenum.models.VanillaEnum(3), djangographeneenum.models.VanillaEnum(3))], default=djangographeneenum.models.VanillaEnum(3), max_length=20)),
            ],
        ),
    ]