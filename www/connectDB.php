<?php
// include forum config file for DB info
include ( "../hl_config/config.php");

$databaseConnection=mysql_connect("$dbhost","$dbuser","$dbpasswd") or die ("cannot connect...");
mysql_select_db("$dbname") or die ("cannot select DB...");

?>