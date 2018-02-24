from django.contrib import admin
from .models import Foods
from .models import directional
from .models import Serving
from .models import Groups
from .models import Form
# Register your models here.
admin.site.register(Foods)
admin.site.register(Groups)
admin.site.register(Serving)
admin.site.register(directional)
admin.site.register(Form)