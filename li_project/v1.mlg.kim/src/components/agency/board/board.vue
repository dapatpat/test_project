<template>
 <div id="" class="index-mobile">
        <div class="title-text">
            <div class="back-btn"><i class="iconfont">&#xe621;</i></div>
            <div class="demand">我发布的需求</div>
        </div>
        <div class="bannar-swap">
            <div class="respond" @click="changeContainFn('1')" :style="feedback == 1? 'color:#ea6556': ''">待响应</div>
            <div class="seek" @click="changeContainFn('2')" :style="seek == 1? 'color:#ea6556': ''">找版中</div>
            <div class="finsh"  @click="changeContainFn('3')" :style="finsh == 1? 'color:#ea6556': ''">已完成</div>
        </div>
        <div class="contain-line"></div>
        <div class="content">
            <!--待反馈-->
            <div class="content-modular"  :style="feedback == 0 ? 'display:none': 'display:block'" >
                 <div class="pic-a"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-b"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-c"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-d"><i class="iconfont">&#xe64e;</i></div>
                 <div class="content-text" v-text="contentText"></div>
                 <div class="modular-line"></div>
                 <div class="modular-edit">
                     <div class="sent-time" v-text="sentTime"></div>
                     <div class="btn-area">
                         <div class="cancel-btn " ><div class="btn dis "  ></div></div>
                         <div class="edit-btn" >
                             <router-link to='info' tag="span"><div class="btn seek-btn" >取消</div></router-link>
                         </div>
                         <div class="contact-btn">
                             <router-link :to="{name:'submit'}" tag="span"><div class="btn seek-btn" >编辑</div></router-link>
                         </div>
                     </div>
                 </div>
            </div>
            <!--找版中-->
            <div class="content-modular sea-modular"  :style="seek == 0 ? 'display:none': 'display:block'" >
                 <div class="pic-a"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-b"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-c"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-d"><i class="iconfont">&#xe64e;</i></div>
                 <div class="content-text">{{contentText}}</div>
                 <div class="modular-line"></div>
                 <div class="modular-edit">
                     <div class="sent-time">已发布：{{sentTime}}分钟</div>
                     <div class="btn-area">
                         <div class="cancel-btn">
                             <router-link tag="span" :to="{name:'list'}">
                                 <div class="btn sec-btn">有反馈</div>
                             </router-link>
                         </div>
                         <div class="edit-btn"><div class="btn seek-btn">取消</div></div>
                         <div class="contact-btn"><div class="btn seek-btn">联系版哥</div></div>
                     </div>
                 </div>
            </div>
            <!--已完成-->
            <div class="content-modular finsh-modular"   :style="finsh == 0 ? 'display:none': 'display:block'" >
                 <div class="pic-a"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-b"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-c"><img src="../../../res/submit/example.png" alt=""></div>
                 <div class="pic-d"><i class="iconfont">&#xe64e;</i></div>
                 <div class="content-text">{{contentText}}</div>
                 <div class="modular-line"></div>
                 <div class="modular-edit">
                     <div class="sent-time">已发布：{{sentTime}}分钟</div>
                     <div class="btn-area">
                         <div class="cancel-btn"><div class="btn dis"></div></div>
                         <div class="edit-btn"><div class="btn dis"></div></div>
                         <div class="contact-btn">
                             <router-link :to="{name:'detail'}" tag="span"><div class="btn finsh-feedback-btn">反馈</div></router-link>
                         </div>
                     </div>
                 </div>
            </div>
            <!--后台客户需求-->
            <div class="content-modular finsh-modular"   :style="customerDemand == 0 ? 'display:none': 'display:block'" >
                <div class="pic-a"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-b"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-c"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-d"><i class="iconfont">&#xe64e;</i></div>
                <div class="content-text">{{contentText}}</div>
                <div class="modular-line"></div>
                <div class="modular-edit">
                    <div class="sent-time">已发布：{{sentTime}}分钟</div>
                    <div class="btn-area">
                        <div class="cancel-btn"><div class="btn dis"></div></div>
                        <div class="edit-btn"><div class="btn dis"></div></div>
                        <div class="contact-btn">
                            <router-link :to="{name:'info'}" tag="span"><div class="btn finsh-feedback-btn">接单</div></router-link>
                        </div>
                    </div>
                </div>
            </div>
            <!--后台找版中-->
            <div class="content-modular sea-modular"  :style=" findMaterial == 0 ? 'display:none': 'display:block'" >
                <div class="pic-a"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-b"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-c"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-d"><i class="iconfont">&#xe64e;</i></div>
                <div class="content-text">{{contentText}}</div>
                <div class="modular-line"></div>
                <div class="modular-edit">
                    <div class="sent-time">已发布：{{sentTime}}分钟</div>
                    <div class="btn-area">
                        <div class="cancel-btn">
                            <router-link tag="span" :to="{name:'detail'}">
                                <div class="btn sec-btn">反馈</div>
                            </router-link>
                        </div>
                        <div class="edit-btn"><div class="btn seek-btn">取消</div></div>
                        <div class="contact-btn"><div class="btn seek-btn">联系客户</div></div>
                    </div>
                </div>
            </div>
            <!--后台已完成-->
            <div class="content-modular finsh-modular"   :style="finshed == 0 ? 'display:none': 'display:block'" >
                <div class="pic-a"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-b"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-c"><img src="../../../res/submit/example.png" alt=""></div>
                <div class="pic-d"><i class="iconfont">&#xe64e;</i></div>
                <div class="content-text">{{contentText}}</div>
                <div class="modular-line"></div>
                <div class="modular-edit">
                    <div class="sent-time">已发布：{{sentTime}}分钟</div>
                    <div class="btn-area">
                        <div class="cancel-btn"><div class="btn dis"></div></div>
                        <div class="edit-btn"><div class="btn dis"></div></div>
                        <div class="contact-btn">
                            <router-link :to="{name:'detail'}" tag="span"><div class="btn finsh-feedback-btn">反馈</div></router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script src="./board.js"></script>
<style src='./board.scss' lang="scss"></style>
