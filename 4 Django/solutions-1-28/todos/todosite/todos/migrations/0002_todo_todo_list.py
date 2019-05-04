# Generated by Django 2.0 on 2019-05-02 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lists', '0001_initial'),
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todo_lists.TodoList'),
            preserve_default=False,
        ),
    ]