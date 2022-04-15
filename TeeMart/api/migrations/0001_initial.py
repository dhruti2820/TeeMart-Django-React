from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, achema_editor):
        user =CustomUser(name="dhruti",
                         email="dhrutiakshaybhavsar@gmail.com",
                         is_staff=True,
                         is_superuser=True,
                         phone=9687654504,
                         gender="Female:"
                         )
        user.set_password("12345")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]