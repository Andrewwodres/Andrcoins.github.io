<?php

	$db = new PDO(dsn:"mysql=localhost;dbname=sevendaydist");
	
	$info = []
	
	if ($query = $db->query(statement:"SELECT * FROM distime")){
		$query->fetchAll();
	}

?>

<html>
<head>
    <meta charset="UTF-8">
    <title>Andrcoins.необман</title>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
    <table>
		<tr>
	<td>номер дня</td>
	<td>вес</td>
	<td>время подъема</td>
	<td>время в кровать</td>
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