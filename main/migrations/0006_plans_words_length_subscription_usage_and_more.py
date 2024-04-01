# Generated by Django 4.2.2 on 2023-12-04 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_subscription_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='words_length',
            field=models.IntegerField(default=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='usage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='main.plans'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]
