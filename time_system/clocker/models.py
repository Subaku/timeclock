from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from decimal import Decimal


class EmployeeManager(BaseUserManager):
    pass


class Employee(AbstractBaseUser):
    hireDate = models.BigIntegerField()
    salaried = models.BooleanField()
    hourlyRate = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank=True)
    salary = models.DecimalField(max_digits = 9, decimal_places = 2, null = True, blank=True)
    username = models.CharField(max_length=40, unique=True)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    isActive = models.BooleanField(default=True)
    dateJoined = models.BigIntegerField()

    objects = EmployeeManager()

    USERNAME_FIELD = "username"

    class Meta:
        ordering = ['username']

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def clockIn(self, timeIn):
        
        assert self.isClockedIn() is None

        shift = Shift(employee=self, timeIn=timeIn)
        try:
            shift.full_clean()
            shift.save()
        except ValidationError as e:
            #TODO: handle this
            print e

    def clockOut(self, timeOut):
        
        shift = self.isClockedIn()
        assert isinstance(shift, Shift)

        shift.timeOut = timeOut
        try:
            shift.full_clean()
            shift.save()
        except ValidationError as e:
            #TODO: handle this
            print e

    def isClockIn(self):

        try:
            return Shift.objects.get(employee=self, timeOut=None)
        except Shift.DoesNotExist:
            return None
        except Shift.MultipleObjectsReturned as e:
            #TODO: handle this
            return e


class ShiftManager(models.Manager):
    pass


class Shift(models.Model):
    employee = models.ForeignKey('Employee')
    summaries = models.ManyToManyField('ShiftSummary')
    timeIn = models.BigIntegerField()
    timeOut = models.BigIntegerField(null = True, blank=True)
    totalHours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    objects = ShiftManager()

    class Meta:
        ordering = ['-timeIn', 'employee']

    def save(self, *args, **kwargs):
        if self.timeOut is not None:
            diff = self.timeOut - self.timeIn
            hours = Decimal(diff.total_seconds()/3600).quantize(Decimal('1.00'))
            self.hours = hours
        else:
            self.hours = None

        super(Shift, self).save(*args, **kwargs)


class ShiftSummaryManager(models.Manager):
    pass


class ShiftSummary(models.Model):
    job = models.ForeignKey('Job')
    totalHours = models.DecimalField(max_digits=4, decimal_places=2)
    miles = models.DecimalField(max_digits = 6, decimal_places = 2, null = True, blank=True)
    note = models.TextField()

    objects = ShiftSummaryManager()


class JobManager(models.Manager):
    pass


class Job(models.Model):
    name = models.CharField(max_length = 25)
    description = models.TextField()
    isActive = models.BooleanField() 

    objects = JobManager()

    class Meta:
        ordering = ['-isActive']

    def __unicode__(self):
        return self.name

