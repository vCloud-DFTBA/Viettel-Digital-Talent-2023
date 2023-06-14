<?php include_once 'config.php'; ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <title>Simple Web App</title>
    <script type="text/javascript">
        var timerStart = Date.now();
    </script>
</head>
<body>
    

    <div class="container-sm text-center">
        <?php
            try {
                $val = query();
                echo "<h2 style='color:green'>Kết nối tới cơ sở dữ liệu thành công!</h2>";
                echo "<h2 style='color:green'>Triển khai website thành công!</h2>";
            } catch(Exception $e) {
                echo "<h2 style='color:red'>Kết nối tới cơ sở dữ liệu thất bại!</h2>";
                echo "<h2 style='color:grey'>Kiểm tra lại thông tin đăng nhập</h2>";
            }
        ?>
    </div>

    <div class="container-sm">
        <div class="row" id="image">
            <div class="col-1"><img src="img/01.jpg" width=100%></div>
            <div class="col-1"><img src="img/02.jpg" width=100%></div>
            <div class="col-1"><img src="img/03.jpg" width=100%></div>
            <div class="col-1"><img src="img/04.jpg" width=100%></div>
            <div class="col-1"><img src="img/05.jpg" width=100%></div>
            <div class="col-1"><img src="img/06.jpg" width=100%></div>
            <div class="col-1"><img src="img/07.jpg" width=100%></div>
            <div class="col-1"><img src="img/08.jpg" width=100%></div>
            <div class="col-1"><img src="img/09.jpg" width=100%></div>
            <div class="col-1"><img src="img/10.jpg" width=100%></div>
            <div class="col-1"><img src="img/11.jpg" width=100%></div>
            <div class="col-1"><img src="img/12.jpg" width=100%></div>
        </div>
        <br>
        <div class="row" id="image">
            <div class="col-1"><img src="img/13.jpg" width=100%></div>
            <div class="col-1"><img src="img/14.jpg" width=100%></div>
            <div class="col-1"><img src="img/15.jpg" width=100%></div>
            <div class="col-1"><img src="img/16.jpg" width=100%></div>
            <div class="col-1"><img src="img/17.jpg" width=100%></div>
            <div class="col-1"><img src="img/18.jpg" width=100%></div>
            <div class="col-1"><img src="img/19.jpg" width=100%></div>
            <div class="col-1"><img src="img/20.jpg" width=100%></div>
            <div class="col-1"><img src="img/21.jpg" width=100%></div>
            <div class="col-1"><img src="img/22.jpg" width=100%></div>
            <div class="col-1"><img src="img/23.jpg" width=100%></div>
            <div class="col-1"><img src="img/24.jpg" width=100%></div>
        </div>
        <br>
        <div class="row">
            <div class="col-auto">Time to load Images: </div>
            <div class="col-auto" id="image-time"></div>
        </div>
        <br>
        </img>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            console.log("Time until DOMready: ", Date.now()-timerStart);
        });
        $(window).load(function() {
            imageLoadTime = Date.now() - timerStart;
            $("#image-time").text(imageLoadTime + "ms");
        });
    </script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js" integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz" crossorigin="anonymous"></script>
</body>
</html>