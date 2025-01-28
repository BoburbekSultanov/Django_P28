from django.urls import path
from django.conf.urls.static import static


from apps.views import products_list, query_product_id, path_product_id, query_product_category, path_product_category, \
    query_add_product, path_add_product, query_product_update, path_product_update, query_product_delete, \
    path_product_delete, query_product_discount, user_list, project_list
from config.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('api/products/', products_list),
    path('api/products/id/', query_product_id),
    path('api/products/id/<int:_id>', path_product_id),
    path('api/products/category/', query_product_category),
    path('api/products/category/<str:category>', path_product_category),
    path('api/products/add/', query_add_product),
    path('api/products/add/<str:title>/<int:price>/<str:description>/<str:category>/', path_add_product),
    path('api/products/update/', query_product_update),
    path('api/products/update/<int:_id>/<str:title>/', path_product_update),
    path('api/products/delete/', query_product_delete),
    path('api/products/delete/<int:_id>', path_product_delete),
    path('api/products/discount/', query_product_discount),
    path('user/list/', user_list),
    path('project/list/', project_list),
]
