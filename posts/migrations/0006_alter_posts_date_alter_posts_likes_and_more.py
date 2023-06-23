# Generated by Django 4.2.1 on 2023-06-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_profilepicture'),
        ('posts', '0005_posts_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likers', to='users.users'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to='users.users'),
        ),
    ]