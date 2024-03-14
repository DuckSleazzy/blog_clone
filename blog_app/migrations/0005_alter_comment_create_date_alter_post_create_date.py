# Generated by Django 5.0.2 on 2024-03-13 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0004_alter_comment_create_date_alter_post_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 13, 14, 18, 46, 564323, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 13, 14, 18, 46, 561571, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]