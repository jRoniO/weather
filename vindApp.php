<meta http-equiv="refresh" content="1">

<?php

$temp = file_get_contents("vindData.txt");
$temp1 = file_get_contents("tempData.txt");

if ($temp){
        $color="blue";
        }

if ($temp1){
        $color1="red";
        }

print "<h1 style='text-align:center;'>Avläsning för temperatur och vindhastighet</h1>";
print "<br>";

print "<p style='text-align:center; font-size:100px; margin-top:10px; margin-bottom:10px; color:".$color.";'>".$temp."</p>";
print "<p style='text-align:center; font-size:100px; margin-top:20px; margin-bottom:20px; color:".$color1.";'>".$temp1."</p>";

?>
