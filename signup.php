<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php
        require('config/connection.php');
        // If form submitted, insert values into the database.
        if (isset($_REQUEST['nama'])){
                // removes backslashes
            $nama = stripslashes($_REQUEST['nama']);
                //escapes special characters in a string
            $nama = mysqli_real_escape_string($conn,$nama); 
            $email = stripslashes($_REQUEST['email']);
            $email = mysqli_real_escape_string($conn,$email);
            $password = stripslashes($_REQUEST['password']);
            $password = mysqli_real_escape_string($conn,$password);
                $query = "INSERT into `tryuser` (nama, email, password)
        VALUES ('$nama', '$email','".md5($password)."')";
                $result = mysqli_query($conn,$query);
                if($result){
                    echo "<div class='form'>
        <h3>You are registered successfully.</h3>
        <br/>Click here to <a href='login.php'>Login</a></div>";
                }
            }else{
    ?>
    <div class="wrapper">
        <h1>Sign Up</h1>
        <div class="form-signup">
            <form>
                <div class="input-box">
                    <input type="text" name="nama" id="name" placeholder="Masukkan Nama">
                </div>
                <div class="input-box">
                    <input type="text" name="email" id="email" placeholder="Masukkan Email">
                </div>
                <div class="input-box">
                    <input type="password" name="passwod" id="password" placeholder="Masukkan Password">
                </div>
                <div class="captchaBackground">
                    <canvas id="captcha">captcha text</canvas>
                </div>
                <button id="refreshButton" type="submit">Refresh</button>
                <div class="input-box">
                    <input id="textBox" type="text" name="text" placeholder="Masukkan Captcha">
                </div>
                <button type="submit" class="btn">Submit</button>
            </form>
        </div>
    </div>
    <script src="script.js"></script>
    <?php } ?>
</body>
</html>