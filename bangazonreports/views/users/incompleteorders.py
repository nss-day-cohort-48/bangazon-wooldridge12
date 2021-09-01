"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from bangazonapi.models import Favorite
from bangazonreports.views import Connection

def incompleteorder_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                o.id AS orderId,
                u.id user_id,
                c.id,
                SUM(p.price),
                o.payment_type_id AS payments,
                u.first_name || ' ' || u.last_name AS full_name
            FROM
                bangazonapi_order o
            JOIN
                bangazonapi_customer c ON o.customer_id = c.id
            JOIN
                auth_user u ON c.user_id = u.id
            LEFT JOIN 
                bangazonapi_orderproduct op ON o.id= op.order_id 
            LEFT JOIN 
                bangazonapi_product p ON op.product_id = p.id
            WHERE
                payments IS NULL
            GROUP BY
                orderId;
            """)
            dataset = db_cursor.fetchall()

            incomplete_orders = {}

            for row in dataset:
                order = order()
                order.
