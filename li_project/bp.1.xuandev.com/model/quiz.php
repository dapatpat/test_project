<?php


class quiz extends engine {
	public function getQuiz() {
		$link = D();

		//按照题目套  获取
		$result = $link->query("SELECT * FROM q_question_green_id ORDER BY seq ASC");

        //从题库随机选取题目
//        $result = $link->query("SELECT * FROM q_question_soccer_2 ORDER BY rand() LIMIT 0, 5");
		$data = [];

        while($row = mysqli_fetch_assoc($result)) {
        	$row['content'] = json_decode($row['content'], true);
        	$data[] = $row;
        }

    	return $data;
	}
}