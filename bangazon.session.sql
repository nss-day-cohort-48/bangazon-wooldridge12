

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



            SELECT
                o.id AS orderId,
                u.id user_id,
                c.id,
                u.first_name || ' ' || u.last_name AS full_name,
                SUM(p.price) AS total_price,
                COUNT(op.id) AS oder_product_id
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
                payments NOT LIKE NULL
            GROUP BY 
                orderId;

             SELECT
                o.id AS orderId,
                u.id user_id,
                c.id,
                SUM(p.price) AS total_price,
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

            SELECT
                o.id AS orderId,
                u.id user_id,
                c.id,
                SUM(p.price) AS total_price,
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
                payments IS NOT NULL
            GROUP BY
                orderId;

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
                
            SELECT
                p.id AS product_id,
                p.price AS price,
                p.name AS name
            FROM
                bangazonapi_product p
            WHERE
                price < 1000
