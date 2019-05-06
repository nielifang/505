/**
 * Created by asus on 2019/4/2.
 */

// ves = document.getElementById("ui-Resizable-1");
// var vesLen = ves.style.width;
// $("#confirm").click(function () {
//     // alert(vesLen);
//     // var vesLen = $("#ui-Resizable-1").css(width);
//
//     var vesLen = ves.style.width;
//     $.ajax({
//         url: "/bay_structure/",
//         type: "post",
//         data: {
//             vesLen: vesLen,
//             post_data: JSON.stringify(POST_DATA)
//         },
//         dataType: "json",
//         success: function () {
//             console.log(666)
//         }
//     })
//
// });


$("#confirm").click(function () {
            var ves = document.getElementById("ui-Resizable-1");
            var ves = ves.style.width;
            vesLen = ves.substring(0, ves.length - 2);
            vesLen =vesLen.toString();

            // var top = document.getElementsByClassName("top");
            var engRom = $(".top").css("marginLeft");
            engRomMar = engRom.substring(0,engRom.length - 2);
            engRomMar = parseInt(engRomMar);
            // var ves = $(".panel1");
            var vesMar = $(".panel1").css("marginLeft");
            vesMar  = vesMar.substring(0,vesMar.length - 2);
            var engRomPos = engRomMar - vesMar;
            engRomPos=engRomPos.toString();

            // vesLen = parseInt(vesLen);
            alert(engRomPos);
            $.ajax({
                url: "/createVes/",
                type: "POST",
                async: false,
                date: {
                    vesLen: vesLen,
                    engRomPos:engRomPos
                },

                success: function (data) {
                    // console.log(666);
                window.location.href="http://127.0.0.1:8006/createVes/"
                }
            })
        });