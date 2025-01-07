from wtforms import Form, StringField

class INNSearchForm(Form):
    search = StringField('')
