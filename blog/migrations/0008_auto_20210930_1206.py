# Generated by Django 3.1.4 on 2021-09-30 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogcomment_parient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parient',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogcomment'),
        ),
    ]
