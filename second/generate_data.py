from django.http import HttpResponse

from second.models import Organization

def generate_fake_data(request):
    for i in range(100):
        Organization.objects.create(country='Russia',
                                    owner_name='Owner',
                                    org_name='Organization'+str(i),
                                    location='Moscow',
                                    site='example.com',
                                    contact_person='Person'+str(i),
                                    email='example@email.com',
                                    inst_type='type' + str(i),
                                    short_description_org='short_description_org',
                                    short_description_infr='short_description_infr',
                                    sci_area='sci_area',
                                    activities='activities',
                                    conditions_on_access='conditions_on_access',
                                    restrictions='restrictions',
                                    inter_cooperation='inter_cooperation',
                                    lat=55.751574- i/10,
                                    lon=37.573856 - i/10
                                    )
    return HttpResponse('Ok')