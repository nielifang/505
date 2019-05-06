/**
 * Created by asus on 2019/3/20.
 */
var oBox = document.getElementById('cont');
    oBox.onmousedown = function(e){
        e = e ||event;
        var x = e.clientX;
        var y = e.clientY;
        var oBoxL = oBox.offsetLeft;
        var oBoxT = oBox.offsetTop;
        var oBoxW = oBox.offsetWidth;
        var oBoxH = oBox.offsetHeight;

        var d = 0;
        if(x < oBoxL + 10){
            d = 'left';
        }
        else if(x > oBoxL + oBoxW -10){
            d = 'right';
        }

        if(y < oBoxT + 10){
            d = 'top';
        }
        else if(d < oBoxT + oBoxH -10){
            d = 'bottom';
        }
        if(x < oBoxL + 10 && y < oBoxT + 10){
            d ='LT';
        }
        document.onmousemove = function(e){
            e = e ||event;
            var xx = e.clientX;
            var yy = e.clientY;
            if(d == 'left'){
                oBox.style.width = oBoxW + x -xx + 'px';
                oBox.style.left = xx  + 'px';
            }
            else if(d == 'right'){
                oBox.style.width = oBoxW + xx -x + 'px'
            }

            if(d == 'top'){
                oBox.style.height = oBoxH + y - yy + 'px';
                oBox.style.top = yy + 'px';
            }
            else if(d == 'bottom'){
                oBox.style.height = oBoxH + yy - y + 'px';
            }
            if(d == 'LT'){
                oBox.style.width = oBoxW + x -xx + 'px'
                oBox.style.left = xx  + 'px';
                oBox.style.height = oBoxH + y - yy + 'px';
                oBox.style.top = yy + 'px';
            }
            return false;
        }
        document.onmouseup = function(){
            document.onmousemove = null;
            document.onmouseup = null;
        }
        if(e.preventDefault){
            e.preventDefault();
        }
    };





