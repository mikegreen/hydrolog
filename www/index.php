<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>
      hydrolog example
    </title>
    <script type="text/javascript" src="//www.google.com/jsapi"></script>
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script type="text/javascript">
      google.load('visualization', '1.1', {packages: ['corechart', 'controls']});
      google.load('visualization', '1.1', {packages: ['corechart', 'gauge']});
    </script>
    <script type="text/javascript">
   
	var d = new Date();
	var currentDay = d.getDate();
	var currentMonth = d.getMonth();
	var currentYear = d.getFullYear();
	
	var dPrior = new Date(d.getTime() - 1*24*60*60*1000);
	var priorDay = dPrior.getDate();
	var priorMonth = dPrior.getMonth();
	var priorYear = dPrior.getFullYear();
   
      function drawVisualization() {
      
      
	var gaugeOptions = {
		// width: 350,
		height: 150
		}
      
	function refreshData() {
		var currentjsonData = $.ajax({
		  url: "current_json.php",
		  dataType:"json",
		  async: false
		  }).responseText;		
	
		var currentData = new google.visualization.DataTable(currentjsonData);
		
		gauges.draw(currentData, gaugeOptions);	
		}	
      
	var jsonData = $.ajax({
          url: "history_hourly_json.php",
          dataType:"text",
          async: false
          }).responseText;
	  
	var gauges = new google.visualization.Gauge(document.getElementById('gauge_div'));

	var dashboard = new google.visualization.Dashboard(
             document.getElementById('dashboard'));
      
         var control = new google.visualization.ControlWrapper({
           'controlType': 'ChartRangeFilter',
           'containerId': 'control',
           'options': {
             // Filter by the date axis.
             'filterColumnIndex': 0,
	     'vAxis': {'viewWindow': {'min': 10, 'max': 30}},
             'ui': {
               'chartType': 'LineChart',
               'chartOptions': {
                 'chartArea': {'width': '80%'},
                 'hAxis': {'baselineColor': 'none'}
               },
               // Display a single series that shows the closing value of the stock.
               // Thus, this view has two columns: the date (axis) and the stock value (line series).
               'chartView': {
                 'columns': [0, 2,3]
               },
               // 1 day in milliseconds = 24 * 60 * 60 * 1000 = 86,400,000
               'minRangeSize': 86400000
             }
           },
           // Initial range
           'state': {'range': {'start': new Date(priorYear, priorMonth, priorDay), 'end': new Date(currentYear, currentMonth, currentDay+1)}}
         });
      
         var chart = new google.visualization.ChartWrapper({
           'chartType': 'LineChart',
           'containerId': 'chart',
	curveType: 'function',
           'options': {
             // Use the same chart area width as the control for axis alignment.
             'chartArea': {'height': '80%', 'width': '80%'},
             'hAxis': {'slantedText': false},
             'vAxis': {'viewWindow': {'min': 25, 'max': 80}},
	     colors:['red','#1c91c0','blue'] 
           },
           // Convert the first column from 'date' to 'string'.
           'view': {
             'columns': [
               {
                 'calc': function(dataTable, rowIndex) {
                   return dataTable.getFormattedValue(rowIndex, 1);
                 },
                 'type': 'string'
               }, 2,3,4]
	       //}, 1, 2, 3, 4]
           }
         });
      
         var data = new google.visualization.DataTable(jsonData);
         data.addColumn('datetime', 'Date');
         //data.addColumn('number', 'Sensor Value');

	

         dashboard.bind(control, chart);
         dashboard.draw(data);
	 refreshData();
	 setInterval(refreshData, 1000*60);
      }
      

      google.setOnLoadCallback(drawVisualization);
    </script>
  </head>
  <body>
    <div id="dashboard" style='width: 100%; height: 100%;'></div>
	Latest readings:
	<div id="gauge_div" ></div>
	<div id="chart" style='width: 100%; height: 500px'></div>
	<div id="control" style='width: 100%; height: 50px;'></div>

    </div>
  </body>
</html>