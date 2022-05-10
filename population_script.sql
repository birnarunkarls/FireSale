INSERT INTO user_profile (user, phone_number, date_of_birth, profile_picture, bio) VALUES (1, '777-7000', '15.06.1990', 'https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_07/2233721/171120-smile-stock-njs-333p.jpg', 'I am very loyal');
INSERT INTO user_profile (user, phone_number, date_of_birth, profile_picture, bio) VALUES (1, '777-7000', '15.06.1990', 'https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_07/2233721/171120-smile-stock-njs-333p.jpg', 'I am very loyal');

INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id) VALUES ('Iphone', 'black iphone 11', 'very good, no cracks', 'electronics', 'IMG', 'SÆKJA', 1);
INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id) VALUES ('Bike', 'red racer', 'nice', 'other', 'IMG', 'SÆKJA', 1);
INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id) VALUES ('Macbook', 'grey macbook pro 13', 'bad condition', 'electronics', 'IMG', 'SÆKJA', 1);
INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id_id) VALUES ('Mic', 'cordless', 'very good', 'electronics', 'IMG', 'SÆKJA', 1);
INSERT INTO item_item (name, description, condition, category, image, highest_bid, seller_id_id) VALUES ('Sweater', 'pink knit', 'medium', 'clothing', 'IMG', 'SÆKJA', 1);


INSERT INTO item_bid (amount, notification, buyer_id_id, item_id_id) VALUES ('100', 'text_message', 1, 19);
INSERT INTO item_bid (amount, notification, buyer_id_id, item_id_id) VALUES ('1000', 'push_notification', 2, 21);
INSERT INTO item_bid (amount, notification, buyer_id_id, item_id_id) VALUES ('2500', 'text_message', 1, 22);


INSERT INTO checkout_payment (cardholder_name, cardnumber, expiration_date, cvc, payment_date, total_amoun) VALUES ('Jón Jónsson', '1111-11-111111', '07/27', '111', '01.05.20222', '10000');
INSERT INTO checkout_payment (cardholder_name, cardnumber, expiration_date, cvc, payment_date, total_amoun) VALUES ('Gunnar Gunnarsson', '2222-11-222222', '02/25', '123', '05.05.20222', '2000');


INSERT INTO checkout_shipping (method, full_name, street_name, house_numer, postal_code, city, country) VALUES ('standard_shipping', 'Jón Jónsson', 'Menntavegur', '1', '102', 'Reykjavik', 'Iceland');
INSERT INTO checkout_shipping (method, full_name, street_name, house_numer, postal_code, city, country) VALUES ('standard_shipping', 'Gunnar Gunnarsson', 'Laugarvegur', '1', '101', 'Reykjavik', 'Iceland');


INSERT INTO item_images (item_id, image) VALUES (19, 'https://images.hindustantimes.com/tech/img/2021/12/21/960x540/iPhone_13_Mini_(9)_1632560822480_1640057457018.jpg')
INSERT INTO item_images (item_id, image) VALUES (19, 'https://images.hindustantimes.com/tech/img/2022/03/16/960x540/iPhone_13_Mini_(10)_1633111870000_1647407172205.jpg')






