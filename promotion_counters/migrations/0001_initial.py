# Generated by Django 3.2.5 on 2023-08-17 17:59

import django.core.validators
import django.utils.timezone
import project.apps.promotion.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionProgram',
            fields=[
                ('id', models.UUIDField(default=project.apps.promotion.models.uuid7, editable=False, primary_key=True,
                                        serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_at', models.DateTimeField(blank=True, verbose_name='Start date')),
                ('end_at', models.DateTimeField(blank=True, null=True, verbose_name='End date')),
                ('target_action', models.CharField(max_length=255, verbose_name='Target action')),
                ('target_value',
                 models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)],
                                     verbose_name='Target value')),
                ('achievement_callback', models.CharField(max_length=255, verbose_name='Achievement callback')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived')),
            ],
            options={
                'verbose_name': 'Promotion program',
                'verbose_name_plural': 'Promotion programs',
                'db_table': 'promotion_program',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='AchievementCounter',
            fields=[
                ('id', models.UUIDField(default=project.apps.promotion.models.uuid7, editable=False, primary_key=True,
                                        serialize=False)),
                ('counter', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)],
                                                verbose_name='Counter')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='Started at')),
                ('last_incremented_at',
                 models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last incremented at')),
                ('achieved_at', models.DateTimeField(blank=True, null=True, verbose_name='Achieved at')),
                ('promotion_program',
                 models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='promotion.promotionprogram',
                                   verbose_name='Promotion program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Achievement counter',
                'verbose_name_plural': 'Achievement counters',
                'db_table': 'achievement_counter',
                'ordering': ('-id',),
            },
        ),
        migrations.AddConstraint(
            model_name='achievementcounter',
            constraint=models.UniqueConstraint(condition=models.Q(('achieved_at__isnull', True)),
                                               fields=('user', 'promotion_program'),
                                               name='unique_unfinished_counter_for_program'),
        ),
        migrations.AddConstraint(
            model_name='achievementcounter',
            constraint=models.CheckConstraint(check=models.Q(('counter__gte', 0)), name='counter_gte_zero'),
        ),
    ]
