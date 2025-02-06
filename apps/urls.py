from django.urls import path
from django.conf.urls.static import static

from apps.views import products_list, query_product_id, path_product_id, query_product_category, path_product_category, \
    query_add_product, path_add_product, query_product_update, path_product_update, query_product_delete, \
    path_product_delete, query_product_discount, user_list, project_list, home_user_list, home_event_list, \
    home_order_list, index_1, index_2, film_from, todo_from

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
    path('home/user/list/', home_user_list),
    path('home/event/list/', home_event_list),
    path('home/order/list/', home_order_list),
    path('index1/', index_1, name='index1'),
    path('index2/<int:num>', index_2, name='index2'),
    path('film/from', film_from, name='filmfrom'),
    path('todo/list/', todo_from, name='todo'),
]
