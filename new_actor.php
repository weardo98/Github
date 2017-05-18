<?php
//Try going to this web address:
//https://block3php-dniemitalo.c9users.io/SQLdatabase/new_actor.php?first=Will&last=Ferrel&age=49


//This uses URL parameters. Everything after "?" is the parameters.
//"first=Will" is the first parameter
//The second parameter comes after "&" and so on.
//The parameters can be fetched from PHP using $_GET
//Later, you can use an HTML form to send GET data to PHP.

//Storing the GET data into variables makes your $sql command a bit easier to read
$first = $_GET['first'];
$last = $_GET['last'];
$age = $_GET['age'];

$conn = new mysqli('localhost','dniemitalo','','movies');
//Notice that $first has single quotes around it and the entire thing has double quotes
$sql = "INSERT INTO actors (first, last, age) VALUES ('$first','$last',$age)";
//You can echo your $sql and test it in mySQL command line to troubleshoot
echo $sql . "<br>";

if($result = mysqli_query($conn, $sql)){
    echo "New record saved successfully: $first $last $age";
}
else{
    echo mysqli_error($conn);
}
mysqli_close($conn);
?>