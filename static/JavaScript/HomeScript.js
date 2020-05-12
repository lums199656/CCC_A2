//python3 manage.py runserver 8001 --insecure
function displayName(){
    if(document.getElementById("hidename").style.display=="none")
        document.getElementById("hidename").style.display="block"
    else
        document.getElementById("hidename").style.display="none"

}

$.ajax({
    url:'get_aurin/',
    methods:'get',
    async:true,
    data:{},
    success: (data) =>{
        console.log(2);
        hello = data
    }
})
console.log(3)
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


