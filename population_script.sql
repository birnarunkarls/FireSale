INSERT INTO fire_sale_about (phone_number, email, address) VALUES ('666-6666', 'bestbids@bestbids.com', 'Menntavegur 1');


INSERT INTO user_profile (bio, user_id, date_of_birth, phone_number, profile_picture) VALUES ('I am very loyal', 1, '15.06.1990', '777-7000', 'IMG');


INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id_id) VALUES ('Iphone', 'black iphone 11', 'very good, no cracks', 'electronics', 'IMG', 'SÆKJA', 1);
INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id_id) VALUES ('Bike', 'red racer', 'nice', 'other', 'IMG', 'SÆKJA', 1);
INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id_id) VALUES ('Macbook', 'grey macbook pro 13', 'bad condition', 'electronics', 'IMG', 'SÆKJA', 1);
INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id_id) VALUES ('Mic', 'cordless', 'very good', 'electronics', 'IMG', 'SÆKJA', 1);
INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id_id) VALUES ('Sweater', 'pink knit', 'medium', 'clothing', 'IMG', 'SÆKJA', 1);


INSERT INTO item_bid (amount, notification, buyer_id_id, item_id_id) VALUES ('100', 'text_message', 1, 19);
INSERT INTO item_bid (amount, notification, buyer_id_id, item_id_id) VALUES ('1000', 'push_notification', 2, 21);
INSERT INTO item_bid (amount, notification, buyer_id_id, item_id_id) VALUES ('2500', 'text_message', 1, 22);


INSERT INTO checkout_payment (cardholder_name, cardnumber, expiration_date, cvc, payment_date, total_amoun) VALUES ('Jón Jónsson', '1111-11-111111', '07/27', '111', '01.05.20222', '10000');
INSERT INTO checkout_payment (cardholder_name, cardnumber, expiration_date, cvc, payment_date, total_amoun) VALUES ('Gunnar Gunnarsson', '2222-11-222222', '02/25', '123', '05.05.20222', '2000');


INSERT INTO checkout_shipping (method, full_name, street_name, house_numer, postal_code, city, country) VALUES ('standard_shipping', 'Jón Jónsson', 'Menntavegur', '1', '102', 'Reykjavik', 'Iceland');
INSERT INTO checkout_shipping (method, full_name, street_name, house_numer, postal_code, city, country) VALUES ('standard_shipping', 'Gunnar Gunnarsson', 'Laugarvegur', '1', '101', 'Reykjavik', 'Iceland');

