# Generated by Django 3.1.8 on 2021-06-04 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcardApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='collection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='flashcardApp.collection'),
            preserve_default=False,
        ),
    ]
