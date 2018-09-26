CREATE TABLE BREWERY
(
	brewery_id INT(30) NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	date_established DATE,
	phone_number VARCHAR(15),
	website VARCHAR(50),
	city VARCHAR(50),
	country VARCHAR(50),
	state VARCHAR(50),
	zipcode CHAR(12),
	region_id INT(9) NOT NULL,
  beer_count INT(9) DEFAULT 0,
	history_description LONGTEXT,
	PRIMARY KEY(brewery_id)
);

CREATE TABLE BEER_FOOD
(
	food_id INT(10) NOT NULL,
	beer_id INT(10) NOT NULL,
	PRIMARY KEY (food_id, beer_id)
);

CREATE TABLE FOOD_PAIRING
(
	food_id INT(10) NOT NULL AUTO_INCREMENT,
	food_type VARCHAR(50),
	PRIMARY KEY(food_id)
);

CREATE TABLE SALES_LOCATION
(
	sales_id int(50) NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	city VARCHAR(50),
	country VARCHAR(50),
	state VARCHAR(50),
	zipcode CHAR(12),
	PRIMARY KEY (sales_id)
);

CREATE TABLE BEER
(
	beer_id INT(10) NOT NULL AUTO_INCREMENT,
	beer_name VARCHAR(30) NOT NULL,
	alcohol_by_volume CHAR(3) NOT NULL,
	ibu_rank VARCHAR(30) NOT NULL,
	standard_reference_method VARCHAR(30) NOT NULL,
	style_id CHAR(9) NOT NULL,
	time_of_year_availability_id CHAR(30),
	price_range_code INT(9) NOT NULL,
	brewery_id INT(30) NOT NULL,
	PRIMARY KEY(beer_id)
);

CREATE TABLE PRICE_RANGE
(
	price_range_code INT(9) NOT NULL,
	price_range VARCHAR (9) NOT NULL,
	PRIMARY KEY (price_range_code)
);

CREATE TABLE BAR
(
	bar_id INT(9) NOT NULL AUTO_INCREMENT,
	bar_name VARCHAR(30) NOT NULL,
	city VARCHAR(30),
	state VARCHAR(30),
	country VARCHAR(30),
	zipcode CHAR(9),
	website_url VARCHAR(100),
	phone_number VARCHAR(15),
	PRIMARY KEY(bar_id)
);

CREATE TABLE BEER_STYLE
(
	style_id CHAR(9) NOT NULL,
	style_name VARCHAR(30) NOT NULL,
	PRIMARY KEY(style_id)
);

CREATE TABLE REGION
(
	region_id INT(9) NOT NULL,
	region_name VARCHAR(120) NOT NULL,
	region_states LONGTEXT,
	PRIMARY KEY(region_id)
);

CREATE TABLE SEASONAL_AVAILABILITY
(
	time_of_year_availability_id INT(9) NOT NULL,
	start_date_of_availability VARCHAR(15),
	end_date_of_availability VARCHAR(15),
	PRIMARY KEY(time_of_year_availability_id)
);

CREATE TABLE BEER_FOR_SEASON
(
	beer_id INT(10) NOT NULL,
	time_of_year_availability_id INT(9) NOT NULL,
	PRIMARY KEY(beer_id, time_of_year_availability_id)
);

CREATE TABLE PERSON
(
	username VARCHAR(22) NOT NULL,
	email VARCHAR(30) NOT NULL,
	name VARCHAR(30) NOT NULL,
	phone_number VARCHAR(15),
	PRIMARY KEY (username)
);

CREATE TABLE LIKES
(
	username VARCHAR(22) NOT NULL,
	beer_id INT(10) NOT NULL,
	PRIMARY KEY (username, beer_id)
);

CREATE TABLE users (
  id INT(30) NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL UNIQUE,
  pass VARCHAR(255) NOT NULL,
  email VARCHAR(50) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);


CREATE TABLE BEER_FOR_SALE
(
	sales_id INT(50) NOT NULL,
	beer_id INT(10) NOT NULL,
	PRIMARY KEY (sales_id, beer_id)
);

CREATE TABLE BEER_IN_BARS
(
	bar_id INT(9) NOT NULL,
	beer_id INT(10) NOT NULL,
	PRIMARY KEY (bar_id, beer_id)
);

ALTER TABLE BREWERY ADD CONSTRAINT FOREIGN KEY(region_id) REFERENCES REGION(region_id);

ALTER TABLE BEER_FOOD ADD CONSTRAINT FOREIGN KEY (food_id) REFERENCES FOOD_PAIRING(food_id);
ALTER TABLE BEER_FOOD ADD CONSTRAINT FOREIGN KEY (beer_id) REFERENCES BEER(beer_id);

ALTER TABLE BEER_FOR_SALE ADD CONSTRAINT FOREIGN KEY (beer_id) REFERENCES BEER(beer_id);
ALTER TABLE BEER_FOR_SALE ADD CONSTRAINT FOREIGN KEY (sales_id) REFERENCES SALES_LOCATION(sales_id);

ALTER TABLE BEER_IN_BARS ADD CONSTRAINT FOREIGN KEY (bar_id) REFERENCES BAR(bar_id);
ALTER TABLE BEER_IN_BARS ADD CONSTRAINT FOREIGN KEY (beer_id) REFERENCES BEER(beer_id);

ALTER TABLE BEER ADD CONSTRAINT FOREIGN KEY (style_id) REFERENCES BEER_STYLE(style_id);
ALTER TABLE BEER ADD CONSTRAINT FOREIGN KEY (brewery_id) REFERENCES BREWERY(brewery_id);
ALTER TABLE BEER ADD CONSTRAINT FOREIGN KEY (price_range_code) REFERENCES PRICE_RANGE(price_range_code);

ALTER TABLE BEER_FOR_SEASON ADD CONSTRAINT FOREIGN KEY (beer_id) REFERENCES BEER(beer_id);
ALTER TABLE BEER_FOR_SEASON ADD CONSTRAINT FOREIGN KEY (time_of_year_availability_id) REFERENCES SEASONAL_AVAILABILITY(time_of_year_availability_id);

ALTER TABLE LIKES ADD CONSTRAINT FOREIGN KEY (beer_id) REFERENCES BEER(beer_id);
ALTER TABLE LIKES ADD CONSTRAINT FOREIGN KEY (username) REFERENCES PERSON(username);


DROP TRIGGER IF EXISTS BreweryBeerCountIncrement;
delimiter //
CREATE TRIGGER BreweryBeerCountIncrement AFTER INSERT ON Beer
  FOR EACH ROW
  BEGIN
    UPDATE brewery
    SET beer_count = beer_count + 1
    WHERE brewery_id = new.brewery_id;
  END;
//
delimiter ;

DROP TRIGGER IF EXISTS BreweryBeerCountDecrement;
delimiter //
CREATE TRIGGER BreweryBeerCountDecrement BEFORE DELETE ON Beer
  FOR EACH ROW
  BEGIN
    UPDATE brewery
    SET beer_count = beer_count - 1
    WHERE brewery_id = old.brewery_id;
  END;
//
delimiter ;

DROP PROCEDURE IF EXISTS ChangePrice;
delimiter //
CREATE PROCEDURE ChangePrice (IN BeerIN INT(10),IN NewRange INT(9) )
BEGIN
  UPDATE BEER set price_range_code = NewRange WHERE beer_id = BeerIN;
END;
//
delimiter ;

DROP VIEW IF EXISTS Best;
CREATE VIEW Best AS(
SELECT BREWERY.brewery_id, BEER.beer_id
FROM BREWERY
JOIN BEER ON BREWERY.brewery_id = BEER.beer_id);

-- SELECT * FROM Best;
