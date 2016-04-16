from django import forms 

class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username", required=False)
    email = forms.CharField(max_length=100, label="Email", required=False)
    city = forms.CharField(max_length=100, label="City", required=False)
    country = forms.CharField(max_length=100, label="Country", required=False)
    telefon = forms.IntegerField(label="Phone", required=False)

class PostForm(forms.Form):
    title = forms.CharField(max_length=20, label="Title")
    text = forms.CharField(max_length=500, label="Announcement description")
    adress = forms.CharField(max_length=500, label="Adress")
    category = forms.ChoiceField(choices=[(x, x) for x in ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others']], label="Category", widget=forms.Select(attrs={'class': "form-control input-lg m-bot15"}))
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']], label="Country", widget=forms.Select(attrs={'class': "form-control input-lg m-bot15"}))
    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']], label="City", widget=forms.Select(attrs={'class': "form-control input-lg m-bot15"}))
    data = forms.CharField(label="Date", widget=forms.TextInput(attrs={'class': "form-control event_input tcal"}))
    timePost = forms.CharField(label="Time", widget=forms.TextInput(attrs={'class': "timepicker"}))
    price = forms.IntegerField(label="Highest price you are willing to pay")

    

