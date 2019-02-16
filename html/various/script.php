<!--php phpinfo(); -->
<?php 
//echo 'ssid ' . htmlspecialchars($_GET["field1"]) . '!\n';
//echo 'pawword ' . htmlspecialchars($_GET["field2"]) . '!\n';
$ssid=$_GET["field1"];
$password=$_GET["field2"];
$key=$_GET["field3"];
$cmd1 = "echo 'network={'";
$cmd2 = "echo '    ssid=\"".$ssid."\"'";
$cmd3 = "echo '    psk=\"".$password."\"'";
$cmd4 = "echo '    key_mgmt=WPA-PSK'";
$cmd5 = "echo '} \n'";
$cmd6 = "echo '    key_mgmt=NONE'";
$cmd_file=">>/etc/wpa_supplicant/wpa_supplicant.conf";
//echo $cmd1.$cmd2.$cmd3.$cmd4.$cmd5.$cmd_file; 
echo shell_exec("sudo chmod 777 /etc/wpa_supplicant/wpa_supplicant.conf");
echo shell_exec($cmd1.$cmd_file);
echo shell_exec($cmd2.$cmd_file);
if ($key == "no") {
    echo shell_exec($cmd6.$cmd_file);
} else {
    echo shell_exec($cmd3.$cmd_file);
    echo shell_exec($cmd4.$cmd_file);
}
echo shell_exec($cmd5.$cmd_file);
echo shell_exec("cat /etc/wpa_supplicant/wpa_supplicant.conf");
echo shell_exec("ls -l /etc/wpa_supplicant/wpa_supplicant.conf");
echo shell_exec('sudo systemctl restart autohotspot.service');
?>
