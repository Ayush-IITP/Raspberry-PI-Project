<?php
/**Authors   Rijul Dhir and Ayush Mishra **/
/**          1501CS37     1501CS16      **/ 
exec("gpio mode 25 out");  // Execute Command on Terminal using Wiring Pi
exec("gpio mode 23 out");  
exec("gpio mode 24 out");  // THese are using Wiring Pi GPIO pin Numbers
exec("gpio mode 22 out");  // Red-22,Yellow-24,Green-23,White-25
/** 16 If Statements to run various LED's.**/
if (($_GET['red']==0)&&($_GET['yellow']==0)&&($_GET['green']==0)&&($_GET['white']==0)) {
        exec("gpio write 22 0");
        exec("gpio write 24 0");
        exec("gpio write 23 0");
        exec("gpio write 25 0");

}
if (($_GET['red']==0)&&($_GET['yellow']==0)&&($_GET['green']==0)&&($_GET['white']==1)){
        exec("gpio write 22 0");
        exec("gpio write 24 0");
        exec("gpio write 23 0");
        exec("gpio write 25 1");
        sleep(1);
}
if (($_GET['red']==0)&&($_GET['yellow']==0)&&($_GET['green']==1)&&($_GET['white']==0)){
        exec("gpio write 22 0");
        exec("gpio write 24 0");
        exec("gpio write 23 1");
        exec("gpio write 25 0");

}
if (($_GET['red']==0)&&($_GET['yellow']==0)&&($_GET['green']==1)&&($_GET['white']==1)){
        exec("gpio write 22 0");
        exec("gpio write 24 0");
        exec("gpio write 23 1");
        exec("gpio write 25 1");

}
if (($_GET['red']==0)&&($_GET['yellow']==1)&&($_GET['green']==0)&&($_GET['white']==0)){
        exec("gpio write 22 0");
        exec("gpio write 24 1");
        exec("gpio write 23 0");
        exec("gpio write 25 0");
}
if (($_GET['red']==0)&&($_GET['yellow']==1)&&($_GET['green']==0)&&($_GET['white']==1)){
        exec("gpio write 22 0");
        exec("gpio write 24 1");
        exec("gpio write 23 0");
        exec("gpio write 25 1");

}
if (($_GET['red']==0)&&($_GET['yellow']==1)&&($_GET['green']==1)&&($_GET['white']==0)){
        exec("gpio write 22 0");
        exec("gpio write 24 1");
        exec("gpio write 23 1");
        exec("gpio write 25 0");

}
if (($_GET['red']==0)&&($_GET['yellow']==1)&&($_GET['green']==1)&&($_GET['white']==1)){
        exec("gpio write 22 0");
        exec("gpio write 24 1");
        exec("gpio write 23 1");
        exec("gpio write 25 1");

}
if (($_GET['red']==1)&&($_GET['yellow']==0)&&($_GET['green']==0)&&($_GET['white']==0)){
        exec("gpio write 22 1");
        exec("gpio write 24 0");
        exec("gpio write 23 0");
        exec("gpio write 25 0");

}
if (($_GET['red']==1)&&($_GET['yellow']==0)&&($_GET['green']==0)&&($_GET['white']==1)){
        exec("gpio write 22 1");
        exec("gpio write 24 0");
        exec("gpio write 23 0");
        exec("gpio write 25 1");

}
if (($_GET['red']==1)&&($_GET['yellow']==0)&&($_GET['green']==1)&&($_GET['white']==0)){
        exec("gpio write 22 1");
        exec("gpio write 24 0");
        exec("gpio write 23 1");
        exec("gpio write 25 0");

}
if (($_GET['red']==1)&&($_GET['yellow']==0)&&($_GET['green']==1)&&($_GET['white']==1)){
        exec("gpio write 22 1");
        exec("gpio write 24 0");
        exec("gpio write 23 1");
        exec("gpio write 25 1");

}
if (($_GET['red']==1)&&($_GET['yellow']==1)&&($_GET['green']==0)&&($_GET['white']==0)){
        exec("gpio write 22 1");
        exec("gpio write 24 1");
        exec("gpio write 23 0");
        exec("gpio write 25 0");

}
if (($_GET['red']==1)&&($_GET['yellow']==1)&&($_GET['green']==0)&&($_GET['white']==1)){
        exec("gpio write 22 1");
        exec("gpio write 24 1");
        exec("gpio write 23 0");
        exec("gpio write 25 1");

}
if (($_GET['red']==1)&&($_GET['yellow']==1)&&($_GET['green']==1)&&($_GET['white']==0)){
        exec("gpio write 22 1");
        exec("gpio write 24 1");
        exec("gpio write 23 1");
        exec("gpio write 25 0");

}
if (($_GET['red']==1)&&($_GET['yellow']==1)&&($_GET['green']==1)&&($_GET['white']==1)){
        exec("gpio write 22 1");
        exec("gpio write 24 1");
        exec("gpio write 23 1");
        exec("gpio write 25 1");

}
?>
