
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from olcha.views import CategoryListCreateView, CategoryDetailView, ProductDetailView, \
    GroupListCreateView, GroupDetailView, ProductListCreateView, \
    ImageListApiView, AttributeKeyListCreateView, AttributeValueListCreateView, ProductAttributeListCreateView, \
    RegisterView, CustomAuthToken, LogoutView

urlpatterns = [
    path('api/category/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('api/category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('api/category/<slug:category_slug>/group/', GroupListCreateView.as_view(), name='group_list_create'),
    path('api/category/<slug:category_slug>/group/<slug:slug>/', GroupDetailView.as_view(), name='group_detail'),
    path('api/category/<slug:category_slug>/group/<slug:group_slug>/product/', ProductListCreateView.as_view(),
         name='product_list_create'),
    path('api/category/<slug:category_slug>/group/<slug:group_slug>/product/<slug:slug>/', ProductDetailView.as_view(),
         name='product_detail'),
    path('all-images/', ImageListApiView.as_view(), name='all_images'),
    path('api/attribute-keys/', AttributeKeyListCreateView.as_view(), name='attribute_key_list_create'),
    path('api/attribute-values/', AttributeValueListCreateView.as_view(), name='attribute_value_list_create'),
    path('api/product-attributes/', ProductAttributeListCreateView.as_view(), name='product_attribute_list_create'),
    path('api-token/',obtain_auth_token),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


]
