<?php $data = $_POST['data'];
//$f = fopen('logs/color_status.log', 'w+');
$file = "logs/color_status.log"; 
//fwrite(f, $data);
//fclose($f);7
//file_put_contents($file, $data, FILE_APPEND | LOCK_EX);
file_put_contents($file,$data,LOCK_EX);
?>
