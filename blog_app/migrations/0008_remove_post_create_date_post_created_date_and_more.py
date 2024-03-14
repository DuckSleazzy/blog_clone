# Generated by Django 5.0.2 on 2024-03-13 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0007_remove_comment_create_date_comment_created_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="create_date",
        ),
        migrations.AddField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 13, 14, 56, 50, 71588, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 13, 14, 56, 50, 71588, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
