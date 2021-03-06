# Generated by Django 3.1.2 on 2020-10-28 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('selling_count', models.IntegerField(null=True)),
                ('buying_count', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.level'),
            preserve_default=False,
        ),
    ]
