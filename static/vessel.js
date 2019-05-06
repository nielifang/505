/**
 * Created by asus on 2019/3/19.
 */

// var mpx = 0;
// var mpy = 0;
// function show_hide_div() {
//     // $("#top").click(function () {
//
//         var theDiv = document.getElementById("mdiv");
//         if (theDiv.style.visibility = "hidden")
//             theDiv.style.visibility = "visible";
//         else
//             theDiv.style.visibility = "hidden";
//
//     // })
//
// }
//
// function finddiv(ev, mdiv) {
//     obj = mdiv;
//     x = ev.clientX - parseInt(obj.style.left);
//     y = ev.clientY - parseInt(obj.style.top);
//
// }
// function movediv(ev) {
//     if (obj == 0) {
//         return false;
//     }
//     else {
//
//         ev = ev || window.event;
//         var mousePos = mouseCoords(ev);
//         if (mousePos.y < 10)return;
//         mpx = mousePos.x - x;
//         mpy = mousePos.y - y;
//
//         obj.style.left = mpx + "px";
//         obj.style.top = mpy + "px";
//     }
// }
// function mouseCoords(ev) {
//     if (ev.pageX || ev.pageY) {
//         return {x: ev.pageX, y: ev.pageY};
//     }
//     return {x: ev.clientX + document.documentElement.scrollLeft, y: ev.clientY + document.documentElement.scrollTop}
// }
//
//
// function show_hide_div2() {
//
//     var theDiv = document.getElementById("mdiv2");
//     if (theDiv.style.visibility == "hidden")
//         theDiv.style.visibility = "visible";
//     else
//         theDiv.style.visibility = "hidden";
//
// }
//
// function finddiv2(ev, mdiv) {
//     obj = mdiv;
//     x = ev.clientX - parseInt(obj.style.left);
//     y = ev.clientY - parseInt(obj.style.top);
//
// }
// function movediv2(ev) {
//     if (obj == 0) {
//         return false;
//     }
//     else {
//
//         ev = ev || window.event;
//         var mousePos = mouseCoords(ev);
//         if (mousePos.y < 10)return;
//         mpx = mousePos.x - x;
//         mpy = mousePos.y - y;
//
//         obj.style.left = mpx + "px";
//         obj.style.top = mpy + "px";
//     }
// }
// function mouseCoords2(ev) {
//     if (ev.pageX || ev.pageY) {
//         return {x: ev.pageX, y: ev.pageY};
//     }
//     return {x: ev.clientX + document.documentElement.scrollLeft, y: ev.clientY + document.documentElement.scrollTop}
// }


function myfunction() {
    var x = document.getElementById("ui-Resizable-1");
    vesWidth = x.style.width;
    // var s='<div class="bay1" id="box"></div>';
    // $("#content").append(s);
    $("#box").style.display = "block";

    // alert(666);
    alert(x.style.width);

}


//	ctrl ：控制元素，panel ：面板 ， type 类型
var m_panel, m_ctrl, m_type;
var moving = 0, m_start_x = 0, m_start_y = 0, m_to_x = 0, m_to_y = 0;
//	面板最小尺寸
var m_min_w = 100, m_min_h = 40;
//	在控制元素中按下
function on_mousedown(e, panel, ctrl, type) {
    var e = e || window.event;
    //	计算出鼠标页面位置 和 当前元素位置的差 = 鼠标相对元素的位置
    m_start_x = e.pageX - ctrl.offsetLeft;
    m_start_y = e.pageY - ctrl.offsetTop;
    m_panel = panel;
    m_ctrl = ctrl;
    m_type = type;
    //	开始处理移动事件
    moving = setInterval(on_move, 10);
}
//	页面鼠标移动侦听处理
document.onmousemove = function (e) {
    var e = window.event || e;
    m_to_x = e.pageX;
    m_to_y = e.pageY;
}
//	鼠标移动处理
function on_move() {

    if (moving) {
        var to_x = m_to_x - m_start_x;
        var to_y = m_to_y - m_start_y;
        switch (m_type) {
            case 'r' :
                m_ctrl.style.left = to_x + "px";
                m_panel.style.width = to_x + 10 + 'px';
                break;
            case 'b' :
                m_ctrl.style.top = to_y + "px";
                m_panel.style.height = to_y + 10 + 'px';
                break;
            case 'rb' :
                m_ctrl.style.left = to_x + "px";
                m_ctrl.style.top = to_y + "px";

                m_panel.style.width = to_x + 20 + 'px';
                m_panel.style.height = to_y + 20 + 'px';
                break;
        }
    }

}
//	鼠标弹起处理
document.onkeyup = document.onmouseup = function (e) {
    clearInterval(moving);
    var cls = document.getElementsByClassName('ui-Resizable-ctrl');
    for (var i = 0; i < cls.length; i++) {
        cls[i].style.left = '';
        cls[i].style.top = '';
    }
}
function Resizable1(panelId) {

    var panel = document.getElementById(panelId);
    //	插入调整控制元素
    var r = document.createElement("div");
    var b = document.createElement("div");
    var rb = document.createElement("div");

    r.class = r.className = 'ui-Resizable-r-1  ui-Resizable-ctrl';
    b.class = b.className = 'ui-Resizable-b-1  ui-Resizable-ctrl';
    rb.class = rb.className = 'ui-Resizable-rb-1 ui-Resizable-ctrl';
    panel.appendChild(r);
    panel.appendChild(b);
    panel.appendChild(rb);
    //	为调整控制元素设置拖拽处理
    r.addEventListener('mousedown', function (e) {
        on_mousedown(e, panel, r, 'r');
    })
    b.addEventListener('mousedown', function (e) {
        on_mousedown(e, panel, b, 'b');
    })
    rb.addEventListener('mousedown', function (e) {
        on_mousedown(e, panel, rb, 'rb');
    })
}
Resizable1('ui-Resizable-1');





