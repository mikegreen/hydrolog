<?php 

// set up header; first two prevent IE from caching queries
header('Cache-Control: no-cache, must-revalidate');
header('Expires: Mon, 26 Jul 1997 05:00:00 GMT');
header('Content-type: application/json');

include ( "../hl_config/config.php");

$con=mysql_connect("$dbhost","$dbuser","$dbpasswd") or die ("cannot connect...");
mysql_select_db("$dbname",$con) or die ("cannot select DB...");

$sth = mysql_query("select * from vw_water_level");

$values = array();

while($v = mysql_fetch_assoc($sth)) {
	$values[] = $v;
}

$jsonTable = json_encode($values);
echo $jsonTable;

?>

