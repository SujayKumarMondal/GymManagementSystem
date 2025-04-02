from django.db import models
from schedule.models import Schedule
from django.utils.translation import gettext_lazy as _
from user.models import User

# Create your models here.

class EquipmentType(models.Model):
    name = models.CharField(_("Name"),max_length=50, null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class Equipment(models.Model):
    name = models.CharField(_("Name"),max_length=50, null=True,blank=True)
    serial = models.CharField(_("Serial"),max_length=30,null=True,blank=True)
    equipmentType = models.ManyToManyField(EquipmentType,blank=True)
    maintenanceDate = models.DateField(_("Maintenance Date"), null=True,blank=True)
    is_available =  models.BooleanField(_("Availability Status"),default=True)
    url =  models.TextField(_("Url"),null=True,blank=True)
    
    price = models.FloatField(_("Price"),null=True,blank=True)
    brand = models.CharField(_("Brand"),max_length=50, null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.name} | {self.serial}'
    
    def get_eqTypes(self):
        eqType = self.equipmentType.all()
        return eqType    

class EquipmentActivityTrack(models.Model):
    start_time = models.DateTimeField(_("Booking start"),null=True,blank=True)
    end_time = models.DateTimeField(_("Booking end"),null=True,blank=True)

    booked_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    booked_for =models.ForeignKey('member.Member', on_delete=models.CASCADE,null=True,blank=True)

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE,null=True,blank=True)
    is_active =  models.BooleanField(_("Is Active"),default=True)

    def __str__(self) -> str:
        return f'{self.equipment} | {self.start_time} - {self.end_time}'