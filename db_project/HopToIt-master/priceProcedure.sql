--to call CALL ChangePrice([Beer_id you want to change], [the new price_range_code])

DROP PROCEDURE IF EXISTS ChangePrice;
delimiter //
CREATE PROCEDURE ChangePrice (IN BeerIN INT(10),IN NewRange INT(9) )
BEGIN
  UPDATE BEER set price_range_code = NewRange WHERE beer_id = BeerIN;
END;
//
delimiter ;
