# Generated by Django 2.2 on 2021-02-22 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtg_app', '0002_auto_20210221_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DeckMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtg_app.Card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtg_app.Deck')),
            ],
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(through='mtg_app.DeckMembership', to='mtg_app.Card'),
        ),
        migrations.AddField(
            model_name='deck',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='decks', to='mtg_app.User'),
        ),
    ]