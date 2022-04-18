from django.db import models

from django.db import migrations

def create_data(apps, schema_editor):
    Inmates = apps.get_model('accounts', 'Inmates')
    Inmates(Hostel_ID="1234", Name="abc", Room_Num="00", Preference="Nil", Bill_Amount="0" , MC="0", Marked="0").save()
class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]

# Create your models here.
class Inmates(models.Model):
	Hostel_ID = models.CharField(max_length=30, null=True)
	Name = models.CharField(max_length=100, null=True)
	Room_Num = models.CharField(max_length=10, null=True)
	Preference = models.CharField(max_length=20, null=True)
	Bill_Amount = models.IntegerField(null=True)
	MC = models.IntegerField(null=True)
	Marked = models.IntegerField(null=True)
