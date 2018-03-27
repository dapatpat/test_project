<template>
    <div class="index-mobile">
        <div class="bannar-warp">
             <div>我要找版</div>
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
                <div class="number-right">
                     <div class="number"> <span style="color:#999">请输入数量</span></div>
                    <div class="subtrac"> <i class="iconfont" @click="numberGoodsSub"> &#xe8b6;</i> </div>
                    <div class="number"> <span  v-text="numberGoods"></span></div>
                    <div class="add"><i class="iconfont" @click="numberGoodsAdd">&#xe8de; </i> </div>
                    <div class="Classifier">
                        <select class="ch-time">
                            <option v-text="classifier" :value="classifier"  v-for="classifier in classifiers"></option>
                        </select>
                    </div>
                     <span> <i class="iconfont"> &#xe656;</i></span>
                </div>
            </div>
            <div class="division"></div>
            <div class="buy-number">
                <div class="number-left">可接受类似或订做</div>
                <div class="number-right">
                    <div class="subtrac">
                        <div class="ticks" :style="choiceColorA== 0 ? 'display:none' : 'display:block'"> <i class="iconfont tick" >&#xe610;</i></div>
                        <i class="iconfont" :style="choiceColorA== 0 ? 'color:#ffd4d4': 'color:#ea6556'" @click="olderAccept"> &#xe8b5;</i>
                    </div>
                    <div class="number" @click="olderAccept"> <span >接受</span></div>
                    <div class="add">
                         <div class="ticks" :style="choiceColorB == 0 ? 'display:none' : 'display:block'" > <i class="iconfont tick" >&#xe610;</i></div>
                        <i class="iconfont" :style="choiceColorB == 0 ? 'color:#ffd4d4': 'color:#ea6556'" @click="olderUnAccept"> &#xe8b5;</i>
                    </div>
                    <div class="Classifier" @click="olderUnAccept">不接受</div>
                </div>
            </div>
            <div class="division"></div>
            <div class="buy-number">
                <div class="number-left">现货还是期货</div>
                <div class="number-right">
                    <div class="subtrac">
                         <div class="ticks" :style="choiceColorC ? 'display:none' : 'display:block'" @click="nowGoods"> <i class="iconfont tick"  >&#xe610;</i></div>
                        <i class="iconfont" :style="choiceColorC ? 'color:#ffd4d4': 'color:#ea6556'" @click="nowGoods"> &#xe8b5;</i>
                    </div>
                    <div class="number" @click="nowGoods"> <span >现货</span></div>
                    <div class="add">
                        <div class="ticks" :style="choiceColorD ? 'display:none' : 'display:block'" @click="featureGoods"> <i class="iconfont tick" >&#xe610;</i></div>
                        <i class="iconfont" :style="choiceColorD  ? 'color:#ffd4d4': 'color:#ea6556'"  @click="featureGoods"> &#xe8b5;</i>
                    </div>
                    <div class="Classifier"  @click="featureGoods">期货</div>
                </div>
            </div>
            <div class="division"></div>
            <div class="buy-number">
                <div class="number-left">限时找</div>
                <div class="number-right" >
                    <select v-model="hour" class="ch-time">
                        <option v-for="hour in hours" :value="hour"  v-text="hour"></option>
                    </select>
                    <span><i class="iconfont">&#xe656;</i></span>
                </div>
            </div>
            <div class="division"></div>
            <div class="buy-number">
                <div class="number-left">允许客服联系你</div>
                <div class="number-right" ><input type="text" class="contact-phone" placeholder="请输入手机号"></div>
            </div>
            <div class="division"></div>
            <div class="rules">
                 <div class="rules-left"><span><i class="iconfont">&#xe60a;</i></span></div>
                 <div class="rules-right">了解规则</div>
             </div>
            <div class="payment">
                <div class="payment-left">
                    <span><i class="iconfont">&#xe60a;</i></span>
                    <span>60</span>
                </div>
                <router-link tag="span" :to="{name:'board'}">
                    <div class="payment-right"><span>免费发布</span></div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script src='./submit.js'></script>
<style src='./submit.scss' lang="scss"></style>
