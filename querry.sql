DROP TABLE IF EXISTS public.cerave_cream;
DROP TABLE IF EXISTS public.cerave_lotion;
DROP TABLE IF EXISTS public.eucerin_adv_cream;
DROP TABLE IF EXISTS public.eucerin_eczema_cream;
DROP TABLE IF EXISTS public.eucerin_intensive_lotion;

CREATE TABLE "cerave_cream"
(
	id SERIAL NOT NULL,
 	profile_name text,
 	stars varchar(20),
	title text,
 	review_date varchar(100),
 	review text,
	helpful varchar(50),
 	form varchar(10),
 	brand varchar(20),
 	sku text,
 	url text 
	);

CREATE TABLE "cerave_lotion"
(
	id SERIAL NOT NULL,
 	profile_name text,
 	stars varchar(20),
	title text,
 	review_date varchar(100),
 	review text,
	helpful varchar(50),
 	form varchar(10),
 	brand varchar(20),
 	sku text,
 	url text 
	);

CREATE TABLE "eucerin_adv_cream"
(
	id SERIAL NOT NULL,
 	profile_name text,
 	stars varchar(20),
	title text,
 	review_date varchar(100),
 	review text,
	helpful varchar(50),
 	form varchar(10),
 	brand varchar(20),
 	sku text,
 	url text 
	);


CREATE TABLE "eucerin_eczema_cream"
(
	id SERIAL NOT NULL,
 	profile_name text,
 	stars varchar(20),
	title text,
 	review_date varchar(100),
 	review text,
	helpful varchar(50),
 	form varchar(10),
 	brand varchar(20),
 	sku text,
 	url text 
	);
	
CREATE TABLE "eucerin_intensive_lotion"
(
	id SERIAL NOT NULL,
 	profile_name text,
 	stars varchar(20),
	title text,
 	review_date varchar(100),
 	review text,
	helpful varchar(50),
 	form varchar(10),
 	brand varchar(20),
 	sku text,
 	url text 
	);
	
	
SELECT stars,review
	FROM cerave_cream
	WHERE review LIKE '%moisture%' OR review LIKE '%love%' AND
	--WHERE NOT review LIKE '%hate%'
	

SELECT *
	FROM cerave_cream
	WHERE stars LIKE '5%'
UNION ALL
SELECT *
	FROM eucerin_intensive_lotion
	WHERE stars LIKE '5%'
UNION ALL
SELECT *
	FROM eucerin_eczema_cream
	WHERE stars LIKE '5%'
-- \copy cerave_cream(profile_name, stars, title, review_date, review, helpful, form, brand, sku, url) FROM '/Users/matthewrichtmyer/Documents/Data Science Bootcamp/Project 2/CPG-Analysis/data/csv/CeraVe_cream.csv' DELIMITER ',' CSV HEADER;
-- \copy cerave_lotion(profile_name, stars, title, review_date, review, helpful, form, brand, sku, url) FROM '/Users/matthewrichtmyer/Documents/Data Science Bootcamp/Project 2/CPG-Analysis/data/csv/CeraVe_lotion.csv' DELIMITER ',' CSV HEADER;
-- \copy eucerin_adv_cream(profile_name, stars, title, review_date, review, helpful, form, brand, sku, url) FROM '/Users/matthewrichtmyer/Documents/Data Science Bootcamp/Project 2/CPG-Analysis/data/csv/Eucerin_advanced_cream.csv' DELIMITER ',' CSV HEADER;
-- \copy eucerin_eczema_cream(profile_name, stars, title, review_date, review, helpful, form, brand, sku, url) FROM '/Users/matthewrichtmyer/Documents/Data Science Bootcamp/Project 2/CPG-Analysis/data/csv/Eucerin_eczema_cream.csv' DELIMITER ',' CSV HEADER;
-- \copy eucerin_intensive_lotion(profile_name, stars, title, review_date, review, helpful, form, brand, sku, url) FROM '/Users/matthewrichtmyer/Documents/Data Science Bootcamp/Project 2/CPG-Analysis/data/csv/Eucerin_intensive_lotion.csv' DELIMITER ',' CSV HEADER;


