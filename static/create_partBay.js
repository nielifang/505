/**
 * Created by asus on 2019/3/28.
 */
// $(document).ready(function getTable (tableid) {
// var element = $("#tb"); // global variable

$(document).ready(function () {


    var element = $("#table"); // global variable
    var getCanvas; // global variable
    // function GetInfoFromTable(tableid) {
    //
    //     var tableobj = document.getElementById(tableid);
    //
    //     for (var index = 0; index < tableobj.rows.length; index++) {
    //         for (var j = 0; j < tableobj.rows[index].cells.length; j++) {
    //             // if (tableobj.rows[index].cells[j].hasOwnProperty(hasClass("active")))
    //             element += tableobj.rows[index].cells[j].innerHTML;
    //             element += " "
    //         }
    //         element += "\n";
    //     }
    //     return element;
    // }
    //
    // GetInfoFromTable('table');

    $("#btn-Preview-Image").on('click', function () {

        html2canvas(element, {
            onrendered: function (canvas) {
                $("#previewImage").append(canvas);
                getCanvas = canvas;
            }
        });
    });

    $("#btn-Convert-Html2Image").on('click', function () {
        var imgageData = getCanvas.toDataURL("image/png");
        // Now browser starts downloading it instead of just showing it
        var newData = imgageData.replace(/^data:image\/png/, "data:application/octet-stream");
        $("#btn-Convert-Html2Image").attr("download", "your_pic_name.png").attr("href", newData);
    });

});

// var element = new Array();
// function GetInfoFromTable(table) {
//
//     var tableobj = document.getElementById(table);
//
//     for (var index = 0; index < tableobj.rows.length; index++) {
//         for (var j = 0; j < tableobj.rows[index].cells.length; j++) {
//             // if (tableobj.rows[index].cells[j].hasOwnProperty(hasClass("active")))
//             element += tableobj.rows[index].cells[j].innerHTML;
//
//
//             var getCanvas; // global variable
//
//             $("#btn-Preview-Image").on('click', function () {
//                 html2canvas(element, {
//                     onrendered: function (canvas) {
//                         $("#previewImage").append(canvas);
//                         getCanvas = canvas;
//                     }
//                 });
//             });
//
//
//             console.log(element);
//             // element += " ";
//         }
//         // element += "\n";
//     }
//     return element;
// }
//
//
// new Promise(function (resolve, reject) {
//     reject('该prormise已被拒绝');
// }).catch(function (reason) {
//     console.log('catch:', reason);
// });
// $("#btn-Convert-Html2Image").on('click', function () {
//     var imgageData = getCanvas.toDataURL("image/png");
//     // Now browser starts downloading it instead of just showing it
//     var newData = imgageData.replace(/^data:image\/png/, "data:application/octet-stream");
//     $("#btn-Convert-Html2Image").attr("download", "your_pic_name.png").attr("href", newData);
// });

// };
// });


// GetInfoFromTable('table');