from django.db import models

# Create your models here.

class AcademicDetails(models.Model):
    appl_no = models.IntegerField(primary_key=True)
    Student_name = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    Roll_no = models.CharField(max_length=20,unique=True)
    Reg_no = models.BigIntegerField()
    hsc_roll_no = models.IntegerField()
    medium_of_study = models.CharField(max_length=20)
    board_of_study = models.CharField()
    NEET_hall_ticket_no = models.BigIntegerField()
    NEET_roll_no = models.BigIntegerField()
    NEET_overall_percentile = models.FloatField()
    NEET_mark = models.IntegerField()
    NEET_air = models.IntegerField()
    admission_quota = models.CharField()
    gen_rank = models.IntegerField()
    HSC_total_mark = models.IntegerField()
    HSC_pcb_total = models.IntegerField()
    date_of_birth = models.DateField()
    allotment_date = models.DateField()
    