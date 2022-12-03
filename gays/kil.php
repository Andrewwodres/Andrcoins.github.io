<?php

	$db = new PDO(dsn:"mysql=localhost;dbname=sevendaydist");
	
	$info = []
	
	if ($query = $db->query(statement:"SELECT * FROM distime")){
		$info = $query->fetchAll(fetch_style: PDO::FETCH_ASSOC);
	} else{
		print_r($db->errorinfo());
	}

?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Andrcoins.необман</title>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
	<?php foreach ($info as $data): ?>
		<div class ="text">
			<text><?php echo $data['dayid']?>
			<text><?php echo $data['massa']?>
			<text><?php echo $data['timeup']?>
			<text><?php echo $data['timedown']?>
	<?php endforeach; ?>
    <table border="1" align="center" width="85%">
		<tr>
	<th>номер дня</th>
	<th>вес</th>
	<th>время подъема</th>
	<th>время в кровать</th>
	</tr>
		<tr>
	<td>0</td>
	<td>53</td>
	<td>12/02/2022, 8:24:34</td>
	<td>12/02/2022, 23:54:44</td>
	</tr>
		<tr>
	<td>1</td>
	<td>55</td>
	<td>12/03/2022, 10:12:24</td>
	<td>12/03/2022, 23:12:24</td>
	</tr>
	</table>
	
    <py-script>
        from datetime import datetime
        now = datetime.now()
        now.strftime("%m/%d/%Y, %H:%M:%S")
    </py-script>
    на момент прверки
</body>
</html>
