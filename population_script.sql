INSERT INTO user_profile (user, first_name, last_name, phone_number, date_of_birth, profile_picture, bio) VALUES (1, 'Birna', 'Karlsdottir', '777-7000', '15.06.1990', 'https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_07/2233721/171120-smile-stock-njs-333p.jpg', 'I am very loyal');
INSERT INTO user_profile (user, first_name, last_name, phone_number, date_of_birth, profile_picture, bio) VALUES (2, 'Helena', 'Agustsdottir', '777-9000', '07.10.2000', 'https://www.scienceabc.com/wp-content/uploads/ext-www.scienceabc.com/wp-content/uploads/2015/10/smile-2.jpg-.jpg', 'I love animals and am very caring');
INSERT INTO user_profile (user, first_name, last_name, phone_number, date_of_birth, profile_picture, bio) VALUES (3, 'Birta', 'Hlidkvist', '777-8000', '22.08.1990', 'https://images.indianexpress.com/2019/04/smiling759_getty.jpg', 'My hobby is bird watching');

INSERT INTO item_itemcategory (name) VALUES ('All products');
INSERT INTO item_itemcategory (name) VALUES ('Electronics');
INSERT INTO item_itemcategory (name) VALUES ('Clothing');
INSERT INTO item_itemcategory (name) VALUES ('Furniture');
INSERT INTO item_itemcategory (name) VALUES ('Other');


INSERT INTO item_item (name, description, condition, category_id, seller_id) VALUES ('Iphone', 'black iphone 11', 'very good, no cracks', 2, 1);
INSERT INTO item_item (name, description, condition, category_id, seller_id) VALUES ('Bike', 'red racer', 'nice', 5, 2);
INSERT INTO item_item (name, description, condition, category_id, seller_id) VALUES ('Macbook', 'grey macbook pro 13', 'bad condition', 2, 3);
INSERT INTO item_item (name, description, condition, category_id, seller_id) VALUES ('Mic', 'cordless', 'very good', 2, 2);
INSERT INTO item_item (name, description, condition, category_id, seller_id) VALUES ('Sweater', 'pink knit', 'medium', 3, 1);


INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (100, 1, 8);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (1000, 2, 9);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (2500, 3, 9);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (1000, 1, 7);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (50, 1, 8);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (3000, 2, 9);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (900, 3, 10);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (1000, 1, 11);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (10200, 3, 17);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (10300, 1, 20);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (100, 7, 26);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (12200, 1, 7);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (540, 1, 8);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (30500, 2, 9);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (90, 3, 10);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (100, 1, 11);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (1000, 3, 17);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (10300, 1, 20);
INSERT INTO item_bid (amount, buyer_id, item_id) VALUES (14000, 7, 26);

INSERT INTO checkout_checkout (full_name, street_name, house_number, postal_code, city, country, cardholder_name, cardnumber, expiration_date, cvc, payment_date, total_amount, user_id, item_id) VALUES ('Jón Jónsson', 'Menntavegur', '1', '102', 'Reykjavik', 'Iceland', 'Birna Rún Karlsdóttir', '1111-11-111111', '07/27', '111', '01.05.20222', 10000, 1, 20);
INSERT INTO checkout_checkout (full_name, street_name, house_number, postal_code, city, country, cardholder_name, cardnumber, expiration_date, cvc, payment_date, total_amount, user_id, item_id) VALUES ('Gunnar Gunnarsson', 'Bjarmaland', '0', '108', 'Reykjavik', 'Iceland', 'Birna Rún Karlsdóttir', '1111-11-111111', '07/27', '111', '01.05.20222', 20000, 1, 30);

INSERT INTO checkout_rating (seller_id, rating) VALUES (1, 6);
INSERT INTO checkout_rating (seller_id, rating) VALUES (2, 9);
INSERT INTO checkout_rating (seller_id, rating) VALUES (2, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (5, 8);
INSERT INTO checkout_rating (seller_id, rating) VALUES (1, 6);
INSERT INTO checkout_rating (seller_id, rating) VALUES (2, 9);
INSERT INTO checkout_rating (seller_id, rating) VALUES (3, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (4, 8);
INSERT INTO checkout_rating (seller_id, rating) VALUES (5, 6);
INSERT INTO checkout_rating (seller_id, rating) VALUES (6, 9);
INSERT INTO checkout_rating (seller_id, rating) VALUES (7, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (1, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (2, 8);
INSERT INTO checkout_rating (seller_id, rating) VALUES (3, 1);
INSERT INTO checkout_rating (seller_id, rating) VALUES (4, 3);
INSERT INTO checkout_rating (seller_id, rating) VALUES (5, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (6, 7);
INSERT INTO checkout_rating (seller_id, rating) VALUES (7, 1);
INSERT INTO checkout_rating (seller_id, rating) VALUES (3, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (3, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (1, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (2, 10);
INSERT INTO checkout_rating (seller_id, rating) VALUES (3, 10);

INSERT INTO item_images (item_id, image) VALUES (7, 'https://images.hindustantimes.com/tech/img/2021/12/21/960x540/iPhone_13_Mini_(9)_1632560822480_1640057457018.jpg')
INSERT INTO item_images (item_id, image) VALUES (7, 'https://images.hindustantimes.com/tech/img/2022/03/16/960x540/iPhone_13_Mini_(10)_1633111870000_1647407172205.jpg')
INSERT INTO item_images (item_id, image) VALUES (8, 'https://vintage-vendor.com/wp-content/gallery/vintage-racing-bikes/vintage-racing-bike-9.jpg')
INSERT INTO item_images (item_id, image) VALUES (9, 'https://149426355.v2.pressablecdn.com/wp-content/uploads/2020/05/13pro-keyboard.jpg')
INSERT INTO item_images (item_id, image) VALUES (9, 'https://i.insider.com/5eb3ff15fc593d5396502623?width=750&format=jpeg&auto=webp')
INSERT INTO item_images (item_id, image) VALUES (9, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR44_0sh9xG8hwhjNGfyvLdvAlbYZR-0T1DfS8xtKeqe2nDO715wiTHtHruyIcdxZdEnDA&usqp=CAU')
INSERT INTO item_images (item_id, image) VALUES (10, 'https://m.media-amazon.com/images/I/41GrPyMMjlL.jpg')
INSERT INTO item_images (item_id, image) VALUES (10, 'https://www.marcotec-shop.com/pub/media/catalog/product/cache/815b290a519d918302a1a2945471f3a8/s/e/sennheiser_xsw2-835_1.jpg')
INSERT INTO item_images (item_id, image) VALUES (10, 'https://assets.fatllama.com/images/medium/sennheiser-g3-handheld-wireless-microphone--receiver-21050828.jpg')
INSERT INTO item_images (item_id, image) VALUES (11, 'https://di2ponv0v5otw.cloudfront.net/posts/2022/04/02/624894c2691412e8b215c421/s_624894f7463d4fa9c0a3ef6e.jpg')
INSERT INTO item_images (item_id, image) VALUES (11, 'https://i.etsystatic.com/12131993/r/il/c2ffe7/3574192585/il_340x270.3574192585_7iie.jpg')


