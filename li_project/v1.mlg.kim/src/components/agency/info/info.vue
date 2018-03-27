<template>
    <div class="index-mobile">
        <div class="bannar-warp">
             <div>客户需求描述</div>
             <div class="icon"><i class="iconfont">&#xe621;</i></div>
        </div>
        <div class="content-modular"  >
            <div v-text="describe" class="describe"></div>
            <div class="pic-a"><img src="../../../res/submit/example.png" alt=""></div>
            <div class="pic-b"><img src="../../../res/submit/example.png" alt=""></div>
            <div class="pic-c"><img src="../../../res/submit/example.png" alt=""></div>
            <div class="content-text"></div>
            <div class="modular-line"></div>
            <div class="buy-number">
                <div class="number-left">采购数量</div>
                <div class="number-right"><span v-text="buyNumber"></span><span>个</span></div>
            </div>
            <div class="division"></div>
            <div class="buy-number">
                <div class="number-left">可接受类似或订做</div>
                <div class="number-right"><span v-text="order"></span></div>
            </div>
            <div class="division"></div>
            <div class="buy-number">
                <div class="number-left">现货还是期货</div>
                <div class="number-right"><span v-text="futures"></span></div>
            </div>
            <div class="division"></div>
            <div class="buy-number">
                <div class="number-left">限时找</div>
                <div class="number-right"><span v-text="timeToFind"></span><span>小时内</span></div>
            </div>
            <div class="division"></div>
            <div class="buy-number">
                <div class="number-left">允许客服联系你</div>
                <div class="number-right"><span v-text="phone"></span></div>
            </div>
            <div class="division"></div>
            <div class="bannar-warp sureBtn">
                <div>接单</div>
            </div>

        </div>
    </div>
</template>
<script src="./info.js"></script>
<style src="./info.scss" lang="scss"></style>
