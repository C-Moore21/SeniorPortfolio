<?php
// Include config file
require_once 'config.php';

//Define variables and initialize with emptu VALUES

$username = $password = "";
$username_err = $password_err = "";

//Processing form data when form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){

  // Check if username is empty
  if(empty(trim($_POST["username"]))){
    $username_err = 'Please enter username.';
  }
  else{
    $username = trim($_POST["username"]);
  }

  // Check if password is empty
  if(empty(trim($_POST["pass"]))){
    $password_err = 'Please enter your password.';
  }
  else {
    $password = trim($_POST['pass']);
  }

  // Validate credentials
  if(empty($username_err) && empty($password_err)){
    //Prepare a select statement
    $sql = "SELECT username, pass FROM users WHERE username = '".$username."'";

    if($stmt = mysqli_prepare($link, $sql)){
      //Bind varables to prepared statement as paramaters
      //mysqli_stmt_bind_param($stmt, "s", $param_username);

      //Set paramaters
      //$param_username = $username;

      // Attempt to execute the prepared statement
      if(mysqli_stmt_execute($stmt)){
        //Store result
        mysqli_stmt_store_result($stmt);

        //Check if username exists, if yes then verify password
        if(mysqli_stmt_num_rows($stmt) == 1){
          //Bind result variables
          //mysqli_stmt_bind_result($stmt, $username, $hashed_password);
          $hash =password_hash($password, PASSWORD_DEFAULT);
          if(mysqli_stmt_fetch($stmt)){
            if(password_verify($password, $hash)){
              /* Password is correct, so start a new session and
              save the username to the session */
              session_start();
              $_SESSION['username'] = $username;
              header("location: welcome.php");
            }
            else {
              //Display error if you fucked up the password
              $password_err = ' The password you entered was not valid.';
            }
          }
        }
        else{
          //Display error if you fucked up the username_err
          $username_err = 'No account found with that username.';
        }
      }
      else {
        echo "Oops! Something went wrong. Please try again later.";
      }
    }
    //Close statement
    mysqli_stmt_close($stmt);
  }
  //close connection
  mysqli_close($link);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
  <style type="text/css">
    body{ font: 14px sans-serif; }
    .wrapper{ width: 350px; padding: 20px; }
  </style>
</head>
<body>
  <div class="wrapper">
    <h2>Login</h2>
    <p>Please fill in your credentials to login.</p>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
      <div class="form-group <?php echo (!empty($username_err)) ? 'has-error' : ''; ?>">
        <label>Username:<sup>*</sup></label>
        <input type="text" name="username"class="form-control" value="<?php echo $username; ?>">
        <span class="help-block"><?php echo $username_err; ?></span>
      </div>
      <div class="form-group <?php echo (!empty($password_err)) ? 'has-error' : ''; ?>">
        <label>Password:<sup>*</sup></label>
        <input type="password" name="pass" class="form-control">
        <span class="help-block"><?php echo $password_err; ?></span>
      </div>
      <div class="form-group">
        <input type="submit" class="btn btn-primary" value="Submit">
      </div>
    </form>
  </div>
</body>
</html>
