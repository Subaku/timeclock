from django.db import models
from django.contrib.auth import models as auth_models
from datetime import datetime

class Employee(models.Model):
    user = models.ForeignKey(auth_models.User, unique=True)
    hire_date = models.DateField('date employee was hired')
    has_salary = models.BooleanField()
    hourly_rate = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank=True)
    salary = models.DecimalField(max_digits = 8, decimal_places = 2, null = True, blank=True)

    class Meta:
        db_table = 'Employee'

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

    def clock_in(self):
        """
        Clocks an employee in.  Returns the error message "none" if the user clocked in and
        "in" if the user was not able to clock in
        """

        max_id = Time.objects.filter(employee=self.user).aggregate(employee=models.Max('id'))
        record = Time.objects.filter(id=max_id['employee'])

        #Employee has never clocked in before or has previously clocked out
        if(len(record) == 0 or record[0].time_out != None):
            time = Time(employee=self.user,
                        time_in=datetime.now())
            time.save()
            return "none"
        else:

            return "in"

    def clock_out(self):
        """
        Clocks an employee out.  Returns the error message "none" if the user clocked out and
        "out" if the user was not able to clock out.
        """

        max_id = Time.objects.filter(employee=self.user).aggregate(employee=models.Max('id'))
        record = Time.objects.filter(id=max_id['employee'])

        #Employee has never clocked out before or has not clocked in yet.
        if(len(record) == 0 or record[0].time_out != None):
            return "out"
        else:
            time = Time(id=record[0].id,
                        employee=record[0].employee,
                        time_in=record[0].time_in,
                        time_out=datetime.now())
            time.save()
            return "none"

class Time(models.Model):
    employee = models.ForeignKey('Employee')
    time_in = models.DateTimeField('clock in time')
    time_out = models.DateTimeField('clock out time', null = True, blank=True)

    class Meta:
        db_table = 'Time'

    def __unicode__(self):
        data = self.employee.user.username + " time_in: " + self.time_in.strftime("%Y-%m-%d %H:%M") + " time_out: "
        if(self.time_out != None):
            data += self.time_out.strftime("%Y-%m-%d %H:%M")
        return data


