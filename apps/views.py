import json
from os.path import join

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from matplotlib.pyplot import title

from apps.models import Project, Order, Film, Todo
from config.settings import BASE_DIR


def products_list(request):
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    return JsonResponse({'message': products})


def query_product_id(request):
    _id = request.GET.get('id')
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f).get('products')
    for product in products:
        if int(product.get('id')) == int(_id):
            return JsonResponse({"message": product})
    return JsonResponse({"message": "Not found product."})


def path_product_id(request, _id: int):
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f).get('products')
    for product in products:
        if product.get('id') == _id:
            return JsonResponse({"message": product})
    return JsonResponse({"message": "Not found product"})


def query_product_category(request):
    category = request.GET.get('category')
    result = []
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f).get('products')
    for product in products:
        if product.get('category') == category:
            result.append(product)
    return JsonResponse({"message": result})


def path_product_category(request, category):
    # category = request.GET.get('category')
    result = []
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f).get('products')
    for product in products:
        if product.get('category') == category:
            result.append(product)
    return JsonResponse({"message": result})


def query_add_product(request):
    title = request.GET.get('title')
    price = request.GET.get('price')
    description = request.GET.get('description')
    category = request.GET.get('category')
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    _id = 1 if not products else products[-1].get('id', 0) + 1
    new_product = {
        'id': _id,
        'title': title,
        'price': price,
        'description': description,
        'category': category,
    }
    products.append(new_product)
    with open(join(BASE_DIR, 'dummy', 'products.json'), 'w') as f:
        json.dump(products, f, indent=4)
    return JsonResponse({"message": products})


def path_add_product(request, title, price, description, category):
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    _id = 1 if not products else products[-1].get('id', 0) + 1
    new_product = {
        'id': _id,
        'title': title,
        'price': price,
        'description': description,
        'category': category,
    }
    products.append(new_product)
    with open(join(BASE_DIR, 'dummy', 'products.json'), 'w') as f:
        json.dump(products, f, indent=4)
    return JsonResponse({"message": products})


def query_product_update(request):
    price = request.GET.get('price')
    _id = request.GET.get('id')
    result = {}
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    for product in products:
        if int(product.get('id')) == int(_id):
            product['price'] = float(price)
            result = product
            break
    else:
        return JsonResponse({'message': "Not found product!"})
    with open(join(BASE_DIR, 'dummy', 'products.json'), 'w') as f:
        json.dump(products, f, indent=4)
    return JsonResponse(result)


def path_product_update(request, _id, title):
    result = {}
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    for product in products:
        if int(product.get('id')) == int(_id):
            product['title'] = title
            result = product
            break
    else:
        return JsonResponse({'message': "Not found product!"})
    with open(join(BASE_DIR, 'dummy', 'products.json'), 'w') as f:
        json.dump(products, f, indent=4)
    return JsonResponse(result)


def query_product_delete(request):
    _id = request.GET.get('id')
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    for index, product in enumerate(products):
        if int(product.get('id')) == int(_id):
            products.pop(index)
            with open(join(BASE_DIR, 'dummy', 'products.json'), 'w') as f:
                json.dump(products, f, indent=4)
            return JsonResponse({'message': "Mahsulot o'chirildi"})
    return JsonResponse({'message': "Not found product."})


def path_product_delete(request, _id: int):
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    for index, product in enumerate(products):
        if product.get('id') == _id:
            products.pop(index)
            with open(join(BASE_DIR, 'dummy', 'products.json'), 'w') as f:
                json.dump(products, f, indent=4)
            return JsonResponse({'message': "Mahsulot o'chirildi"})
    return JsonResponse({'message': "Not found product."})


def query_product_discount(request):
    discount = request.GET.get('discount')
    result = []
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    for product in products:
        if float(product.get('discountPercentage')) > int(discount):
            result.append(product)
    return JsonResponse(result)


def user_list(request):
    users = User.objects.all()
    return render(request, 'lesson2/users-list.html', context={"users": users})


def project_list(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'lesson2/products-list.html', context)


def home_user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'lesson2/homework/user-list.html', context)


def home_event_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'lesson2/homework/event-list.html', context)


def home_order_list(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, 'lesson2/homework/order-list.html', context)


def index_1(request):
    return render(request, 'lesson_3/index1.html')


def index_2(request, num):
    return render(request, 'lesson_3/index2.html')


def film_from(request):
    if request.method == 'GET':
        return render(request, 'lesson_4/film-from.html')
    if request.method == 'POST':
        post = request.POST
        title = post.get('title')
        video = post.get('video')
        image = post.get('images')
        duration = post.get('duration')
        Film.objects.create(title=title, video=video, main_image=image, duration=duration)
        return render(request, 'lesson_4/film-from.html')


def todo_from(request):
    # return render(request, 'lesson_4/todo-list.html')
    if request.GET == 'GET':
        return render(request, 'lesson_4/todo-list.html')
    if request.POST == 'POST':
        # name = request.POST.get('name')
        # Todo.objects.create(name=name)
        return render(request, 'lesson_4/todo-list.html')

