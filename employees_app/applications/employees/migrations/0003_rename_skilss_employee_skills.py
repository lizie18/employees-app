# Generated by Django 4.1.5 on 2023-02-02 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_skill_alter_employee_options_employee_avatar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='skilss',
            new_name='skills',
        ),
    ]
