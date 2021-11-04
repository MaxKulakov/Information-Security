const fs = require('fs');
const path = require('path');


// var remote = require('remote');
// var dialog = remote.require('electron').dialog;
//
// var path = dialog.showOpenDialog({
//     properties: ['openDirectory']
// });

// var remote = require('electron').remote;
// var fs = remote.require('fs');
// // var electronDialog = remote.dialog;

// var pathToFolder = document.getElementById("myFile").files[0].path;

// fs.readdir('./src', (err, data) => {

// var fileList = '';
// fs.readdir('./fileDirectory/', (err, data) => {
//   // console.log(data);
//   data.forEach(file => {
//     console.log(file);
//     fileList += `${file} <br/> `
//   });
//   document.getElementsByClassName("results")[0].innerHTML = `${fileList} <br/> `;
// })

// Рекурсивная функция для получения всех файлов из переданной директории
var getFiles = function (dir, files_){
  files_ = files_ || [];
    var files = fs.readdirSync(dir);
    for (var i in files){
        var name = dir + '/' + files[i];
        if (fs.statSync(name).isDirectory()){
            getFiles(name, files_);
        } else {
            files_.push(name);
        }
    }
    return files_;
};

console.log(getFiles('./fileDirectory'));


//
// document.getElementsByClassName("results")[0].innerHTML = `[9, 0, 0, 1, 1, 1, 2, 2, 3, 3]: ${arr1} <br/>
//                                                                 [9, 2, 7, 5, 5, 5, 6, 6, 9, 0]: ${arr2} <br/>
//                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9, -11]: ${arr3} <br/>
//                                                                 []: ${arr4} <br/>
//                                                                 'aw93fha=': ${str1}`;


// document.querySelector('button').addEventListener('click', function() {
//   let file = document.getElementById('file').files[0];
//   let reader = new FileReader();
//   reader.readAsText(file);
//   reader.onload = function() {
//     console.log(reader.result);
//   }
//   reader.onerror = function() {
//     console.log(reader.error);
//   }
// })
