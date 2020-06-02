# Generated by Django 3.0.6 on 2020-05-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_stages_prompt", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="prompt", name="order", field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="prompt",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "Text"),
                    ("e-mail", "Email"),
                    ("password", "Password"),
                    ("number", "Number"),
                    ("checkbox", "Checkbox"),
                    ("data", "Date"),
                    ("data-time", "Date Time"),
                    ("separator", "Separator"),
                    ("hidden", "Hidden"),
                    ("static", "Static"),
                ],
                max_length=100,
            ),
        ),
    ]
