# Generated by Django 4.2.5 on 2023-10-07 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0018_alter_menuplate_unique_together_menuplate_restaurant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.restaurant'),
            preserve_default=False,
        ),
    ]
