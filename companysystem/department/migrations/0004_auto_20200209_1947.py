# Generated by Django 2.1.5 on 2020-02-09 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_auto_20200209_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='dept_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='emp_name',
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='name',
            new_name='manager_name',
        ),
    ]