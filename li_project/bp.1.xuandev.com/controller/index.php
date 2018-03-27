<?php

class index extends engine {
    public function home() {
        $smarty = new Smarty();
        
        $quizType = mt_rand(1, 3);

        $shareTitle = [
            "1",
            "2"
        ];

        $index = mt_rand(0, 1);
        $smarty->assign("tilte", $shareTitle[$index]);

        ##储存风格
        session_start();
        $_SESSION["quiz_type"] = $quizType;
        $smarty->assign("quiz_type", $_SESSION["quiz_type"]);

        $smarty->display("index.html");
    }

    public function result() {
        $smarty = new Smarty();
        $smarty->display("result.html");
    }
}