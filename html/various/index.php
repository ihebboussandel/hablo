<?php
$status = shell_exec("ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo 1 || echo 0");
if($status==1){
echo 'network is working';
include 'configssid.php';
}elseif($status==0){
echo 'there is no network';
include 'configssid.php';
}

?>
