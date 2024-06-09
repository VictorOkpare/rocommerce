import json
from django.shortcuts import render
from django.http import JsonResponse
from.models import Products
from django.views.decorators.csrf import csrf_exempt


def getProducts(request):
    if request.method == "GET":
        products = Products.objects.all()
        products_list = list(products.values())
        return JsonResponse({"message": "Get product route is active",
                             "data": products_list})
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)


@csrf_exempt
def addProduct(request):
    if request.method =="POST":
        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)
        

       
        product_name = data_dict.get("name")
        existing_product = Products.objects.filter(name = product_name).first()
        if existing_product:
            return JsonResponse({"Message": "Product with this name already exists"})
        else:
            Products.objects.create(**data_dict)
        
    
        return JsonResponse({"Message": "Post added successfully"}, )
    else:
        return JsonResponse({"ERROR": "Invalid Methos"}, status=405)


@csrf_exempt
def updateProduct(request):
    if request.method == "PUT":
        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)
        
        product_id = data_dict.get("id")
        existing_product = Products.objects.filter(id=product_id).first()
        
        if existing_product:
            existing_product.image_url = data_dict.get("image_url", existing_product.image_url)
            existing_product.type = data_dict.get("type", existing_product.type)
            existing_product.brand = data_dict.get("brand", existing_product.brand)
            existing_product.price = data_dict.get("price", existing_product.price)
            existing_product.description = data_dict.get("description", existing_product.description)
            existing_product.available = data_dict.get("available", existing_product.available)
            existing_product.save()
            
            return JsonResponse({"Message": "Product updated successfully"})
        else:
            return JsonResponse({"Message": "Product with this ID does not exist"})
    else:
        return JsonResponse({"ERROR": "Invalid Method"}, status=405)
    
@csrf_exempt  
def deleteProduct(request):
    if request.method == "DELETE":
        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)
        
        product_name = data_dict.get("name")
        existing_product = Products.objects.filter(name=product_name).first()
        
        if existing_product:
            existing_product.delete()
            return JsonResponse({"Message": "Product deleted successfully"})
        else:
            return JsonResponse({"Message": "Product with this name does not exist"})
    else:
        return JsonResponse({"ERROR": "Invalid Method"}, status=405)
    
    
# @csrf_exempt
# def updateProduct(request):
#     if request.method == "PUT":
#         json_data = request.body.decode("utf-8")
#         data_dict = json.loads(json_data)
        
#         product_name = data_dict.get("name")
#         existing_product = Products.objects.filter(name=product_name).first()
        
#         if existing_product:
#             existing_product.image_url = data_dict.get("image_url", existing_product.image_url)
#             existing_product.type = data_dict.get("type", existing_product.type)
#             existing_product.brand = data_dict.get("brand", existing_product.brand)
#             existing_product.price = data_dict.get("price", existing_product.price)
#             existing_product.description = data_dict.get("description", existing_product.description)
#             existing_product.available = data_dict.get("available", existing_product.available)
#             existing_product.save()
            
#             return JsonResponse({"Message": "Product updated successfully"})
#         else:
#             return JsonResponse({"Message": "Product with this name does not exist"})
#     else:
#         return JsonResponse({"ERROR": "Invalid Method"}, status=405)
  
  
  
  
  
  
  
  
        # Products.objects.create(
        #     name = data_dict["name"],
        #     image_url = data_dict["image_url"],
        #     type = data_dict["type"],
        #     brand = data_dict["brand"],
        #     price = data_dict["price"],
        #     description = data_dict["description"],
        #     available = data_dict["available"],
        # )