# Generated by Django 4.0.3 on 2022-09-14 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WordRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('acurate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_misspelleds', to='aiautocorrectapp.word')),
                ('misspelled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_accurates', to='aiautocorrectapp.word')),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='accurates',
            field=models.ManyToManyField(related_name='misspelleds', through='aiautocorrectapp.WordRelation', to='aiautocorrectapp.word'),
        ),
    ]
