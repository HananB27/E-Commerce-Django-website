# Generated by Django 4.1.4 on 2022-12-27 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_item_image_item_bid_item_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('is_closed', models.BooleanField(blank=True, default=False, null=True)),
                ('url', models.CharField(max_length=800)),
                ('description', models.CharField(max_length=400)),
                ('category', models.CharField(blank=True, max_length=400, null=True)),
                ('bid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='auctions.bid')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing', to=settings.AUTH_USER_MODEL)),
                ('watchList', models.ManyToManyField(blank=True, related_name='watch_listings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='comments',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listing'),
        ),
        migrations.AddField(
            model_name='comments',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
