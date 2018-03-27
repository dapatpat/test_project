export default {
    data () {
        return {
            feedback:"1",
            seek:"1",
            finsh:"1",
            customerDemand: '1',
            findMaterial: '1',
            finshed: '1',
            contentText:"用来做夏天的衣服",
            sentTime:"已经",
            cancel:"取消",
            edit: "取消",
            contact: "编辑",
        }
    },
    methods: {
        changeContainFn:function (cc) {
            if(cc == '1' ){
                this.feedback='1';
                this.seek='0';
                this.finsh='0'
            }else if (cc == '2'){
                this.feedback='0';
                this.seek='1';
                this.finsh='0'
            }else if (cc == '3'){
                this.feedback='0';
                this.seek='0';
                this.finsh='1'
            }

        }
    }
}