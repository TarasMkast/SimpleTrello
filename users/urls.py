from django.urls import path
from django.contrib.auth import views
from users.views import RegisterFormView

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

def check(request, uuid_code, action):
    if action in ['yes', 'no'] and uuid_code:
        try:
            sympathy_check_record = SympathyCheck.objects.get(unique_uuid=uuid_code)
            # Setting lang to en
            request.LANGUAGE_CODE = 'en'
            # Checking lang
            if sympathy_check_record.language_to_response == 'de':
                request.LANGUAGE_CODE = 'de'
            sympathy_check_record.positive_response = False
            if action == 'yes':
                man_object = ManUserProxy.objects.get(pk=sympathy_check_record.man.id)
                print(man_object)
                sympathy_check_record.positive_response = True
                plaintext = get_template('sympathy_response.txt')
                text_content = plaintext.render({'username': 'TestUser'})

                host = request.is_secure() and "https" or "http"
                host += '://' + request.get_host()

                host = HostInfo(request).get_host()

                html_content = render_to_string('sympathy_response.html', {
                    'man_object': man_object,
                    'woman_object': sympathy_check_record.woman,
                    'host': host,
                    'lang_code': request.LANGUAGE_CODE,
                })
                subject = 'Hello!'
                msg = EmailMultiAlternatives(subject=subject, body=text_content, to=['roman.krasnyak@gmail.com',
                                                                                     'taras.baziv@gmail.com',
                                                                                     sympathy_check_record.woman.email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            sympathy_check_record.save()
            return HttpResponseRedirect('/')
        except SympathyCheck.DoesNotExist:
            return HttpResponse('Not found!', status=404)