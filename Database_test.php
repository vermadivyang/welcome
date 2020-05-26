<?php
if(array_key_exists('Submit', $_POST)) { 
            doIt(); 
        } 

function doIt() {  
	$id = $_POST['id'];
	$password = $_POST['password'];
	$username = $_POST['username'];
	$email = $_POST['email'];

	if(!emtpy($id) ||!emtpy($password) || !emtpy($username) || ($email)){
		$host = "localhost";
		$dbUsername = "root";
		$dbPassword = "";
		$dbname = "users";
		
		$conn = new sqli($host, $dbUsername, $dbPassword, $dbname);
		if (mysqli_connect_errno()){
			die('Connect Error('.mysqli_connect_errno().')'.mysqli_connect_error());
		} else{
			$SELECT = 'SELECT email From users Where email = ? limit 1';
			$INSERT = 'INSERT into users($password, $username, $email, $id) values(?, ?, ?, ?)';
			
			$stmt = $conn ->perpare($SELECT);
			$stmt -> blind_param("s", $email);
			$stmt -> execute();
			$stmt -> blind_resutle($email);
			$stmt -> store_resutle();
			$rnum = $stmt -> num_rows();
			
			if (rnum == 0){
				$stmt -> close();
				
				$stmt = $conn -> prepare(INSERT);
				$stmt -> blind_param("ssssii", $email, $password, $username, $id);
				$stmt -> execute();
				echo 'Your informaton is inserted';
			} else{
				echo 'You cannot make 2 accouts with the same email';
			}
			
			$stmt ->close();
			$conn ->close();
		}
	} else{
		echo 'Are all of them filled in';
		die();
	}
}
?>