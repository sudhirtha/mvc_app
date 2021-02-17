from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email = models.EmailField(max_length=30)
    salary=models.FloatField()

    @classmethod
    def get_dummy_emp(cls):
        return cls(id=0,name='',age=0,email='',salary=0.0)

    class Meta:
        db_table = "EMP_INFO"

class Address(models.Model):
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pincode=models.IntegerField()
    empref = models.ForeignKey(Employee,on_delete=models.CASCADE, null=True,related_name='adrref')

    @classmethod
    def get_dummy_adr(cls):
        return cls(id=0, city='',state='',pincode=0)

    class Meta:
        db_table="ADR_INFO"
