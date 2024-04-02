# Generated by Django 4.2.6 on 2024-03-30 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commondb', '0029_alter_genre_image_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='commondb.restaurant', verbose_name='店舗名'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(verbose_name='コメント'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='review_images/', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='review_images/', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='review_images/', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], verbose_name='評価'),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondb.restaurant', verbose_name='店名'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー名'),
        ),
        migrations.AlterField(
            model_name='review',
            name='visit_date',
            field=models.DateField(verbose_name='訪問日'),
        ),
    ]