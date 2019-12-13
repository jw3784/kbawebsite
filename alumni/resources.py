
from import_export import resources, fields

from alumni.models import alumnus

class alumnusResource(resources.ModelResource):

    class Meta:
        model = alumnus
        exclude = ('id')
        fields = ('name', 'a_class', 'a_company', 'a_title', 'a_field', 'a_email', 'a_city', 'a_country', 'id')