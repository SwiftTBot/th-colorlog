# Generated by Django 2.2.4 on 2019-09-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region',
            field=models.CharField(choices=[('02', '서울'), ('051', '부산'), ('053', '대구'), ('032', '인천'), ('062', '광주'), ('042', '대전'), ('052', '울산'), ('044', '세종'), ('031', '경기'), ('033', '강원'), ('043', '충북'), ('041', '충남'), ('063', '전북'), ('061', '전남'), ('054', '경북'), ('055', '경남'), ('064', '제주')], max_length=10),
        ),
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='story',
            name='color',
            field=models.CharField(choices=[('red', 'red'), ('orange', 'orange'), ('yellow', 'yellow'), ('green', 'green'), ('sky', 'sky'), ('blue', 'blue'), ('purple', 'purple'), ('white', 'white'), ('gray', 'gray'), ('black', 'black')], max_length=15),
        ),
        migrations.AlterField(
            model_name='story',
            name='region',
            field=models.CharField(choices=[('02', '서울'), ('051', '부산'), ('053', '대구'), ('032', '인천'), ('062', '광주'), ('042', '대전'), ('052', '울산'), ('044', '세종'), ('031', '경기'), ('033', '강원'), ('043', '충북'), ('041', '충남'), ('063', '전북'), ('061', '전남'), ('054', '경북'), ('055', '경남'), ('064', '제주')], max_length=10),
        ),
    ]
