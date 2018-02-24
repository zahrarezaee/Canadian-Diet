from django import forms
from .models import Form
GENDER = (
    ('Male', 'Male'),
    ('Female','Female'),
)
AGES = (
    ('2 to 3','2 to 3'),
    ('4 to 8','4 to 8'),
    ('9 to 13','9 to 13'),
    ('14 to 18','14 to 18'),
    ('19 to 30','19 to 30'),
    ('31 to 50','31 to 50'),
    ('51 to 70','51 to 70'),
    ('71+','71+'),
)
class ageForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER,required=True)
    age = forms.ChoiceField(choices=AGES,required=True)
    class Meta:
        model = Form
        fields = ('gender','age')

