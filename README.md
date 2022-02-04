# ProductsAPI - Freshmania 🍏 - Doc  
Endpoints

Method   | Example value
--------- | ------
POST | /products
DELETE | /products/id
GET |  /products
PATCH| /products/id


## POST /products
This endpoint is to create a new product. Body requisition example below
```
{
	"name":"Freshmania",
	"price":12,
	"image":"https://www.publicdomainpictures.net/pictures/320000/nahled/background-image.png"
}
```

If everything goes as planned it will work a answer like this and return a status code of 201
```
{
  "created_at": "04/02/2022 00:21",
  "id": 16,
  "image": "https://www.publicdomainpictures.net/pictures/320000/nahled/background-image.png",
  "name": "Freshmania",
  "price": 12.0,
  "updated_at": null
}
```
## PATCH /products/id
This endpoint is to update an already existing product. You only need to pass the fields that you want to update. For example, i want to update the field name
```
{
    "name":"Inovando"
}
```
It should return the item already updated and the stauts code of 200.

## DELETE /products/id
This endpoint is to delete an product from the database. There's no of a body in the requisition, if works will return the deleted product and the status code 200

## GET  /products
This endpoint is to get all the products from the database. There's no need for a body in the requisition and it will return a list of products and the status code 200

