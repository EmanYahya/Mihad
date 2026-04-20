PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(20) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	password VARCHAR(60) NOT NULL, 
	birthday DATETIME NOT NULL, 
	gender VARCHAR(10) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
INSERT INTO user VALUES(1,'van','p@f.com','$2b$12$SzAPbLWes61g6YJwc.68kemwnGq1tPL4hoGDm2uz/i57PxYU5EdnO','2020-06-10 00:00:00.000000','Female');
INSERT INTO user VALUES(2,'abel','abelmesfin555@gmail.com','$2b$12$M48Ea2S2EvlNHNFC6axsYORKa5d.pewOrCDNC4OsJ9ctSMLiKgHI.','2023-01-26 21:03:44.145142','Female');
INSERT INTO user VALUES(3,'yidu','yidu@gmail.com','$2b$12$BiukT4vAvHqDSPziCJHfIeudY58yNqZYCOM2w1BPuF./8j/1LAwY2','2023-02-21 12:29:09.724244','Female');
INSERT INTO user VALUES(4,'yid','yiu@gmail.com','$2b$12$2wpFzypE/QGybZzaV6pVdunK9wm00f9J2mXpitvETncfx7tvinNjK','2023-02-21 12:30:07.668452','Female');
CREATE TABLE category (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO category VALUES(1,'Fragrance');
INSERT INTO category VALUES(2,'Men');
INSERT INTO category VALUES(3,'Women');
CREATE TABLE infor (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	address VARCHAR(100) NOT NULL, 
	country VARCHAR(100) NOT NULL, 
	city VARCHAR(100) NOT NULL, 
	postcode VARCHAR(100) NOT NULL, 
	phone VARCHAR(100) NOT NULL, 
	order_date DATETIME NOT NULL, 
	total_price INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO infor VALUES(1,'Van Cao','Dao Duy Tu','Italy','HoChiMinh','70000','6969696969','2020-06-21 15:06:32.244896',1720);
CREATE TABLE product (
	id INTEGER NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	date_posted DATETIME NOT NULL, 
	price INTEGER NOT NULL, 
	description TEXT NOT NULL, 
	image_file VARCHAR, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);
INSERT INTO product VALUES(1,'aqua allegoria perfume bottle','2020-06-10 14:29:59.720095',176,'Best sales of Fragrancecategory!','aqua allegoria perfume bottle 1961791.jpg',1);
INSERT INTO product VALUES(2,'chanel garrielle bottle covered with beaded necklace','2020-06-10 14:30:00.128009',606,'Best sales of Fragrancecategory!','chanel garrielle bottle covered with beaded necklace 1200502.jpg',1);
INSERT INTO product VALUES(3,'clear fragrance bottle','2020-06-10 14:30:00.419237',958,'Best sales of Fragrancecategory!','clear fragrance bottle 2090264.jpg',1);
INSERT INTO product VALUES(4,'jeanne lanvin my sin perfume bottle','2020-06-10 14:30:00.735731',844,'Best sales of Fragrancecategory!','jeanne lanvin my sin perfume bottle 1961794.jpg',1);
INSERT INTO product VALUES(5,'perfume bottle on a book','2020-06-10 14:30:01.651023',849,'Best sales of Fragrancecategory!','perfume bottle on a book 4110336.jpg',1);
INSERT INTO product VALUES(6,'photo of perfume','2020-06-10 14:30:02.448354',874,'Best sales of Fragrancecategory!','photo of perfume 3059609.jpg',1);
INSERT INTO product VALUES(7,'purple petaled flowers on a glass jar','2020-06-10 14:30:02.925227',105,'Best sales of Fragrancecategory!','purple petaled flowers on a glass jar 3272365.jpg',1);
INSERT INTO product VALUES(8,'white labeled perfume bottle','2020-06-10 14:30:03.972866',959,'Best sales of Fragrancecategory!','white labeled perfume bottle 2922276.jpg',1);
INSERT INTO product VALUES(9,'acoustic guitar adult boy cool','2020-06-10 14:30:04.760322',667,'Best sales of Mencategory!','acoustic guitar adult boy cool 325688.jpg',2);
INSERT INTO product VALUES(10,'black and white photo of man smoking','2020-06-10 14:30:05.086437',244,'Best sales of Mencategory!','black and white photo of man smoking 3594354.jpg',2);
INSERT INTO product VALUES(11,'close up photography of a man','2020-06-10 14:30:05.397303',995,'Best sales of Mencategory!','close up photography of a man 3031396.jpg',2);
INSERT INTO product VALUES(12,'grayscale photo of two men standing near hut','2020-06-10 14:30:05.754877',335,'Best sales of Mencategory!','grayscale photo of two men standing near hut 1359707.jpg',2);
INSERT INTO product VALUES(13,'laughing man wearing gray v neck t shirt','2020-06-10 14:30:14.541785',260,'Best sales of Mencategory!','laughing man wearing gray v neck t shirt 936119.jpg',2);
INSERT INTO product VALUES(14,'man about to touch his face wearing blue suit','2020-06-10 14:30:14.842979',410,'Best sales of Mencategory!','man about to touch his face wearing blue suit 718261.jpg',2);
INSERT INTO product VALUES(15,'man holding bamboo plant wearing sunglasses and fedora hat','2020-06-10 14:30:15.045437',481,'Best sales of Mencategory!','man holding bamboo plant wearing sunglasses and fedora hat 1656684.jpg',2);
INSERT INTO product VALUES(16,'man in black adidas full zip jacket','2020-06-10 14:30:15.389739',355,'Best sales of Mencategory!','man in black adidas full zip jacket 1192601.jpg',2);
INSERT INTO product VALUES(17,'man in black jacket','2020-06-10 14:30:15.622323',516,'Best sales of Mencategory!','man in black jacket 771742.jpg',2);
INSERT INTO product VALUES(18,'man in blue dress shirt and black formal suit','2020-06-10 14:30:15.886855',557,'Best sales of Mencategory!','man in blue dress shirt and black formal suit 1043473.jpg',2);
INSERT INTO product VALUES(19,'man in blue v neck t shirt','2020-06-10 14:30:16.125886',722,'Best sales of Mencategory!','man in blue v neck t shirt 1430879.jpg',2);
INSERT INTO product VALUES(20,'man in denim jacket yellow cap and sunglasses smiling','2020-06-10 14:30:16.499471',364,'Best sales of Mencategory!','man in denim jacket yellow cap and sunglasses smiling 2975401.jpg',2);
INSERT INTO product VALUES(21,'man in red jacket','2020-06-10 14:30:16.709543',553,'Best sales of Mencategory!','man in red jacket 1681010.jpg',2);
INSERT INTO product VALUES(22,'man in white v neck t shirt and black pants','2020-06-10 14:30:16.946510',843,'Best sales of Mencategory!','man in white v neck t shirt and black pants 775358.jpg',2);
INSERT INTO product VALUES(23,'man lying on brown dried grass','2020-06-10 14:30:17.169291',711,'Best sales of Mencategory!','man lying on brown dried grass 3772771.jpg',2);
INSERT INTO product VALUES(24,'man lying on plants','2020-06-10 14:30:17.384132',652,'Best sales of Mencategory!','man lying on plants 2915216.jpg',2);
INSERT INTO product VALUES(25,'man reading burning newspaper','2020-06-10 14:30:17.765987',741,'Best sales of Mencategory!','man reading burning newspaper 3278364.jpg',2);
INSERT INTO product VALUES(26,'man sitting on floor','2020-06-10 14:30:18.089691',628,'Best sales of Mencategory!','man sitting on floor 1205033.jpg',2);
INSERT INTO product VALUES(27,'man sitting on white car hood','2020-06-10 14:30:18.349541',216,'Best sales of Mencategory!','man sitting on white car hood 1211588.jpg',2);
INSERT INTO product VALUES(28,'man squatting while holding sunglasses','2020-06-10 14:30:19.004549',795,'Best sales of Mencategory!','man squatting while holding sunglasses 2897532.jpg',2);
INSERT INTO product VALUES(29,'man standing beside green leafed plants','2020-06-10 14:30:19.540827',411,'Best sales of Mencategory!','man standing beside green leafed plants 3067333.jpg',2);
INSERT INTO product VALUES(30,'man standing under a flowering tree','2020-06-10 14:30:19.899891',543,'Best sales of Mencategory!','man standing under a flowering tree 2814239.jpg',2);
INSERT INTO product VALUES(31,'man wearing black and white paisley dress shirt','2020-06-10 14:30:21.419345',109,'Best sales of Mencategory!','man wearing black and white paisley dress shirt 2897531.jpg',2);
INSERT INTO product VALUES(32,'man wearing black suit','2020-06-10 14:30:21.630288',355,'Best sales of Mencategory!','man wearing black suit 2955376.jpg',2);
INSERT INTO product VALUES(33,'man wearing blue dress shirt and black jeans','2020-06-10 14:30:21.940247',838,'Best sales of Mencategory!','man wearing blue dress shirt and black jeans 2905237.jpg',2);
INSERT INTO product VALUES(34,'man wearing blue lacoste polo shirt and silver colored','2020-06-10 14:30:22.243656',561,'Best sales of Mencategory!','man wearing blue lacoste polo shirt and silver colored 1232459.jpg',2);
INSERT INTO product VALUES(35,'man wearing gray and white full zip jacket','2020-06-10 14:30:22.580449',568,'Best sales of Mencategory!','man wearing gray and white full zip jacket 1081606.jpg',2);
INSERT INTO product VALUES(36,'man wearing multicolored costume','2020-06-10 14:30:22.786191',457,'Best sales of Mencategory!','man wearing multicolored costume 1038040.jpg',2);
INSERT INTO product VALUES(37,'man wearing red button up dress shirt','2020-06-10 14:30:23.140135',611,'Best sales of Mencategory!','man wearing red button up dress shirt 1726710.jpg',2);
INSERT INTO product VALUES(38,'man wearing the joker makeup','2020-06-10 14:30:23.556288',983,'Best sales of Mencategory!','man wearing the joker makeup 3078404.jpg',2);
INSERT INTO product VALUES(39,'man wearing yellow clothing','2020-06-10 14:30:23.914981',451,'Best sales of Mencategory!','man wearing yellow clothing 3632878.jpg',2);
INSERT INTO product VALUES(40,'man with braided hair in yellow outfit','2020-06-10 14:30:24.203447',216,'Best sales of Mencategory!','man with braided hair in yellow outfit 3341231.jpg',2);
INSERT INTO product VALUES(41,'photo of man holding camera','2020-06-10 14:30:24.497605',217,'Best sales of Mencategory!','photo of man holding camera 1484771.jpg',2);
INSERT INTO product VALUES(42,'photo of man wearing black shirt','2020-06-10 14:30:24.808706',181,'Best sales of Mencategory!','photo of man wearing black shirt 3290886.jpg',2);
INSERT INTO product VALUES(43,'photo of man wearing denim jacket','2020-06-10 14:30:25.068138',823,'Best sales of Mencategory!','photo of man wearing denim jacket 1599980.jpg',2);
INSERT INTO product VALUES(44,'photo of man wearing orange beanie','2020-06-10 14:30:25.282863',659,'Best sales of Mencategory!','photo of man wearing orange beanie 2801538.jpg',2);
INSERT INTO product VALUES(45,'photo of man wearing red tuxido','2020-06-10 14:30:25.531886',851,'Best sales of Mencategory!','photo of man wearing red tuxido 3022718.jpg',2);
INSERT INTO product VALUES(46,'photography of guy wearing yellow hoodie','2020-06-10 14:30:25.917273',533,'Best sales of Mencategory!','photography of guy wearing yellow hoodie 1183266.jpg',2);
INSERT INTO product VALUES(47,'photography of man wearing eyeglasses','2020-06-10 14:30:26.205218',423,'Best sales of Mencategory!','photography of man wearing eyeglasses 792326.jpg',2);
INSERT INTO product VALUES(48,'side view photography of man while closing his eyes','2020-06-10 14:30:26.406082',929,'Best sales of Mencategory!','side view photography of man while closing his eyes 761115.jpg',2);
INSERT INTO product VALUES(49,'smiling man looking at his phone leaning on concrete pillar','2020-06-10 14:30:26.651699',916,'Best sales of Mencategory!','smiling man looking at his phone leaning on concrete pillar 3206079.jpg',2);
INSERT INTO product VALUES(50,'time lapse photography of man doing skateboard trick','2020-06-10 14:30:27.001947',837,'Best sales of Mencategory!','time lapse photography of man doing skateboard trick 3133688.jpg',2);
INSERT INTO product VALUES(51,'grayscale photo of woman in formal suit sitting on folding','2020-06-10 14:30:27.487483',143,'Best sales of Womencategory!','grayscale photo of woman in formal suit sitting on folding 952214.jpg',3);
INSERT INTO product VALUES(52,'man and woman standing outside near bare tree','2020-06-10 14:30:27.739436',527,'Best sales of Womencategory!','man and woman standing outside near bare tree 2174661.jpg',3);
INSERT INTO product VALUES(53,'newly married couple hugging each other','2020-06-10 14:30:28.078359',752,'Best sales of Womencategory!','newly married couple hugging each other 3673460.jpg',3);
INSERT INTO product VALUES(54,'photo of woman wearing white dress','2020-06-10 14:30:28.341658',739,'Best sales of Womencategory!','photo of woman wearing white dress 748870.jpg',3);
INSERT INTO product VALUES(55,'serious female tailor cutting pieces of black fabric while','2020-06-10 14:30:28.569227',161,'Best sales of Womencategory!','serious female tailor cutting pieces of black fabric while 3959073.jpg',3);
INSERT INTO product VALUES(56,'smiling woman with natural grape as earring','2020-06-10 14:30:28.772922',205,'Best sales of Womencategory!','smiling woman with natural grape as earring 3746254.jpg',3);
INSERT INTO product VALUES(57,'stylish young woman in garden with blooming trees','2020-06-10 14:30:29.114039',391,'Best sales of Womencategory!','stylish young woman in garden with blooming trees 3954259.jpg',3);
INSERT INTO product VALUES(58,'two women standing beside each other wearing white top and','2020-06-10 14:30:29.320777',239,'Best sales of Womencategory!','two women standing beside each other wearing white top and 2711729.jpg',3);
INSERT INTO product VALUES(59,'woman about to kiss the man at the forest','2020-06-10 14:30:29.659388',544,'Best sales of Womencategory!','woman about to kiss the man at the forest 2249172.jpg',3);
INSERT INTO product VALUES(60,'woman holding coca cola glass bottle','2020-06-10 14:30:30.146925',136,'Best sales of Womencategory!','woman holding coca cola glass bottle 3286125.jpg',3);
INSERT INTO product VALUES(61,'woman hugging man in black sweatshirt','2020-06-10 14:30:30.520508',531,'Best sales of Womencategory!','woman hugging man in black sweatshirt 709794.jpg',3);
INSERT INTO product VALUES(62,'woman in black dress','2020-06-10 14:30:30.764124',164,'Best sales of Womencategory!','woman in black dress 3972493.jpg',3);
INSERT INTO product VALUES(63,'woman in black long sleeved shirt wearing black hat','2020-06-10 14:30:31.030366',831,'Best sales of Womencategory!','woman in black long sleeved shirt wearing black hat 4450356.jpg',3);
INSERT INTO product VALUES(64,'woman in black spaghetti strap top holding fire extinguisher','2020-06-10 14:30:31.466838',718,'Best sales of Womencategory!','woman in black spaghetti strap top holding fire extinguisher 1851994.jpg',3);
INSERT INTO product VALUES(65,'woman in blue sweater with black hijab outfit','2020-06-10 14:30:32.334112',728,'Best sales of Womencategory!','woman in blue sweater with black hijab outfit 925043.jpg',3);
INSERT INTO product VALUES(66,'woman in brown coat standing on bridge','2020-06-10 14:30:33.315099',991,'Best sales of Womencategory!','woman in brown coat standing on bridge 3615455.jpg',3);
INSERT INTO product VALUES(67,'woman in maroon buttoned coat wearing black hat','2020-06-10 14:30:33.748938',825,'Best sales of Womencategory!','woman in maroon buttoned coat wearing black hat 952629.jpg',3);
INSERT INTO product VALUES(68,'woman in white and black striped shirt','2020-06-10 14:30:34.051037',791,'Best sales of Womencategory!','woman in white and black striped shirt 1756170.jpg',3);
INSERT INTO product VALUES(69,'woman in yellow crew neck t shirt','2020-06-10 14:30:34.407248',884,'Best sales of Womencategory!','woman in yellow crew neck t shirt 3975955.jpg',3);
INSERT INTO product VALUES(70,'woman leaning against wall','2020-06-10 14:30:34.783785',664,'Best sales of Womencategory!','woman leaning against wall 2267139.jpg',3);
INSERT INTO product VALUES(71,'woman posing beside rock','2020-06-10 14:30:35.118135',280,'Best sales of Womencategory!','woman posing beside rock 2249718.jpg',3);
INSERT INTO product VALUES(72,'woman posing outdoors','2020-06-10 14:30:35.447031',956,'Best sales of Womencategory!','woman posing outdoors 2608344.jpg',3);
INSERT INTO product VALUES(73,'woman sitting on bungee chair','2020-06-10 14:30:36.162856',494,'Best sales of Womencategory!','woman sitting on bungee chair 993871.jpg',3);
INSERT INTO product VALUES(74,'woman sitting on sofa bed wearing sunglasses','2020-06-10 14:30:36.712744',136,'Best sales of Womencategory!','woman sitting on sofa bed wearing sunglasses 965324.jpg',3);
INSERT INTO product VALUES(75,'woman touching face with own hand','2020-06-10 14:30:37.241910',472,'Best sales of Womencategory!','woman touching face with own hand 1852015.jpg',3);
INSERT INTO product VALUES(76,'woman wearing blue long sleeved shirt and red skirt standing','2020-06-10 14:30:37.782924',210,'Best sales of Womencategory!','woman wearing blue long sleeved shirt and red skirt standing 955332.jpg',3);
INSERT INTO product VALUES(77,'woman wearing gray waist vest and gray flare pants','2020-06-10 14:30:38.445069',730,'Best sales of Womencategory!','woman wearing gray waist vest and gray flare pants 953271.jpg',3);
INSERT INTO product VALUES(78,'woman wearing maroon and white floral dress','2020-06-10 14:30:38.900099',892,'Best sales of Womencategory!','woman wearing maroon and white floral dress 1428788.jpg',3);
INSERT INTO product VALUES(79,'woman wearing red lace bra','2020-06-10 14:30:39.535476',526,'Best sales of Womencategory!','woman wearing red lace bra 1970261.jpg',3);
INSERT INTO product VALUES(80,'woman wearing sleeveless top and pants','2020-06-10 14:30:39.897486',489,'Best sales of Womencategory!','woman wearing sleeveless top and pants 1983917.jpg',3);
INSERT INTO product VALUES(81,'woman wearing strapless dress sitting on staircase','2020-06-10 14:30:40.391474',574,'Best sales of Womencategory!','woman wearing strapless dress sitting on staircase 859202.jpg',3);
INSERT INTO product VALUES(82,'woman wearing teal pink and purple button up shirt','2020-06-10 14:30:40.699708',189,'Best sales of Womencategory!','woman wearing teal pink and purple button up shirt 1839904.jpg',3);
INSERT INTO product VALUES(83,'women s black long sleeved shirt with white polka dots','2020-06-10 14:30:41.061367',570,'Best sales of Womencategory!','women s black long sleeved shirt with white polka dots 1021693.jpg',3);
INSERT INTO product VALUES(84,'women s white and black striped dress shirt','2020-06-10 14:30:41.507072',146,'Best sales of Womencategory!','women s white and black striped dress shirt 1844012.jpg',3);
INSERT INTO product VALUES(85,'women s white and brown floral dress','2020-06-10 14:30:41.874030',582,'Best sales of Womencategory!','women s white and brown floral dress 1805412.jpg',3);
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu
INSERT INTO products_product (id, name, description, price, category_id, brand_id, created_at, updated_at, image, is_featured, is_newarrival, slu

CREATE TABLE comment (
	id INTEGER NOT NULL, 
	date_posted DATETIME NOT NULL, 
	content TEXT NOT NULL, 
	content_chatbot TEXT NOT NULL, 
	user_id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);
INSERT INTO comment VALUES(1,'2020-06-10 14:43:11.275187','Chao','Chao',1,9);
INSERT INTO comment VALUES(2,'2020-06-10 14:43:32.645042','Bo nay con hang khong?','bao nhieu mau',1,9);
INSERT INTO comment VALUES(3,'2020-06-10 14:44:06.732118','Bo nay co bao nhieu mau?','Bo co 3 loai mau chinh: do, xanh, den',1,9);
INSERT INTO comment VALUES(4,'2020-06-10 14:47:05.945665','Chao','Chao ban, Minh ten la Li Li. Minh co the giup gi cho ban?',1,84);
INSERT INTO comment VALUES(5,'2020-06-10 15:10:21.181804','','Ao nay co bao nhieu size?',1,84);
INSERT INTO comment VALUES(6,'2020-06-10 15:11:47.835504','','Ao nay co bao nhieu size?',1,84);
INSERT INTO comment VALUES(7,'2020-06-10 16:12:49.121867','Chao','Chao ban, Minh ten la Li Li. Minh co the giup gi cho ban?',1,85);
INSERT INTO comment VALUES(8,'2020-06-15 09:59:23.760121','hello','Bo nay co bao nhieu mau?',1,84);
INSERT INTO comment VALUES(9,'2020-06-15 09:59:28.582785','','Ao nay co bao nhieu size?',1,84);
INSERT INTO comment VALUES(10,'2020-06-20 06:43:18.053361','hi','Ao co 3 size: S, M, L',1,10);
INSERT INTO comment VALUES(11,'2020-06-20 06:43:40.048905','Chao','Chao ban, Minh ten la Li Li. Minh co the giup gi cho ban?',1,10);
INSERT INTO comment VALUES(12,'2020-06-21 15:05:52.427886','Chao','Chao ban, Minh ten la Li Li. Minh co the giup gi cho ban?',1,83);
INSERT INTO comment VALUES(13,'2023-02-18 07:33:59.464112','gsgsg','gsgsg',2,9);
CREATE TABLE cart_item (
	id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	quantity INTEGER NOT NULL, 
	infor_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_id) REFERENCES product (id), 
	FOREIGN KEY(infor_id) REFERENCES infor (id)
);
INSERT INTO cart_item VALUES(1,83,3,1);
COMMIT;
