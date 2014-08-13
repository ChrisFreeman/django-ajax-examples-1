from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jqtest.views.home', name='home'),
    url(r'^jq_example1/$', 'jqtest.views.jq_example1', name='jq_example1'),
    url(r'^jq_example2_edit_text/$', 'jqtest.views.jq_example2_edit_text', name='jq_example2_edit'),
    url(r'^jq_example2_submit/$', 'jqtest.views.jq_example2_submit', name='jq_example2_submit'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
