"""Module for generating report"""
import sqlite3
from django.shortcuts import render
from bangazonapi.models import Favorite
from bangazonreports.views import Connection

def favoriteseller_list(request):
    """Function to build an HTML report"""
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                    f.id, 
                    f.seller_id,
                    f.customer_id,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM 
                    bangazonapi_favorite f
                JOIN
                    bangazonapi_customer c ON f.customer_id = c.id
                JOIN
                    auth_user u ON c.user_id = u.id;
            """)
            dataset = db_cursor.fetchall()

            favorite_seller = {}

            for row in dataset:
                favorite = Favorite()
                favorite.customer_id = row["customer_id"]
                favorite.seller_id = row["seller_id"]

                uid = row["user_id"]

                if uid in favorite_seller:
                    favorite_seller[uid]['favorites'].append(favorite)

                else:
                    favorite_seller[uid] = {}
                    favorite_seller[uid]["id"] = uid
                    favorite_seller[uid]["full_name"] = row["full_name"]
                    favorite_seller[uid]["favorites"] = [favorite]

            list_of_users_with_favorites = favorite_seller.values()

            template = 'users/list_withFavorites.html'
            context = {
                'favoriteseller_list': list_of_users_with_favorites
            }

            return render(request, template, context)
