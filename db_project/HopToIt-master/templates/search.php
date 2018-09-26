<?php
  mysql_connect("localhost","root","") or die("Could not connect");
  mysql_select_db("hop_to_it") or die("Could not fond database");

  //collect
  if(isset($_POST['search'])) {
    $searchq = $_POST['search'];

    $query = mysql_query("SELECT * FROM hop_to_it WHERE ") or die("could not search");
  }

 ?>
 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
 <html xmlns="http://www.w3.org/1999/xhtml">
 <head>
     <title>Search results</title>
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
     <link rel="stylesheet" type="text/css" href="style.css"/>
 </head>
 <body>
<?php
  //gets a value from search form
  $query = $_GET['query'];

  //minimal lenght for the searhc, optional
  $min_length = 3;

  if(strlen($query) >= $min_length){

    //change from html
    $query = htmlspecialchars($query);

    //no sql incetion
    $query = mysql_real_escape_string($query);

    $question = "(SELECT beer_name, ibu_rank, standard_reference_method, alcohol_by_volume, 'beer' as type FROM beer WHERE
    beer_name LIKE '%" . $keyword . "%' OR ibu_rank LIKE '%" . $keyword . "%' OR standard_reference_method LIKE '%" . $keyword . "%'
    OR alcohol_by_volume LIKE '%" . $keyword . "%' )
    UNION
    (SELECT name, date_established, website, city, country, state, 'brewery' as type FROM brewery WHERE
    name LIKE '%" . $keyword . "%' OR website LIKE '%" . $keyword . "%' OR city LIKE '%" . $keyword . "%'
    OR country LIKE '%" . $keyword . "%' OR state LIKE '%" . $keyword . "%')
    UNION
    (SELECT bar_name, website_url, city, country, state, 'bar' as type FROM bar WHERE
    bar_name LIKE '%" . $keyword . "%' OR website_url LIKE '%" . $keyword . "%' OR city LIKE '%" . $keyword . "%'
    OR country LIKE '%" . $keyword . "%' OR state LIKE '%" . $keyword . "%')";

//    $raw_results = mysql_query("SELECT * FROM beer
//      WHERE ('beer_name' LIKE '%".$query."%')
//      OR ('ibu_rank' LIKE '%".$query."%')
//      OR ('standard_reference_method' LIKE '%".$query."%')
//      OR ('style_id' LIKE '%".$query."%')") or die(mysql_error());

    $raw_results = mysql_query($question) or die(mysql_error());

    if(mysql_num_rows($raw_results) > 0){
      while($results = mysql_fetch_array($raw_results)){
        echo "<p><h3>".$results['beer_name']."</h3>".$results['ibu_rank'].$results['standard_reference_method'].$results['style_id']"</p>";
      }
    }
    else{
      echo "No results";
    }
  }
  else {
    echo "Minimum length is ".$min_length;
  }

  ?>
</body>
</html>
