# Generated by Django 4.2.6 on 2023-10-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0021_alter_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='img_menu_url',
            field=models.URLField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.canva.com%2Fes_es%2Fmenus%2Fplantillas%2F&psig=AOvVaw2J6ejfkjXfELK9saL1IX_Q&ust=1698090814443000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLiXy7C3ioIDFQAAAAAdAAAAABAE', max_length=4000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo_url',
            field=models.URLField(blank=True, default=None, max_length=2000, null=True),
        ),
    ]
