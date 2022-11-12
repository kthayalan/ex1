# Generated by Django 4.1.1 on 2022-10-19 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='locality code')),
                ('name', models.CharField(max_length=150, verbose_name='locality name')),
            ],
        ),
        migrations.CreateModel(
            name='LocalPostalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='local postal code name')),
                ('postcode', models.IntegerField(verbose_name='postal code')),
                ('locality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AddressComponent.locality', verbose_name='locality')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='state code')),
                ('name', models.CharField(max_length=150, verbose_name='state name')),
                ('country', models.CharField(max_length=150, verbose_name='country')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='street name')),
                ('local_postal_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AddressComponent.localpostalcode', verbose_name='local postal code')),
            ],
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='post code')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AddressComponent.state', verbose_name='state')),
            ],
        ),
        migrations.AddField(
            model_name='locality',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AddressComponent.state', verbose_name='state'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name='no')),
                ('address_1', models.CharField(max_length=150, verbose_name='address_1')),
                ('street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AddressComponent.street', verbose_name='street')),
            ],
        ),
    ]
