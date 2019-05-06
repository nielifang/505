//克隆节点
//克隆事件
var old = 1;

$("#btn20").on('click', function () {
var z='bay' + old;
    $(".content").append($(this).clone(false).attr('id', z).css({
        'height': '150px',
        'background-color': '#b9def0'
    }));
    old += 1;

     $("#"+z).click(function (){
        $(this).remove();
         old-=1
    });


});

$("#btn40").on('click', function () {
    var y='bay' + old;
    $(".content").append($(this).clone(false).attr('id', y).css({
        'height': '150px',
        'width': '60px',
        'background-color': '#28a4c9'
    }));
    old += 1;



     $("#"+y).click(function (){
        $(this).remove();
         old-=1
    });
    // $(".ves20").css('display','block')
});
$("#btn").on('click', function () {
    var x='bay' + old;
    $(".content").append($(this).clone(false).attr('id',x,'class','b').css({'height': '150px',
        'width': '30px'}));
    old += 1;

    // $("#"+x).click(function (){
    //     $(this).remove();
    //     old-=1
    // });
});


$(".b").dblclick(function () {
    var id = $(this).attr("id");
    window.location.href = "http://127.0.0.1:8006/part_bay2/"+id
});

// $("button：last").on('click', function() {
//         //找到所有p元素中，包含了3的元素
//         //这个也是一个过滤器的处理
//         $("this").remove()
//     })
//     $('#remove').prev('button').remove()
// $("#remove").on('click',function () {
//     $(".content:first").remove()
// })
//
//     $("#aa").click(function () {
// //你要做什么
//         $("#a").hide();//隐藏按钮
//     })
// })
//
