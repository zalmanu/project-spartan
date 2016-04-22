from django import forms

class LicitatieForm(forms.Form):
    pret = forms.IntegerField(label="Liciteaza:", widget=forms.TextInput(attrs={'class': "form-control",
                                                                           'id':"bid-input",
                                                                            'aria-describedby': "start-date"  }))
    tip = forms.ChoiceField(choices=[(x, x) for x in ['Pe anunt', 'Pe ora']], widget=forms.Select(attrs={'class': "form-control input-lg m-bot15 bid-sort"
                                                                                                         , 'id':"sort-by"}))
