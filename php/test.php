<?php
    class Car {
        public $color;
        public $model;
        public function __construct($color, $model) {
          $this->color = $color;
          $this->model = $model;
        }
        public function message() {
          echo __CLASS__;
          return "My car is a " . $this->color . " " . $this->model . "!";
        }
    }

    $myCar = new Car("red", "Volvo");
    var_dump($myCar);

    echo "</br>";
    echo "</br>";

    $a = array("Volvo", "BMW", "Toyota"); // indexed array
    $b = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43"); // associative array

    $a = (object) $a;
    $b = (object) $b;

    //To verify the type of any object in PHP, use the var_dump() function:
    var_dump($a);
    var_dump($b);
    
    echo "</br>";
    

    define("cars", [
        "Alfa Romeo",
        "BMW",
        "Toyota"
    ]);
    echo cars[0];
    echo "</br>";
    
    echo __DIR__;
    echo "</br>";
    echo __FILE__;
    echo "</br>";
    
    function echoFuncName() {
        echo __FUNCTION__;
    }
    // __LINE__
    // __METHOD__
    // __NAMESPACE__
    // __TRAIT__
    echoFuncName();
    echo "</br>";

    $members = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    foreach ($members as $x => $y) {
    echo "$x : $y <br>";
    }

    $colors = array("red", "green", "blue", "yellow");
    foreach ($colors as $x) {
    if ($x == "blue") break;
    echo "$x <br>";
    }

    $myCar = new Car("red", "Volvo");
    foreach ($myCar as $x => $y) {
    echo "$x: $y <br>";
    }

    // by using the & character in the foreach declaration, the array item is assigned by reference, which results in any changes done to the array item will also be done to the original array
    $colors = array("red", "green", "blue", "yellow");
    foreach ($colors as &$x) {
    if ($x == "blue") $x = "pink";
    }
    var_dump($colors);

    echo "</br>";

    $age = array("Peter"=>35, "Ben"=>37, "Joe"=>43);
    echo json_encode($age);

    echo "</br>";

    $jsonobj = '{"Peter":35,"Ben":37,"Joe":43}';
    var_dump(json_decode($jsonobj));

    echo "</br>";
?>
<!DOCTYPE html>
<html>

<body>

    <?php
    echo "My first PHP script!";
    ?>

</body>

</html>