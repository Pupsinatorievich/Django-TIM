from django import forms

"""
- существует несколько представлений формы в html документе

{{ form.as_table }} выведет их в таблице, в ячейках тега <tr>
{{ form.as_p }} обернет их в тег <p>
{{ form.as_ul }} выведет в теге <li>

- каждый раз когда мы используем формы в HTML документе , 
  нужно использовать тэг {% csrf_token %} 
"""

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)

