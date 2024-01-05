# Generated by Django 4.2.4 on 2023-11-12 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=350)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retweets', to='tweet.tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retweets_by_user', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('tweet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tweet.tweet')),
                ('reply_to_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='tweet.tweet')),
            ],
            bases=('tweet.tweet',),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('tweet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tweet.tweet')),
                ('quote_to_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='tweet.tweet')),
            ],
            bases=('tweet.tweet',),
        ),
    ]
