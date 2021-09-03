import sqlite3
from django.shortcuts import render
from bangazonapi.models import Product
from bangazonreports.views import Connection

def productunderthousand_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                p.id AS product_id,
                p.price AS price,
                p.name AS name
            FROM
                bangazonapi_product p
            WHERE
                price < 1000
            """)
            dataset = db_cursor.fetchall()

            lessthanthousand_products = {}

            for row in dataset:
                uid = row["product_id"]

                lessthanthousand_products[uid] = {}
                lessthanthousand_products[uid]["product_id"] = uid
                lessthanthousand_products[uid]["name"] = row["name"]
                lessthanthousand_products[uid]["price"] = row["price"]

            list_of_products_under_thousand = lessthanthousand_products.values()

            template = 'users/list_of_products_under_thousand.html'
            context = {
                'productunderthousand_list':
                list_of_products_under_thousand
            }
            return render(request, template, context)
