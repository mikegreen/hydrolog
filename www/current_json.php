<?php 

// set up header; first two prevent IE from caching queries
header('Cache-Control: no-cache, must-revalidate');
header('Expires: Mon, 26 Jul 1997 05:00:00 GMT');
header('Content-type: application/json');

include ( "../hl_config/config.php");

$con=mysql_connect("$dbhost","$dbuser","$dbpasswd") or die ("cannot connect...");
mysql_select_db("$dbname",$con) or die ("cannot select DB...");

// The Chart table contains two fields: weekly_task and percentage
// This example will display a pie chart. If you need other charts such as a Bar chart, you will need to modify the code a little to make it work with bar chart and other charts
$sth = mysql_query("select * from vw_current_values");

$rows = array();
//flag is not needed
$flag = true;
$table = array();
$table['cols'] = array(

    // Labels for your chart, these represent the column titles
	array('label' => 'sensor_type', 'type' => 'string'), 
	array('label' => 'sensor_value', 'type' => 'number'),
	//array('label' => 'reading_ts', 'type' => 'string')

);

$rows = array();
while($r = mysql_fetch_assoc($sth)) {
  
    $temp = array();

    // the following line will be used to slice the Pie chart
//    $temp[] = array('v' => (string) $r['reading_date']); 
	$temp[] = array('v' => (string) $r['sensor_type']);  
	$temp[] = array('v' => (float) $r['sensor_value']); 
	//$temp[] = array('v' => (string) $r['reading_ts']); 
	$rows[] = array('c' => $temp);
}

$table['rows'] = $rows;
$jsonTable = json_encode($table);
echo $jsonTable;
?>

