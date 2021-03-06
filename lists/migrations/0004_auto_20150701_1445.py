# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, null=True, to='lists.List'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='', null=True),
        ),
    ]
