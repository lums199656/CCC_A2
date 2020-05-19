//python3 manage.py runserver 8001 --insecure
function displayName(){
    if(document.getElementById("hidename").style.display=="none")
        document.getElementById("hidename").style.display="block"
    else
        document.getElementById("hidename").style.display="none"

}

// var sentiment = 5;
// console.log(1)
// $.ajax({
//     url:'../get_sentiments/',
//     methods:'get',
//     async:false,
//     data:{},
//     success: (data) =>{
//         console.log(2);
//         sentiment = data;
//     }
// })
//
// var Happydata = JSON.parse(sentiment)
//
// $.ajax({
//     url:'get_aurin/',
//     methods:'get',
//     async:true,
//     data:{},
//     success: (data) =>{
//
//         hello = data
//     }
// })

//
// function page(){
//     $.ajax({
//         url: "go_to_chart/",
//         type:"post",
//         async: false,
//         success: function(result){
//             alert(result);
//         }
//     })
// }


