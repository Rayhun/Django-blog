# Generated by Django 3.1.4 on 2021-09-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_replayblogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='parient',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]