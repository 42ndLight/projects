# Generated by Django 5.2.2 on 2025-06-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='comments',
        ),
    ]
