from django import forms 

class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username", required=False)
    email = forms.CharField(max_length=100, label="Email", required=False)
    city = forms.CharField(max_length=100, label="City", required=False)
    country = forms.CharField(max_length=36, label="Country", required=False)
    telefon = forms.IntegerField(label="Phone", required=False)

class PostForm(forms.Form):
    title = forms.CharField(max_length=244, label="Title")
    text = forms.CharField(max_length=500, label="Announcement description")
    adress = forms.CharField(max_length=500, label="Adress")
    category = forms.ChoiceField(choices=[(x, x) for x in ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others']], label="Category", widget=forms.Select(attrs={'class': "form-control input-lg m-bot15", 'id': "choose_category"}))
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']], label="Country", widget=forms.Select(attrs={'class': "form-control input-lg m-bot15",
                                                                                                                   'id': "choose_category"}))
    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']], label="City", widget=forms.Select(attrs={'class': "form-control input-lg m-bot15", 'id': "choose_category"}))
    data = forms.DateField(label="Date", widget=forms.TextInput(attrs={'class': "form-control event_input tcal"}))
    timePost = forms.CharField(label="Time", widget=forms.TextInput(attrs={'class': "timepicker"}))
    price = forms.IntegerField(label="Highest price you are willing to pay")
    
class SpartanForm(forms.Form):
    prenume = forms.CharField(max_length=40, label="First name")
    nume = forms.CharField(max_length=40, label="Last name")
    data = forms.DateField(label="Bitrthday", widget=forms.TextInput(attrs={'class': "form-control event_input tcal"}))
    adress = forms.CharField(max_length=500, label="Adress")
    CNP = forms.IntegerField(label="CNP")
    serie = forms.CharField(max_length=30, label="ID card series")
    cui = forms.CharField(max_length=30, label="CUI")
    cont = forms.CharField(max_length=30, label="Banck account")
    abilitate = forms.ChoiceField(choices=[(x, x) for x in ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others']], label="Category", widget=forms.Select(attrs={'class': "form-control input-lg m-bot15", 'id': "choose_category"}))  



