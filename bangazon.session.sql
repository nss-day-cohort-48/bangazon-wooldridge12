

                SELECT
                    f.id, 
                    f.seller_id,
                    f.customer_id,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM 
                    bangazonapi_favorite f
                JOIN
                    bangazonapi_customer c ON f.customer_id 
                JOIN
                    auth_user u ON c.user_id = u.id
                    