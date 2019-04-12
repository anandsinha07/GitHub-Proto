from django import forms

from .models import Program

class CreateProgramForm(forms.ModelForm):

    class Meta:
        model = Program
        fields = ('title', 'description')

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(CreateProgramForm, self).__init__(*args, **kwargs)

    def clean_title(self):
    	title = self.cleaned_data.get("title")
    	user = self.user
    	qs = user.programs.filter(title__iexact=title)
    	if qs.exists():
    		raise forms.ValidationError("Cannot use this title. You have another program saved with the same title.")
    	return title


    def save(self, commit=True):
        program = super(CreateProgramForm, self).save(commit=False)
        if commit:
        	program.owner = self.user
        	program.save()
        return program
