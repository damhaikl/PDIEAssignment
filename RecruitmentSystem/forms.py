from django import forms
from .models import ApplicationStatus, StudentApplication, OCData, OCBureauLeaderData, OCPresidentData, OCEventData, OCEventData2, SelectedOC

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ['name', 'student_id', 'email', 'gender', 'interest_bureau', 'proof_of_skills']

        GENDER_CHOICES = [
            ('Male', 'Male'),
            ('Female', 'Female'),
        ]

        BUREAU_CHOICES = [
            ('Tugasan Khas', 'Tugasan Khas'),
            ('MakanMinum', 'MakanMinum'),
            ('Media', 'Media'),
            ('Kesihatan', 'Kesihatan'),
            ('Aktiviti', 'Aktiviti'),
        ]

        widgets = {
            'gender': forms.RadioSelect(choices=GENDER_CHOICES),
            'interest_bureau': forms.CheckboxSelectMultiple(choices=BUREAU_CHOICES),
        }

class OCDataForm(forms.ModelForm):
    class Meta:
        model = OCData
        fields = ['ocname', 'ocusername', 'ocpassword', 'ocid', 'ocemail', 'ocgender', 'ocbureau']

class OCBureauLeaderDataForm(forms.ModelForm):
    class Meta:
        model = OCBureauLeaderData
        fields = ['ocbureauleadername', 'ocbureauleaderusername', 'ocbureauleaderpassword', 'ocbureauleaderid', 'ocbureauleaderemail', 'ocbureauleadergender', 'ocbureauleaderbureau']

        GENDER_CHOICES = [
            ('Male', 'Male'),
            ('Female', 'Female'),
        ]

        BUREAU_CHOICES = [
            ('Tugasan Khas', 'Tugasan Khas'),
            ('MakanMinum', 'MakanMinum'),
            ('Media', 'Media'),
            ('Kesihatan', 'Kesihatan'),
            ('Aktiviti', 'Aktiviti'),
        ]

        widgets = {
            'ocbureauleadergender': forms.RadioSelect(choices=GENDER_CHOICES),
            'ocbureauleaderbureau': forms.CheckboxSelectMultiple(choices=BUREAU_CHOICES),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    login_type = forms.ChoiceField(choices=[('OC', 'OC'), ('OC Bureau Leader', 'OC Bureau Leader'), ('OC President', 'OC President')])

class OCPresidentDataForm(forms.ModelForm):
    class Meta:
        model = OCPresidentData
        fields = ['ocpresidentusername', 'ocpresidentpassword']

class OCEventDataForm(forms.ModelForm):
    class Meta:
        model = OCEventData
        fields = ['oceventname','oceventdate','oceventtime','oceventlocation','oceventdescription','oceventocneeded']

class OCEventData2Form(forms.ModelForm):
    class Meta:
        model = OCEventData2
        fields = ['OCEventName','OCEventDescription','OCEventLocation','OCStartDate','OCStartTime','OCEndDate','OCEndTime','OCNeeded']
        labels = {
            'OCEventName': 'OC Event Name',
            'OCEventDescription': 'OC Event Description',
            'OCEventLocation': 'OC Event Location',
            'OCStartDate': 'OC Start Date',
            'OCStartTime': 'OC Start Time',
            'OCEndDate': 'OC End Date',
            'OCEndTime': 'OC End Time',
            'OCNeeded': 'OC Needed',
        }

class SelectedOCForm(forms.ModelForm):
    class Meta:
        model = SelectedOC
        fields = ['oc', 'event', 'selected']

def __init__(self, *args, **kwargs):
    super(SelectedOCForm, self).__init__(*args, **kwargs)
    self.fields['oc'].queryset = OCData.objects.all()
    self.fields['event'].queryset = OCEventData2.objects.all()
    self.fields['event'].label_from_instance = lambda obj: obj.OCEventName

class  UpdateApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = ApplicationStatus
        fields = ['status']