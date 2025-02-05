# Generated by Django 5.1.5 on 2025-01-23 18:06

import django.db.models.deletion
import uuid6
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyResult',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField()),
                ('goal', models.DecimalField(decimal_places=2, max_digits=14)),
                ('initial_value', models.DecimalField(decimal_places=2, max_digits=14)),
                ('description', models.TextField(blank=True, null=True)),
                ('format', models.TextField(choices=[('NUMBER', 'Number'), ('PERCENTAGE', 'Percentage'), ('COIN_BRL', 'Coin Brl'), ('COIN_USD', 'Coin Usd'), ('COIN_EUR', 'Coin Eur'), ('COIN_GBP', 'Coin Gbp')])),
                ('type', models.TextField(choices=[('ASCENDING', 'Ascending'), ('DESCENDING', 'Descending')])),
                ('mode', models.TextField(choices=[('COMPLETED', 'Completed'), ('PUBLISHED', 'Published'), ('DRAFT', 'Draft'), ('DELETED', 'Deleted')])),
                ('comment_count', models.JSONField()),
                ('last_updated_by', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'key_result',
            },
        ),
        migrations.CreateModel(
            name='KeyResultCheckIn',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('value', models.FloatField()),
                ('confidence', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('previous_state', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'key_result_check_in',
            },
        ),
        migrations.CreateModel(
            name='KeyResultCheckMark',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('state', models.TextField(choices=[('CHECKED', 'Checked'), ('UNCHECKED', 'Unchecked')])),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'key_result_check_mark',
            },
        ),
        migrations.CreateModel(
            name='KeyResultComment',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('type', models.TextField(choices=[('suggestion', 'Suggestion'), ('praisal', 'Praisal'), ('question', 'Question'), ('alignment', 'Alignment'), ('improvement', 'Improvement'), ('issue', 'Issue'), ('comment', 'Comment')])),
                ('extra', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'key_result_comment',
            },
        ),
        migrations.CreateModel(
            name='KeyResultSupportTeamMembersUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'key_result_support_team_members_user',
            },
        ),
        migrations.CreateModel(
            name='KeyResultUpdate',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('author', models.JSONField()),
                ('old_state', models.JSONField()),
                ('patches', models.JSONField()),
                ('new_state', models.JSONField()),
            ],
            options={
                'db_table': 'key_result_update',
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField()),
                ('description', models.CharField(blank=True, null=True)),
                ('mode', models.TextField(choices=[('COMPLETED', 'Completed'), ('PUBLISHED', 'Published'), ('DRAFT', 'Draft'), ('DELETED', 'Deleted')])),
            ],
            options={
                'db_table': 'objective',
            },
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('period', models.CharField()),
                ('cadence', models.TextField(choices=[('YEARLY', 'Yearly'), ('QUARTERLY', 'Quarterly')])),
                ('active', models.BooleanField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='okr.cycle')),
            ],
            options={
                'db_table': 'cycle',
            },
        ),
    ]

