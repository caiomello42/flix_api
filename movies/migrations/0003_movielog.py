from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedeletelog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieDeleteLog',
            new_name='MovieLog',
        ),
        migrations.RenameField(
            model_name='movielog',
            old_name='deleted_by',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='movielog',
            old_name='deleted_at',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='movielog',
            name='action',
            field=models.CharField(
                choices=[('create', 'Criação'), ('update', 'Edição'), ('delete', 'Exclusão')],
                default='delete',
                max_length=10,
            ),
            preserve_default=False,
        ),
    ]
