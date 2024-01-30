from django.contrib import admin
from django.urls import path , include , re_path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView

# from rest_framework_swagger.views import get_swagger_view

urlpatterns         = [ path('admin/', admin.site.urls),]

API_Title           = 'Medi-Manager APIs'

schema_view         = get_schema_view(title=API_Title)
# swagger_schema_view = get_swagger_view(title=API_Title)



urlpatterns = [
    path('admin/',  admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),

    # Medi-Manager all APIs from V1 listed hereby :
    path('api/v1/activity-mapping/' ,      include('activity_mapping.urls')),
    path('api/v1/appointment/' ,             include('appointment.urls')),
    path('api/v1/consultation/' ,            include('consultation.urls')),
    path('api/v1/consultation-symptom/' ,    include('consultation_symptom.urls')),
    path('api/v1/consultation-medicine/' ,   include('consultation_medicine.urls')),
    path('api/v1/consultation-instruction/', include('consultation_instruction.urls')),
    path('api/v1/component/' ,              include('component.urls')),
    path('api/v1/entity-type/' ,            include('entity_type.urls')),
    path('api/v1/entity/' ,                 include('entity.urls')),
    path('api/v1/medicine-master/',         include('medicine_master.urls')),
    path('api/v1/vital-master/',            include('vital_master.urls')),
    path('api/v1/patient-vital/',           include('patient_vital.urls')),
    path('api/v1/procedure/' ,              include('procedure.urls')),
    path('api/v1/role/' ,                   include('role.urls')),
    path('api/v1/specialization/',          include('specialization.urls')),
    path('api/v1/specialization-procedure/',include('specialization_procedure_mapping.urls')),
    path('api/v1/specialization-workflow/', include('specialization_workflow_mapping.urls')),
    path('api/v1/symptom-master/',          include('symptom_master.urls')),
    path('api/v1/template-master/',         include('template_master.urls')),
    path('api/v1/test-report/',             include('test_report.urls')),
    path('' ,                   include('user.urls')),
    path('api/v1/user-entity-mapping/' ,    include('user_entity_mapping.urls')),
    path('api/v1/user-specialization-procedure/', include('user_specialization_procedure_mapping.urls')),
    path('api/v1/user-role-mapping/' ,      include('user_role_mapping.urls')),
    path('api/v1/workflow/' ,               include('workflow.urls')),
    path('api/v1/workflow-component/' ,     include('workflow_component_mapping.urls')),

    path('api-auth/',               include('rest_framework.urls')),
    path('docs/',                   include_docs_urls(title= API_Title)),
    path('schema/',                 schema_view),
    # path('api/v1/swagger/',         swagger_schema_view)
    
    ]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]