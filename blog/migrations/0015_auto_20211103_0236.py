# Generated by Django 3.1.2 on 2021-11-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blogcomment_total_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='last_seen',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='watching_time',
            field=models.IntegerField(null=True),
        ),
    ]