<?php
?>
<div id="sidebar-menu" class="main_menu_side hidden-print main_menu">

                        <div class="menu_section">
                            <h3>General</h3>
                            <ul class="nav side-menu">
                                <li><a><i class="fa fa-wifi"></i> Configure wifi <span class="fa fa-chevron-down"></span></a>
                                    <ul class="nav child_menu" style="display: none">
                                        <li><a href="set_ssid.php">Set SSID</a>
                                        </li>
                                        <!--<li><a href="display_devices.php">Display Devices</a>
                                        </li>-->
                                        <!--<li><a href="index.php">Wifi Status</a>
                                        </li>-->
                                    </ul>
                                </li>
                            </ul>
                        </div>
<?php 
//$status = shell_exec("ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo 1 || echo 0");
//if($status==1){
//echo 'network is working';
//if code here to be done
//}elseif($status==0){
//echo 'hotspot mode';
include 'mic_menu_section.php';
//}
?>
                         <div class="menu_section">
                            <h3>Tunning</h3>
                            <ul class="nav side-menu">
                                <li><a><i class="fa fa-lightbulb-o"></i> Color Settings <span class="fa fa-chevron-down"></span></a>
                                    <ul class="nav child_menu" style="display: none">
                                        <li><a href="color_change.php">Color Utility</a>
                                        </li>
                                        <!--<li><a href="#">Modes</a>-->
                                        </li>
                                    </ul>
                                </li>
                              <!--  <li><a><i class="fa fa-laptop"></i> Landing Page <span class="label label-success pull-right">Coming Soon</span></a>
                                </li>-->
                            </ul>
                        </div>

                    </div>
		    <!-- menu footer buttons --> 
		    <div class="sidebar-footer hidden-small">
                        <a data-toggle="tooltip" data-placement="top" title="ShutDown Device">
                            <span class="glyphicon glyphicon-off" aria-hidden="true" onclick="call_php_program()"></span>
                        </a>
                    </div>
		  <!-- menu footer buttons --> 
