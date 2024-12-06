from django.contrib import admin
from myapp.models import person
from myapp.models import news
from myapp.models import publications
from myapp.models import video
from myapp.models import services
from myapp.models import current_issue
from myapp.models import FAQ
from myapp.models import laws
from myapp.models import university
from myapp.models import energy
from myapp.models import health
from myapp.models import technology
from myapp.models import myregister
from myapp.models import myhelp
from myapp.models import myrev
from myapp.models import userRegister
# Register your models here.
admin.site.register(person)
admin.site.register(news)
admin.site.register(publications)
admin.site.register(video)
admin.site.register(services)
admin.site.register(current_issue)
admin.site.register(FAQ)
admin.site.register(laws)
admin.site.register(university)
admin.site.register(energy)
admin.site.register(health)
admin.site.register(technology)
admin.site.register(myregister)
admin.site.register(myhelp)
admin.site.register(myrev)
admin.site.register(userRegister)