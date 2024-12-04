from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username','email','first_name','last_name','public_visibility','birth_year','address')

    def age(self, obj): #Custome method to display age into admin 
        return obj.age
    age.short_description = 'Age' #Display name for the column