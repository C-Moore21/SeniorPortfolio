<?php
/* Database credential,
 ssuming standard MySQL with default settings
 (user'root' with no password)
*/

define ('DB_SERVER', 'localhost')
define ('DB_USERNAME', 'hop_owner')
define ('DB_PASSWORD', '')
define ('DB_NAME', 'hop_to_it')

/*Attempt  to connect to MySQL database */
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

// check connection
if($link === false){
  die("ERROR: Could not connect. " . mysqli_connect_error());
}

?>
