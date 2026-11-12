from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='picture',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
