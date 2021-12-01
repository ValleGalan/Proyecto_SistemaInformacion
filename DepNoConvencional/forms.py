from django.forms import ModelForm
from .models import Actividad , Profesional


#----formulario Lugar
class ActividadForm(ModelForm):
    
    class Meta:
        model = Actividad
        fields = '__all__'
        # fields = ['last_store', 'make', 'model', 'series', 'series_year', 'price_new', 'engine_size', 'fuel_system', 'tank_capacity', 'power', 'seating_capacity', 'standard_transmission', 'body_type', 'drive', 'wheelbase', 'available']

class ProfesionalForm(ModelForm):
    
    class Meta:
        model = Profesional
        fields = '__all__'
'''
class FormularioUsuario(forms.ModelForm):
    class meta:
        model = Usuario
        fields='__all__'
        widgets={'fechaRegistro': forms.DateInput(attrs={'type':'date'})}
        #correo=forms.EmailField()
        #mensaje =forms.CharField()'''