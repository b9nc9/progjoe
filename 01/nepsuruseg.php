<!DOCTYPE HTML>

<html>
    <head>
        <meta charset="utf-8"/>
        <title>Népsűrűség</title>
    </head>
    <body>
        <form method="post">
            <input type="number" name="terulet" min="0" placeholder="terület">km<sup>2</sup><br>
            <input type="number" name="lakossag" min="0" placeholder="lakosság"><br>
            <input type="submit" value="Kiszámít">
        </form>
        <?php
            $terulet = 0;
            $lakossag = 0;
            if(isset($_POST["terulet"]) && isset($_POST["lakossag"])){
                $terulet = $_POST["terulet"];
                $lakossag = $_POST["lakossag"];
                echo "<p>".($lakossag/$terulet)."</p>";
            }
        ?>
    
    </body>

</html>
