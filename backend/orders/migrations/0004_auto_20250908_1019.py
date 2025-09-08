from django.db import migrations, models
import uuid

def populate_order_id(apps, schema_editor):
    Booking = apps.get_model('orders', 'Booking')
    for booking in Booking.objects.all():
        if not getattr(booking, 'order_id', None):
            booking.order_id = f"ORD{uuid.uuid4().hex[:6].upper()}"
            booking.save()

class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20250908_1001'),  # last successfully applied migration
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='order_id',
            field=models.CharField(max_length=20, unique=True, blank=True, null=True, editable=False),
        ),
        migrations.RunPython(populate_order_id),
        # Optional: Make the field non-nullable after populating all rows
        migrations.AlterField(
            model_name='booking',
            name='order_id',
            field=models.CharField(max_length=20, unique=True, editable=False),
        ),
    ]
