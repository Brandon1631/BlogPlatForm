# Generated by Django 3.2.9 on 2021-11-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
