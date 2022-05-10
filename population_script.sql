INSERT INTO user_profile (user, first_name, last_name, phone_number, date_of_birth, profile_picture, bio) VALUES (1, 'Birna', 'Karlsdottir', '777-7000', '15.06.1990', 'https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_07/2233721/171120-smile-stock-njs-333p.jpg', 'I am very loyal');
INSERT INTO user_profile (user, first_name, last_name, phone_number, date_of_birth, profile_picture, bio) VALUES (2, 'Helena', 'Agustsdottir', '777-9000', '07.10.2000', 'https://www.scienceabc.com/wp-content/uploads/ext-www.scienceabc.com/wp-content/uploads/2015/10/smile-2.jpg-.jpg', 'I love animals and am very caring');
INSERT INTO user_profile (user, first_name, last_name, phone_number, date_of_birth, profile_picture, bio) VALUES (3, 'Birta', 'Hlidkvist', '777-8000', '22.08.1990', 'https://images.indianexpress.com/2019/04/smiling759_getty.jpg', 'My hobby is bird watching');

INSERT INTO item_item (name, description, condition, category, highest_bid, seller_id) VALUES ('Iphone', 'black iphone 11', 'very good, no cracks', 'electronics', 0, 1);
INSERT INTO item_item (name, description, condition, category, highest_bid, seller_id) VALUES ('Bike', 'red racer', 'nice', 'other', 0, 2);
INSERT INTO item_item (name, description, condition, category, highest_bid, seller_id) VALUES ('Macbook', 'grey macbook pro 13', 'bad condition', 'electronics', 0, 3);
INSERT INTO item_item (name, description, condition, category, highest_bid, seller_id) VALUES ('Mic', 'cordless', 'very good', 'electronics', 0, 2);
INSERT INTO item_item (name, description, condition, category, highest_bid, seller_id) VALUES ('Sweater', 'pink knit', 'medium', 'clothing', 0, 1);

INSERT INTO item_bid (amount, notification, buyer_id, item_id) VALUES (100, 'text_message', 1, 3);
INSERT INTO item_bid (amount, notification, buyer_id, item_id) VALUES (1000, 'push_notification', 2, 2);
INSERT INTO item_bid (amount, notification, buyer_id, item_id) VALUES (2500, 'text_message', 3, 2);


INSERT INTO checkout_payment (cardholder_name, cardnumber, expiration_date, cvc, payment_date, total_amount) VALUES ('Jón Jónsson', '1111-11-111111', '07/27', '111', '01.05.20222', 10000);
INSERT INTO checkout_payment (cardholder_name, cardnumber, expiration_date, cvc, payment_date, total_amount) VALUES ('Gunnar Gunnarsson', '2222-11-222222', '02/25', '123', '05.05.20222', 2000);

INSERT INTO checkout_shipping (method, full_name, street_name, house_number, postal_code, city, country) VALUES ('standard_shipping', 'Jón Jónsson', 'Menntavegur', '1', '102', 'Reykjavik', 'Iceland');
INSERT INTO checkout_shipping (method, full_name, street_name, house_number, postal_code, city, country) VALUES ('standard_shipping', 'Gunnar Gunnarsson', 'Laugarvegur', '1', '101', 'Reykjavik', 'Iceland');


INSERT INTO item_images (item_id, image) VALUES (2, 'https://images.hindustantimes.com/tech/img/2021/12/21/960x540/iPhone_13_Mini_(9)_1632560822480_1640057457018.jpg')
INSERT INTO item_images (item_id, image) VALUES (2, 'https://images.hindustantimes.com/tech/img/2022/03/16/960x540/iPhone_13_Mini_(10)_1633111870000_1647407172205.jpg')
INSERT INTO item_images (item_id, image) VALUES (3, 'https://vintage-vendor.com/wp-content/gallery/vintage-racing-bikes/vintage-racing-bike-9.jpg')
INSERT INTO item_images (item_id, image) VALUES (4, 'https://149426355.v2.pressablecdn.com/wp-content/uploads/2020/05/13pro-keyboard.jpg')
INSERT INTO item_images (item_id, image) VALUES (4, 'https://i.insider.com/5eb3ff15fc593d5396502623?width=750&format=jpeg&auto=webp')
INSERT INTO item_images (item_id, image) VALUES (4, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR44_0sh9xG8hwhjNGfyvLdvAlbYZR-0T1DfS8xtKeqe2nDO715wiTHtHruyIcdxZdEnDA&usqp=CAU')
INSERT INTO item_images (item_id, image) VALUES (5, 'https://m.media-amazon.com/images/I/41GrPyMMjlL.jpg')
INSERT INTO item_images (item_id, image) VALUES (5, 'https://www.marcotec-shop.com/pub/media/catalog/product/cache/815b290a519d918302a1a2945471f3a8/s/e/sennheiser_xsw2-835_1.jpg')
INSERT INTO item_images (item_id, image) VALUES (5, 'https://assets.fatllama.com/images/medium/sennheiser-g3-handheld-wireless-microphone--receiver-21050828.jpg')
INSERT INTO item_images (item_id, image) VALUES (6, 'https://di2ponv0v5otw.cloudfront.net/posts/2022/04/02/624894c2691412e8b215c421/s_624894f7463d4fa9c0a3ef6e.jpg')
INSERT INTO item_images (item_id, image) VALUES (6, 'https://i.etsystatic.com/12131993/r/il/c2ffe7/3574192585/il_340x270.3574192585_7iie.jpg')


