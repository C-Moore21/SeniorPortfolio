/*
--Insert commands
--sales_id    format  sl1...  char
--brewery_id  format  01...   int
--food_id     format  1...    int
--beer_id     format  1...    int
--bar_id      format  01...     int
--style_id    format  bs1...  char
--region_id   format  1...    int
--username    format  UNKNONW   VARCHAR
--price_range_code  format  1...  int
--time_of_year_availability_id  format  1...  int
*/

/*
--
-- Dumping data for table 'REGION'
--
*/


INSERT INTO REGION(region_id, region_name, region_states) VALUES (1, 'New England', 'Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont');

INSERT INTO REGION(region_id, region_name, region_states) VALUES (2, 'Mid-Atlantic', 'New Jersey, New York, Pennsylvania');

INSERT INTO REGION(region_id, region_name, region_states) VALUES (3, 'East North Central', 'Illinois, Indiana, Michigan, Ohio, Wisconsin');

INSERT INTO REGION(region_id, region_name, region_states) VALUES (4, 'West North Central', 'Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota');

INSERT INTO REGION(region_id, region_name, region_states) VALUES (5, 'South Atlantic', 'Delaware, Florida, Georgia, Maryland, North Carolina, South Carolina, Virginia, District of Columbia, West Virginia');

INSERT INTO REGION(region_id, region_name, region_states) VALUES (6, 'East South Central', 'Alabama, Kentucky, Mississippi, Tennessee');

INSERT INTO REGION(region_id, region_name, region_states) VALUES (7, 'West South Central', 'Arkansas, Louisiana, Oklahoma, Texas');

INSERT INTO REGION(region_id, region_name, region_states) VALUES (8, 'Mountain', 'Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, Wyoming');

INSERT INTO REGION(region_id, region_name, region_states) VALUES (9, 'Pacific', 'Alaska, California, Hawaii, Oregon, and Washington');



/*
--
-- Dumping data for table 'BREWERY'
--
*/

INSERT INTO BREWERY (brewery_id, name, date_established, phone_number, website, city, country, state, zipcode, region_id, history_description) VALUES
(1, 'Wasatch Brewery', '1986-01-01', '801-783-1127', 'www.wasatchbeers.com', 'Salt Lake City', 'United States', 'Utah', 84111, 8, 'This Brewery was founded in 1986 to satisfy the most discerning beer enthusiasts. "Where''s the beer? Where are the breweries?" Those were among the first thoughts Greg Schirf had after moving to Utah from Milwaukee in the early 80s. Incredibly, drinking and brewing were all but forbidden. Greg took matters into his own hands and did what any self respecting midwesterner would do: He started a brewery. Wasatch was the very first brewery in Utah, and one of the first craft brewers in all of the U.S., brewing award winning brews since 1986.');

INSERT INTO BREWERY (brewery_id, name, date_established, phone_number, website, city, country, state, zipcode, region_id, history_description) VALUES
(2, 'Epic Brewery', '2008-01-01', '801-906-0123', 'www.epicbrewing.com', 'Salt Lake City', 'United States', 'Utah', 84111, 8, 'David Cole and Peter Erickson are the founders and co-owners of Epic Brewing Company. Cole and Erickson, originally from California, started an international aquaculture company in Utah in 1992. In 28, Utah law changed allowing these two entrepreneurs to pursue their longtime dream of opening a strong beer microbrewery in Utah, like those they frequented in the Golden State.');

INSERT INTO BREWERY (brewery_id, name, date_established, phone_number, website, city, country, state, zipcode, region_id, history_description) VALUES
(3, 'Left Hand Brewing', '1980-02-23', '303-772-0258', 'www.lefthandbrewing.com', 'Longmont', 'United States', 'Colorado', 80501, 8, 'Living here in our great state requires great balance theres just simply too much to do! Soak in over 3 days of sunshine a year. Catch a show at Red Rocks. Climb to the top of 14,255ft Longs Peak. Catch an Avs or Rockies game. Drop into some fresh powder at A-Basin. Tee up on the first hole at Haystack Mountain.');

INSERT INTO BREWERY (brewery_id, name, date_established, phone_number, website, city, country, state, zipcode, region_id, history_description) VALUES
(4, 'Bridger Brewing', '2013-03-02', '406-587-2124', 'www.bridgerbrewing.com', 'Bozeman', 'United States', 'Montana', 59715, 8, "Choosing the Bridger Brewing name for our dream was easy. From the mountain man Jim Bridger himself; to the beautiful mountains that surround our community, the name is legendary; inspiring happenings that are outside the realm of possibility for most, but not for us. We climb the iciest peaks, swim the swiftest rivers, con the most elusive trout, still hunt, gather or grow many of our meals, laugh easy, cry some and perhaps most of all, relish and appreciate this miraculous spot on the globe we call home.");

INSERT INTO BREWERY (brewery_id, name, date_established, phone_number, website, city, country, state, zipcode, region_id, history_description) VALUES
(5, 'Big Beaver Brewing', '2010-01-01', '970-818-6064', 'www.bigbeaverbrew.com', 'Loveland','United States', 'Colorado', 80537, 8, "Since 2010, the Big Beaver Brewing Company has been creating delicious craft beer in the shadows of the Rocky Mountain National Park. This awe-inspiring view demands equally awesome beer, and the Big Beaver Brewery provides just that with 16 beers on tap to choose from. Enjoy your favorite beer in the cozy confines of our Taproom or to-go in refillable growlers. Stop by today and see for yourself why everybody is saying…");

INSERT INTO BREWERY (brewery_id, name, date_established, phone_number, website, city, country, state, zipcode, region_id, history_description) VALUES
(6, 'Spencer Brewery', '1957-01-01', '508-885-5756', 'www.spencerbrewery.com', 'Spencer','United States', 'Massachusetts', 01562, 8, "Trappist communities observe the counsel of the Rule of St. Benedict, a 6th century guide for monastic life, that stresses the importance of ora et labora or pray and work. Monks are encouraged to be self-supportive and offer charitable assistance to others by producing and selling goods to the public.");

INSERT INTO BREWERY (brewery_id, name, date_established, phone_number, website, city, country, state, zipcode, region_id, history_description) VALUES
(7, 'Lagunitas Brewing Company', '2013-03-02', '406-587-2124', 'www.lagunitas.com', 'Petaluma','United States', 'California', 94954,  9, "Choosing the Bridger Brewing name for our dream was easy. From the mountain man Jim Bridger himself; to the beautiful mountains that surround our community, the name is legendary; inspiring happenings that are outside the realm of possibility for most, but not for us. We climb the iciest peaks, swim the swiftest rivers, con the most elusive trout, still hunt, gather or grow many of our meals, laugh easy, cry some and perhaps most of all, relish and appreciate this miraculous spot on the globe we call home.");

/*
--
-- Dumping data for table 'BEER_STYLE'
--
*/

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (1, 'Pale Ale');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (2, 'Amber Lager');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (3, 'Porter');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (4, 'Stout');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (5, 'Bock');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (6, 'Brown Ale');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (7, 'Bitter');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (8, 'Barley Wine');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (9, 'American Pale Ale');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (10, 'Wheat Beer');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (11, 'Dunkel');

INSERT INTO BEER_STYLE(style_id, style_name) VALUES (12, 'Pilsner');


/*
--
-- Dumping data for table 'PRICE_RANGE'
--
*/

INSERT INTO PRICE_RANGE(price_range_code, price_range) VALUES (1, '1-3USD');
INSERT INTO PRICE_RANGE(price_range_code, price_range) VALUES (2, '3-6USD');
INSERT INTO PRICE_RANGE(price_range_code, price_range) VALUES (3, '6-9USD');
INSERT INTO PRICE_RANGE(price_range_code, price_range) VALUES (4, '10++USD');

/*
--
-- Dumping data for table 'BEER'
--
*/

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(1, 'Spiral Jetty IPA', 6.6, '60', '69', 1, 1, 1, 2);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(2, 'Devastator', 8.0, '60', '69', 2, 2, 2, 1);

INSERT INTO BEER (beer_ID, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(3, 'Milk Stout', 8.0, '60', '69', 2, 2, 3, 3);

INSERT INTO BEER (beer_ID, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(4, 'Polygamy Porter', 8.8, '60', '69', 2, 2, 2, 1);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(5, 'Polestar Pilsner', 6.8, '40', '49', 12, 2, 2, 4);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(6, 'Lee Metcalf Pale Ale', 5.4, '50', '59', 9, 2, 2, 5);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(7, 'Ghost Town Coffee Stout', 4.8, '50', '59', 4, 2, 2, 5);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(8, 'Fisher Beer', 4.5, '40', '49', 12, 2, 2, 3);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(9, 'Fisher Brexit Brown', 6.5, '50', '59', 6, 2, 2, 3);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(10, 'Big Woody IPA', 7.7, '60', '69', 1, 2, 2, 6);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(11, 'Pecker Pilsner', 4.7, '40', '49', 12, 2, 2, 6);

INSERT INTO BEER (beer_id, beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES
(12, 'Vigilante IPA', 7.4, '60', '69', 1, 2, 2, 5);

/*
--
-- Dumping data for table 'PERSON'
--
*/

INSERT INTO PERSON (username, email, name, phone_number) VALUES
('thomasE', 'mannsverk21@gmail.com', 'Thomas Eliassen', '801111111');

INSERT INTO PERSON (username, email, name, phone_number) VALUES
('bridgerf', 'bef0926@westminstercollege.edu', 'Bridger Fisher', '8012222222');
/*
--
-- Dumping data for table 'SEASONAL_AVAILABILITY'
--
*/

INSERT INTO SEASONAL_AVAILABILITY(time_of_year_availability_id, start_date_of_availability, end_date_of_availability) VALUES (1, 'March', 'June');

INSERT INTO SEASONAL_AVAILABILITY(time_of_year_availability_id, start_date_of_availability, end_date_of_availability) VALUES (2, 'June', 'December');


/*
--
-- Dumping data for table 'BAR'
--
*/

INSERT INTO BAR(bar_id, bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (1, 'Ex Wives Place', 'Salt Lake City', 'Utah', 'United States', 84105, 'https://m.facebook.com/X-Wifes-Place-67250768716/', '18015321954');

INSERT INTO BAR(bar_id, bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (2, 'Liquid Joes', 'Salt Lake City', 'Utah', 'United States', 84106, 'http://liquidjoes.net/', '(801) 467-5637');

INSERT INTO BAR(bar_id, bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (3, 'Busy Bee', 'Salt Lake City', 'Utah', 'United States', 84105, 'No Website Available', '(801) 935-4014');

INSERT INTO BAR(bar_id, bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (4, 'Sugarhouse Pub', 'Salt Lake City', 'Utah', 'United States', 84105, 'https://www.facebook.com/sugarhousepub/?rf=153914834679862', '(801) 413-2857');

INSERT INTO BAR(bar_id, bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (5, 'Wasatch Brew Pub', 'Salt Lake City', 'Utah', 'United States', 84105, 'wasatchbeers.com', '(801) 783-1127');

INSERT INTO BAR(bar_id, bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (6, 'Cheers to You', 'Salt Lake City', 'Utah', 'United States', 84105, 'No Website Available', '(801) 575-64');

INSERT INTO BAR(bar_id, bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (7, 'Porqupine Pub', 'Salt Lake City', 'Utah', 'United States', 84105, 'Porqupinepub.com', '(801) 582-5555');

INSERT INTO BAR(bar_id, bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (8, 'Town Club', 'Salt Lake City', 'Utah', 'United States', 84105, 'Townclub.com', '(801) 322-1371');

/*
--
-- Dumping data for table 'FOOD_PAIRING'
--
*/

INSERT INTO FOOD_PAIRING(food_id, food_type) VALUES (1, 'Meat');

INSERT INTO FOOD_PAIRING(food_id, food_type) VALUES (2, 'Dessert');

INSERT INTO FOOD_PAIRING(food_id, food_type) VALUES (3, 'Strong');

INSERT INTO FOOD_PAIRING(food_id, food_type) VALUES (4, 'Salty');

/*
--
-- Dumping data for table 'BEER_FOOD'
--
*/

INSERT INTO BEER_FOOD(food_id, beer_id) VALUES (1, 1);

INSERT INTO BEER_FOOD(food_id, beer_id) VALUES (2, 2);

INSERT INTO BEER_FOOD(food_id, beer_id) VALUES (3, 12);

INSERT INTO BEER_FOOD(food_id, beer_id) VALUES (4, 6);

INSERT INTO BEER_FOOD(food_id, beer_id) VALUES (4, 1);


/*
--
-- Dumping data for table 'BEER_IN_BARS'
--
*/

INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (1, 1);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (2, 2);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (1, 3);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (1, 4);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (2, 4);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (2, 3);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (3, 1);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (3, 2);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (3, 3);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (3, 4);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 1);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 2);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 3);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 4);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 1);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 2);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 3);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 4);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 1);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 2);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 3);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 4);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 1);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 2);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 3);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 4);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 1);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 2);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 3);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 4);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 5);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 6);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 7);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 8);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 5);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 6);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 7);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 8);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 5);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 6);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 7);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 8);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 5);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 6);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 7);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 8);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 5);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 6);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 7);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 8);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 9);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 10);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 11);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (4, 12);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 9);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 10);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 11);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (5, 12);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 9);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 10);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 11);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (6, 12);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 9);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 10);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 11);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (7, 12);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 9);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 10);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 11);
INSERT INTO BEER_IN_BARS(bar_id, beer_id) VALUES (8, 12);

/*
--
-- Dumping data for table 'SALES_LOCATION'
--
*/

INSERT INTO SALES_LOCATION(sales_id, name, city, country, state, zipcode) VALUES (1, 'Smiths', 'Salt Lake City', 'United States', 'Utah', 84111);

INSERT INTO SALES_LOCATION(sales_id, name, city, country, state, zipcode) VALUES (2, 'State Liquor Store', 'Salt Lake City', 'United States', 'Utah', 84111);

/*
--
-- Dumping data for table 'BEER_FOR_SALE'
--
*/

INSERT INTO BEER_FOR_SALE(sales_id, beer_id) VALUES (1, 1);

INSERT INTO BEER_FOR_SALE(sales_id, beer_id) VALUES (2, 2);

/*
--
-- Dumping data for table 'BEER_FOR_SEASON'
--
*/

INSERT INTO BEER_FOR_SEASON(beer_id, time_of_year_availability_id) VALUES (1, 1);

INSERT INTO BEER_FOR_SEASON(beer_id, time_of_year_availability_id) VALUES (2, 2);
/*
--
-- Dumping data for table 'LIKES'
--
*/

INSERT INTO LIKES(username, beer_id) VALUES ('thomasE', 1);


INSERT INTO users(id, username, pass, email) VALUES (1, 'tme0221', 'tmepass', 'tme0221@westminstercollege.edu');
INSERT INTO users(id, username, pass, email) VALUES (2, 'cbm0908', 'cbmpass', 'cbm0908@westminstercollege.edu');
INSERT INTO users(id, username, pass, email) VALUES (3, 'bef0926', 'befpass', 'bef0926@westminstercollege.edu');
INSERT INTO users(id, username, pass, email) VALUES (4, 'lag0917', 'lagpass', 'lag0917@westminstercollege.edu');
