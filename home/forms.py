from django import forms

class AnswerForm(forms.Form):
	ans_text = forms.CharField(widget=forms.Textarea)
	def __str__(self):
		return self.ans_text