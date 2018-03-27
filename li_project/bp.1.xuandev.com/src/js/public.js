(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-92633598-10', 'auto');

if (document.getElementById("platform-input").value.indexOf("UCNewsApp") >= 0) {
    ga('set', 'dimension1', 2);     //1 非ucnews   2 ucnews
} else {
    ga('set', 'dimension1', 1);     //1 非ucnews   2 ucnews
}

ga('send', 'pageview');