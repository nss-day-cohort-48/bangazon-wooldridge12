import sqlite3
from django.shortcuts import render
from bangazonapi.models import Order
from bangazonreports.views import Connection

def completeorder_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                o.id AS orderId,
                u.id user_id,
                c.id,
                pt.merchant_name AS payment_type,
                SUM(p.price) AS total_price,
                o.payment_type_id AS payments,
                u.first_name || ' ' || u.last_name AS full_name
            FROM
                bangazonapi_order o
            JOIN
                bangazonapi_customer c ON o.customer_id = c.id
            JOIN
                auth_user u ON c.user_id = u.id
            JOIN
                bangazonapi_payment pt ON pt.customer_id = c.id
            LEFT JOIN 
                bangazonapi_orderproduct op ON o.id= op.order_id 
            LEFT JOIN 
                bangazonapi_product p ON op.product_id = p.id
            WHERE
                payments IS NOT NULL
            GROUP BY
                orderId;
            """)
            dataset = db_cursor.fetchall()

            complete_orders = {}

            for row in dataset:
                uid = row["orderId"]

                complete_orders[uid] = {}
                complete_orders[uid]["order_id"] = uid
                complete_orders[uid]["full_name"] = row["full_name"]
                complete_orders[uid]["total_price"] = row["total_price"]
                complete_orders[uid]["payment_type"] = row["payment_type"]

            list_of_complete_orders = complete_orders.values()

            template = 'users/list_of_complete_orders.html'
            context = {
                'completeorder_list':
                list_of_complete_orders
            }
            return render(request, template, context)
                