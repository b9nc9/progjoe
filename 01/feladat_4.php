<!DOCTYPE HTML>

<html>
    <head>
        <meta charset="utf-8"/>
        <title>Progjoe 1. feladatos 4. feladat</title>
    </head>
    <body>
        <form method="post">
            <input type="text" name="szoveg">
            <input type="submit">
        
        </form>
        <?php
            $szoveg = "";
            if(isset($_POST["szoveg"])){
                $szoveg = $_POST["szoveg"];
            }
            echo "<p>".$szoveg."</p>";
        ?>
    
    </body>

</html>
