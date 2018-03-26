<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>留言板</title>
    <script  type="text/javascript" src="./jquery.js"></script>
    <script type="text/javascript" src="./bootstrap.min.js"></script>
    <link href="./bootstrap.min.css" rel="stylesheet">
    <style>
        *{padding:0 0 0 0;margin: 0 0 0 0 }
       .text{border: solid 1px seagreen;margin-top: 20px}
       .sub{margin-top: 10px;float: right}
        .bg{border-radius: 10px;background-color:lightskyblue;height: 200px;opacity:0.6;border: solid 1px seagreen}
        .body{margin-top: 20px;height:60px ;background-color:powderblue;border-radius: 6px;border: solid 1px seagreen;opacity:0.6}
       .btn1{float: right;margin-top:10px;margin-right: 10px;}
       .liuyan{padding: 30px}
        .zc{float: right;padding-left: 20px}
    </style>

</head>
<body class="container" style="margin-top: 20px">
     <div class=" bg col-xs-10 col-xs-offset-1" >
          <div  ><form><textarea name="" class="form-control text" rows="5" style="border-radius: 7px"></textarea></form></div>
          <div class="sub"> (可按Enter 回复)&nbsp;&nbsp;&nbsp;<input  name=" " type="submit" value="提交评论" class="btn btn-danger">  </div>
     </div>

     <div class=" body col-xs-10 col-xs-offset-1 body" >
           <div style="opacity: 1">
               <input class="btn1" type="button" value="3" name="">
               <input class="btn1"  type="button" value="2" name="">
               <input class="btn1" type="button" value="1" name="">
           </div>
           <div style="margin-top:60px;" class="">
               <?php
                  for ($i=0;$i<=10;$i++){
                      echo "<div  class='liuyan' style='border: solid 1px #cccccc;margin:0 -18px 0 -18px'>".$i.".{{留言内容}}<br><br>{{XX年XX月XX日}}<span class='zc'>赞一下{{0}}</span><span class='zc'>踩一下{{0}}</span></div>";
                  }?>
           </div>
     </div>
</body>

<script>
    $(".btn1").addClass('btn btn-info');
    $(".liuyan").css({height:100});
    $('.btn-danger').click(function () {
        var text=( $(".text").val());
        $.ajax({
             method:'post',
            url:"ajax.php",
            data:{a:text},
            success:function (res) {
                alert("评论成功")
            },
            error:function () {
                 alert("评论失败！")
             }
    })})
</script>
</html>