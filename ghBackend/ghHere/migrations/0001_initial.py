# Generated by Django 3.1.5 on 2022-03-22 15:55

from django.db import migrations, models
import ghHere.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GHRequest',
            fields=[
                ('code', models.CharField(default=ghHere.models.generate_code, max_length=10, primary_key=True, serialize=False)),
                ('gh_num', models.CharField(max_length=128, null=True)),
                ('input_data', models.JSONField(default=ghHere.models.inputDefault, null=True)),
                ('txt_input', models.FileField(default='Default/input.txt', null=True, upload_to='')),
                ('stl_result', models.FileField(default='Default/DFW-V0-3d_file_with_various_height.stl', null=True, upload_to='')),
                ('succeed', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
