# Generated by Django 3.0.3 on 2020-02-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200222_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(help_text='Insert tags here for better SEO ', max_length=30),
        ),
    ]
