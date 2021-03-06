# Generated by Django 3.0.4 on 2020-04-01 09:09

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', ckeditor.fields.RichTextField(default='this is a Description of About FSK Salon.')),
            ],
        ),
        migrations.CreateModel(
            name='Beauty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('short_description', ckeditor.fields.RichTextField(default='Course Short Descriptions')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='Couuse Long Descriptions')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('short_description', ckeditor.fields.RichTextField(default='Blog Short Description')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='Blog Long Description')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Bridal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('description', ckeditor.fields.RichTextField(default='this is a single line details of image')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('short_description', ckeditor.fields.RichTextField(default='Course Short Descriptions')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='Couuse Long Descriptions')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Hair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('short_description', ckeditor.fields.RichTextField(default='this is a dummy text')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='this is a Description of About FSK Salon.')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Nail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('description', ckeditor.fields.RichTextField(default='this is a single line details of image')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('description', ckeditor.fields.RichTextField(default='this is a single line details of image')),
            ],
        ),
        migrations.CreateModel(
            name='Tattoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('description', ckeditor.fields.RichTextField(default='this is a single line details of image')),
            ],
        ),
    ]
