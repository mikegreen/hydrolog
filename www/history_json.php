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
$sth = mysql_query("select reading_date, reading_ts, air_temp_value, humidity_value, water_temp_value " 
	."from vw_dht22_readings "
	."where reading_date > (current_date - 3)  "
	."order by reading_ts ");

$rows = array();
//flag is not needed
$flag = true;
$table = array();
$table['cols'] = array(

    // Labels for your chart, these represent the column titles
	array('label' => 'reading_date', 'type' => 'date'), 
	array('label' => 'reading_ts', 'type' => 'date'),
	array('label' => 'air_temp_value', 'type' => 'number'),
	array('label' => 'humidity_value', 'type' => 'number'),
	array('label' => 'water_temp_value', 'type' => 'number')

);

$rows = array();
while($r = mysql_fetch_assoc($sth)) {

    $year = date("Y", strtotime($r['reading_ts'])); 
    $month = date("n", strtotime($r['reading_ts'])) - 1; 
    $day = date("j", strtotime($r['reading_ts'])); 
    $hour = date("H", strtotime($r['reading_ts']));
    $minute = date("i", strtotime($r['reading_ts']));

    $temp = array();

    // the following line will be used to slice the Pie chart
//    $temp[] = array('v' => (string) $r['reading_date']); 
    $temp[] = array('v' => "Date($year, $month, $day)"); 
    $temp[] = array('v' => "Date($year, $month, $day, $hour, $minute, 0, 0)"); 

    // Values of each slice
    $temp[] = array('v' => (float) $r['air_temp_value']); 
    $temp[] = array('v' => (float) $r['humidity_value']); 
    $temp[] = array('v' => (float) $r['water_temp_value']);     
    $rows[] = array('c' => $temp);
}

$table['rows'] = $rows;
$jsonTable = json_encode($table);
echo $jsonTable;
?>

