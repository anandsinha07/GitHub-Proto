from django import forms

from .models import Module

class CreateModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = [
        'title', 
        'version', 
        'dev_id', 
        'developer', 
        'description', 
        'languages', 
        'NumberOfInputs', 
        'InputDescription', 
        'InputType', 
        'Optional', 
        'SubstitutedCode', 
        'var_decl',
        'Indent',
        'IsInFunction'
        ]

    def clean_title(self):
    	title = self.cleaned_data.get("title")
    	qs = Module.objects.filter(title__iexact=title)
    	if qs.exists():
    		raise forms.ValidationError("Cannot use this title. You have another module saved with the same title.")
    	return title

class UpdateModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = [
        'title', 
        'version', 
        'dev_id', 
        'developer', 
        'description', 
        'languages', 
        'NumberOfInputs', 
        'InputDescription', 
        'InputType', 
        'Optional', 
        'SubstitutedCode', 
        'var_decl',
        'Indent',
        'IsInFunction'
        ]
