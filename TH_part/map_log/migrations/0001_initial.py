# Generated by Django 2.2.4 on 2019-09-28 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('02', '서울'), ('051', '부산'), ('053', '대구'), ('032', '인천'), ('062', '광주'), ('042', '대전'), ('052', '울산'), ('044', '세종'), ('031', '경기'), ('033', '강원'), ('043', '충북'), ('041', '충남'), ('063', '전북'), ('061', '전남'), ('054', '경북'), ('055', '경남'), ('064', '제주')], max_length=1)),
                ('base_color', models.CharField(default='#fafafa', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=2)),
                ('content', models.TextField(blank=True)),
                ('written_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('traveled_start_date', models.DateTimeField()),
                ('traveled_end_date', models.DateTimeField()),
                ('region', models.CharField(choices=[('02', '서울'), ('051', '부산'), ('053', '대구'), ('032', '인천'), ('062', '광주'), ('042', '대전'), ('052', '울산'), ('044', '세종'), ('031', '경기'), ('033', '강원'), ('043', '충북'), ('041', '충남'), ('063', '전북'), ('061', '전남'), ('054', '경북'), ('055', '경남'), ('064', '제주')], max_length=1)),
                ('spot', models.CharField(max_length=50)),
                ('color', models.CharField(choices=[('0', 'red'), ('1', 'orange'), ('2', 'yellow'), ('3', 'green'), ('4', 'sky'), ('5', 'blue'), ('6', 'purple'), ('7', 'white'), ('8', 'gray'), ('9', 'black')], max_length=1)),
            ],
        ),
    ]
