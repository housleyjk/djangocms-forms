# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0005_formfield_field_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdefinition',
            name='email_template',
            field=models.CharField(default='djangocms_forms/email_template/default.txt', max_length=150, verbose_name='Email Template', blank=True, choices=[('djangocms_forms/email_template/default.txt', 'Default')]),
        ),
    ]
