# Generated by Django 2.1.5 on 2019-01-11 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('main', '0002_specuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='userspec',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(choices=[('seller', 'seller'), ('user', 'user'), ('clinic', 'clinic'), ('hospital', 'hospital'), ('bloodbank', 'bloodbank'), ('diagnostic', 'diagnostic')], default='user', max_length=10)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='specuser',
        ),
    ]
