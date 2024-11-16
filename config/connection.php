<?php 
$conn = mysqli_connect('localhost:3307','root','','femminder');

 
// Check connection
if (mysqli_connect_errno()){
	echo "Koneksi database gagal : " . mysqli_connect_error();
}
 
?>