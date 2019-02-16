<?php 
if(isset($_GET["mode"])){
if(isset($_GET["state"])){
$mode=$_GET["mode"];
$state=$_GET["state"];
if($mode=="ai" && $state=="start"){
    echo "<p> " .$mode." + ".$state. "</p>";
    echo shell_exec("sudo systemctl stop hablo_engine_streamer.service"); 
    echo shell_exec("sudo systemctl start hablo_engine.service");
}elseif($mode=="ai" && $state=="stop"){
    echo "<p>, " .$mode." + ".$state. "</p>";
    echo shell_exec("sudo systemctl stop hablo_engine.service");
}elseif($mode=="live_track" && $state=="start"){
    echo "<p>, " .$mode." + ".$state. "</p>";
    echo shell_exec("sudo systemctl stop hablo_engine.service");
    echo shell_exec("sudo systemctl start hablo_engine_streamer.service"); 
}elseif($mode=="live_track" && $state=="stop"){
   echo "<p>, " .$mode." + ".$state. "</p>";
    echo shell_exec("sudo systemctl stop hablo_engine_streamer.service"); 

}
}
}
//echo shell_exec("sudo systemctl start hablo_engine.service");
?>
