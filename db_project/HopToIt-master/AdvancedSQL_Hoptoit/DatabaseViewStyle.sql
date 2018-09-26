USE HOP_TO_IT;
CREATE TABLE Store;

CREATE VIEW Best AS(
SELECT Beer_style.Style_name, BEER.BEER_name
FROM BEER, region
JOIN BEER ON Beer_style.style_id = BEER.STYLE_id);

SELECT * FROM Best;
