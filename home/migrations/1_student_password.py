
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
