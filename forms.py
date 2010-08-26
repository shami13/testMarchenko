from django.forms import ModelForm, widgets
from models import User

class CalendarWidget(widgets.DateInput):
    def render(self, name, value, attrs):
        attributes = attrs
        
        res = super(CalendarWidget, self).render(name, value, attrs=attributes)
        res += """ <script type="text/javascript">
  $(function() {
    $("#id_%s").datepicker({ dateFormat: 'yy-mm-dd' });
  });
  </script>""" % name
        return res
            
    class Media:
        css = {'all':('/media/jquery-ui.css',)}
        js = ('/media/jquery.ui.datepicker.js',)

class UserForm(ModelForm):
    class Meta:
        model = User
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['birthDate'].widget = CalendarWidget()
        
