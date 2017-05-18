<?php
$conn = new mysqli('localhost','dniemitalo','','movies');
$sql = "SELECT first, last, age FROM actors";
$result = mysqli_query($conn, $sql);

$row = mysqli_fetch_assoc($result);
echo $row['first'] . " " . $row['last'] . ", age: " . $row['age'] . "<br>";

$row = mysqli_fetch_assoc($result);
echo $row['first'] . " " . $row['last'] . ", age: " . $row['age'] . "<br>";

mysqli_close($conn);
?>