# Generated by Django 3.2.9 on 2022-07-20 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core2', '0002_auto_20220703_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='is_quote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tweet',
            name='quote_to_tweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='core2.tweet'),
        ),
    ]
