from django.db import models

# Create your models here.

class StudentApplication(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    interest_bureau = models.CharField(max_length=100)
    proof_of_skills = models.FileField(upload_to='proof_of_skills/')

    def __str__(self):
        return self.name

class ApplicationStatus(models.Model):
    student_application = models.OneToOneField(StudentApplication, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending')

    def __str__(self):
        return f"{self.student_application.name} - {self.status}"

class OCData(models.Model):
    ocname = models.CharField(max_length=100)
    ocusername = models.CharField(max_length=50)
    ocpassword = models.CharField(max_length=50)
    ocid = models.CharField(max_length=20)
    ocemail = models.EmailField()
    ocgender = models.CharField(max_length=10)
    ocbureau = models.CharField(max_length=100)

    def __str__(self):
        return self.ocname
    
class OCBureauLeaderData(models.Model):
    ocbureauleadername = models.CharField(max_length=100)
    ocbureauleaderusername = models.CharField(max_length=50)
    ocbureauleaderpassword = models.CharField(max_length=50)
    ocbureauleaderid = models.CharField(max_length=20)
    ocbureauleaderemail = models.EmailField()
    ocbureauleadergender = models.CharField(max_length=10)
    ocbureauleaderbureau = models.CharField(max_length=100)

    def __str__(self):
        return self.ocbureauleadername
    
class OCPresidentData(models.Model):
    ocpresidentusername = models.CharField(max_length=100)
    ocpresidentpassword = models.CharField(max_length=50)

    def __str__(self):
        return self.ocpresidentusername

class OCEventData(models.Model):
    oceventname = models.CharField(max_length=200)
    oceventdate = models.DateField()
    oceventtime = models.TimeField()
    oceventlocation = models.CharField(max_length=200)
    oceventdescription = models.TextField()
    oceventocneeded = models.IntegerField()

    def __str__(self):
        return self.oceventname

class OCEventData2(models.Model):
    OCEventName = models.CharField(max_length=200)
    OCEventDescription = models.TextField()
    OCEventLocation = models.CharField(max_length=200)
    OCStartDate = models.DateField()
    OCStartTime = models.TimeField()
    OCEndDate = models.DateField()
    OCEndTime = models.TimeField()
    OCNeeded = models.IntegerField()

    def __str__(self):
        return self.OCEventName

class SelectedOC(models.Model):
    oc = models.ForeignKey(OCData, on_delete=models.CASCADE)
    event = models.ForeignKey(OCEventData2, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.oc.ocname} - {self.event.oceventname}"