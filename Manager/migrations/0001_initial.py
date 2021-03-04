# Generated by Django 3.0.8 on 2021-03-03 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=80)),
                ('Contact', models.IntegerField()),
                ('Registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=255, null=True)),
                ('Password', models.CharField(max_length=120, null=True)),
                ('Contact_Number', models.IntegerField()),
                ('Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_type', models.CharField(max_length=50)),
                ('Transaction_amount', models.FloatField(max_length=50, null=True)),
                ('Bal_before_tansaction', models.FloatField(max_length=50)),
                ('Bal_after_transaction', models.FloatField(max_length=50)),
                ('Transaction_Date', models.DateTimeField(auto_now_add=True)),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_no', models.IntegerField()),
                ('Account_Balance', models.FloatField(max_length=100, null=True)),
                ('Creted_date', models.DateTimeField(auto_now_add=True)),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Customer')),
            ],
        ),
    ]
