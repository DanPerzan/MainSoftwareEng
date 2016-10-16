<?php
$info = ["loggedIn" => false];
if ($_POST["username"] === "abc" && $_POST["password"] === "def") {
    $info["loggedIn"] = true;
}
echo json_encode($info);