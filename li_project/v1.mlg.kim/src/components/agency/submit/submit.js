export default {
    data () {
        return {
            choiceColorA: '0',
            choiceColorB: '0',
            choiceColorC: true,
            choiceColorD: true,
            classifier:"个",
            classifiers:['个','只'],
            hours:['1小时内','2小时内','6小时内','12小时内', '24小时内'],
            hour:"1小时内",
            describe:'用来夏天做衣服的布料',
            numberGoods:12,
            order:"不接受",
            futures:"现货",
            timeToFind:"1",
            phone:"110"
        }
    },
    methods: {
        numberGoodsAdd: function () {
            this.numberGoods = this.numberGoods + 1
        },
        numberGoodsSub: function () {
            this.numberGoods = this.numberGoods - 1
        },
        olderAccept: function () {
            this.choiceColorA = '1';
            this.choiceColorB='0'
        },
        olderUnAccept: function () {
            this.choiceColorA='0';
            this.choiceColorB='1'
        },
        nowGoods: function () {
            this.choiceColorC= !this.choiceColorC;
        },
        featureGoods:function () {
            this.choiceColorD= !this.choiceColorD;
        }
    }
}