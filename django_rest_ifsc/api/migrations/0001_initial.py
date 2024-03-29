# Generated by Django 3.0.5 on 2020-04-11 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('ifsc', models.CharField(max_length=500, unique=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Bank')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branch',
                'ordering': ('name',),
            },
        ),
    ]
