import json
from os.path import join

from config.settings import BASE_DIR


def products_list():
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f).get('products')
    return products


# print(products_list()[1])


def query_product_id(_id: str):
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    for product in products:
        if product.get('id') == _id:
            return product
    return 'salom'


# print(query_product_id('3'))


# def query_product_category(category):
#     # category = request.GET.get('category')
#     result = []
#     with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
#         products = json.load(f).get('products')
#     for product in products:
#         if product.get('category') == category:
#             result.append(JsonResponse({"message": product}))
#     return JsonResponse({"message":result})


def query_add_product(title, price, description, category):
    # title = request.GET.get('title')
    # price = request.GET.get('price')
    # description = request.GET.get('description')
    # category = request.GET.get('category')
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f).get('products')
    print(type(products))
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
    return products


# print(query_add_product('yangi mahsulot', 123, 'asfsdfs', 'dfdgsdf'))


def test(id):
    with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
        products = json.load(f)
    for product in products:
        if product.get('id') == id:
            pass
    print(*products)


test(1)
