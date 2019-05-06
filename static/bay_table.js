/**
 * 合并单元格(如果结束行传0代表合并所有行)
//  * @param table1    表格的ID
//  * @param startCol  起始列
//  * @param endCol    结束列
//  * @param row   合并的行号，对第几列进行合并(从0开始)。第一行从0开始
//  */
// function mergeCell(table1, startCol, endCol, row) {
//     var tb = document.getElementById(table1);
//     if (!tb || !tb.cols || tb.cols.length <= 0) {
//         return;
//     }
//     if (row >= tb.cols[0].cells.length || (startCol >= endCol && endCol != 0)) {
//         return;
//     }
//     if (endCol == 0) {
//         endCol = tb.cols.length - 1;
//     }
//     for (var i = startCol; i < endCol; i++) {
//         if (tb.cols[startCol].cells[row].innerHTML == tb.cols[i + 1].cells[row].innerHTML) { //如果相等就合并单元格,合并之后跳过下一行
//             tb.cols[i + 1].removeChild(tb.cols[i + 1].cells[row]);
//             tb.cols[startCol].cells[row].colSpan = (tb.cols[startCol].cells[row].colSpan) + 1;
//         } else {
//             mergeCell(table1, i + 1, endCol, row);
//             break;
//         }
//     }
// }
// mergeCell('mytable',0,2,1);


/**
             * 合并单元格(如果结束行传0代表合并所有行)
             * @param table1    表格的ID
             * @param startRow  起始行
             * @param endRow    结束行
             * @param col   合并的列号，对第几列进行合并(从0开始)。第一行从0开始
             */
//             function mergeCell(table1, startRow, endRow, col) {
//                 var tb = document.getElementById(table1);
//                 if(!tb || !tb.cols || tb.cols.length <= 0) {
//                     return;
//                 }
//                 if(col >= tb.cols[0].cells.length || (startRow >= endRow && endRow != 0)) {
//                     return;
//                 }
//                 if(endRow == 0) {
//                     endRow = tb.cols.length - 1;
//                 }
//                 for(var i = startRow; i < endRow; i++) {
//                     if(tb.cols[startRow].cells[col].innerHTML == tb.cols[i + 1].cells[col].innerHTML) { //如果相等就合并单元格,合并之后跳过下一行
//                         tb.cols[i + 1].removeChild(tb.cols[i + 1].cells[col]);
//                         tb.cols[startRow].cells[col].colSpan = (tb.cols[startRow].cells[col].colSpan) + 1;
//                     } else {
//                         mergeCell(table1, i + 1, endRow, col);
//                         break;
//                     }
//                 }
//             }
//
// mergeCell('mytable',0,2,2);
//
// function mc(table1, startRow, endRow, col) {
//                 var tb = document.getElementById(table1);
//                 let tableCellLength = tb.rows[0].cells.length;
//                 for (let i = startRow; i < endRow; i++) {
//                     if (tb.rows[startRow].cells[col].innerHTML == tb.rows[i + 1].cells[col].innerHTML) {
//                         //合并最后一列相同的行
//                         tb.rows[i + 1].removeChild(tb.rows[i + 1].cells[tableCellLength-1]);
//                         tb.rows[startRow].cells[tableCellLength-1].rowSpan = (tb.rows[startRow].cells[tableCellLength-1].rowSpan | 0) + 1;
//                         //合并第col列相同的行
//                         tb.rows[i + 1].removeChild(tb.rows[i + 1].cells[col]);
//                         tb.rows[startRow].cells[col].rowSpan = (tb.rows[startRow].cells[col].rowSpan | 0) + 1;
//                     }else{
//                         mc(table1, i + 1, endRow, col)
//                     }
//                 }
//             }