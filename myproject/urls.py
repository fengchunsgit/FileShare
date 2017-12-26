from django.conf.urls import include, url
from django.contrib import admin
from Share.views import HomeView,DisplayView

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(),name="home"),
    url(r'^s/(?P<code>\d+)/$', HomeView.as_view(),name="home"),#/s/(?P<code>\d+ 使用了组匹配的方式 匹配code任意长度的数字，如/s/123456，将123456传给 DisplayView,这里的 code 必须和视图函数的 code 保持一致。


]
