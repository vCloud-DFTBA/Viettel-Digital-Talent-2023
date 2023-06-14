<?php
function query() {
    ########## CONFIG HERE ##########
    $host = "172.16.1.101";
    $port = "30336";
    $dbname = "simplewebapp";
    $user = "root";
    $password = "123";
    #################################

    $pdo = new \PDO("mysql:host=$host;port=$port;dbname=$dbname", $user, $password);
    $records = $pdo->query("SELECT * FROM test ORDER BY id;")->fetchAll();
    return $records;
}
?>