<template>
<body style="color:#fafafa">
    <div id="" class="index-mobile">
        <div class="bannar-warp">
             <div>反馈结果</div>
             <div class="icon"><i class="iconfont">&#xe621;</i></div>
        </div>
        <form action="" method="post">
            <div class="content-modular"  >
                 <div class="content-text">
                     <div  v-text="results" class="results">反馈一</div>
                 </div>
                 <div class="modular-line"></div>
                 <div class="buy-number">
                     <div class="number-left">档口名字：</div>
                     <div class="number-right"><input type="text" class="text-input" v-model="shopName"></div>
                 </div>
                 <div class="division"></div>
                 <div class="buy-number">
                     <div class="number-left">档口地址：</div>
                     <div class="number-right"><input type="text" class="text-input" v-model="address"></div>
                 </div>
                 <div class="division"></div>
                 <div class="buy-number">
                     <div class="number-left">档口联系电话：</div>
                     <div class="number-right"><input type="text" class="text-input" v-model="phone"></div>
                 </div>
                 <div class="division"></div>
                 <div class="buy-number">
                     <div class="number-left">价格：</div>
                     <div class="number-right"><input type="text" class="text-input" v-model="price"></div>
                 </div>
                 <div class="division"></div>
                 <div class="buy-number">
                     <div class="number-left">现货：</div>
                     <div class="number-right"><input type="text" class="text-input" v-model="goods"></div>
                 </div>
                 <div class="division"></div>
                 <div class="bannar-warp sureBtn">
                     <div>提交反馈</div>
                 </div>
            </div>
        </form>
    </div>
</body>
</template>
<script src="./detail.js"></script>
<style src='./detail.scss' lang="scss"></style>