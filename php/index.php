<?php
    echo 'Hello from PHP!';
    echo '<br />';
    print 'Hello from Print!';
    echo '<br />';
    echo 'Value one; ', 'Value two';

    $title = 'Learn English with Us!!!';
    $heading = 'Boost Your English Skills!';

    echo '<br />';
    var_dump($title);
    echo '<br />';
    echo getType($heading);

    $friends = ['Akiyama', 'Nhat Vu'];
    echo '<br />';
    var_dump($friends);

    $person = new stdClass();
    echo '<br />';
    var_dump($person);

    $car = null;

    // resource
    $file = fopen('README.md', 'r');
    echo '<br />';
    var_dump($file);

    $firstName = 'John';
    $lastName = 'Doe';
    $fullname = $firstName . ' ' . $lastName;
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $title ?></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 40px;
            text-align: center;
        }
        .container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            width: 80%;
            margin: auto;
        }
        .header {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 8px 8px 0 0;
        }
        .content {
            margin: 20px 0;
        }
        .footer {
            font-size: smaller;
            color: #888;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><?= $heading ?></h1>
        </div>
        <div class="content">
            <p>Join our expert-led English courses available online and in-person. Tailored to all levels from beginners to advanced speakers.</p>
            <p>Our interactive sessions help you improve grammar, vocabulary, and pronunciation.</p>
            <p>Flexible schedules and competitive pricing. Enroll now and start your journey to fluency!</p>
            <button style="padding: 10px; font-size: large; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">Enroll Today</button>
        </div>
        <div class="footer">
            Contact us at info@englishlearning.com
        </div>
        <p><?= 'Hello, my name is ' . $fullname . '<br />' ?></p>
        <p><?= "Hello, my name is $fullname" ?></p>
    </div>
</body>
</html>