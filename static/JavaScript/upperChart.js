// {#Author: Kailun Huang#}
// {#ID: 828808#}
// {#Team 32#}

var suburb = [];
var type1 = [];
var type2 = [];
var color = [];
var myBarChart;
var recieve_result = {}

$.ajax({
    url:'../get_sentiments_count/',
    methods:'get',
    headers:{ 'X-API-KEY': 'de9dECvvcd48CfEdvfDrgbtD'},
    async:false,
    data:{"year":""},
    success: (data) =>{
        console.log(2);
        recieve_result = data;
    }
})

var suburb_sentiments_count = JSON.parse(recieve_result)
console.log(suburb_sentiments_count)
function callServer(callback, num, statistics1, statistics2){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(this.responseText, num, statistics1, statistics2);
        };
    }
    xmlhttp.open("GET", "../static/JSON/new_submit.json", true);
    xmlhttp.send();
}

function  showBar(data, yID1, yID2) {
    if (myBarChart){
        myBarChart.destroy();
    }
    var chart = document.getElementById("barchart").getContext("2d");
    myBarChart = new Chart(chart, {
        type: 'bar',
        data: data
    });

}

function extract_unemployment_data_Bar(responseText, num, statistics1, statistics2){
    suburb = []
    type1 = [];
    type2 = [];
    var myArr = JSON.parse(responseText);
    var item;
    // console.log(statistics1);
    // console.log(statistics2);
    for (item in myArr){
        // suburb.push(item);
        // // console.log(statistics1);
        // // console.log(statistics2);
        // type1.push(myArr[item][statistics1]);
        // // console.log(myArr[item][statistics1]);
        // // console.log(myArr[item]["total_unemployed"]);
        // type2.push(myArr[item][statistics2]);
        if (item in suburb_sentiments_count){
            type1.push(myArr[item][statistics1])
            if (suburb_sentiments_count[item][statistics2] < 10){
                type2.push(suburb_sentiments_count[item][statistics2]*100)
            }else if(suburb_sentiments_count[item][statistics2] < 50){
                type2.push(suburb_sentiments_count[item][statistics2]*20)
            }else if(suburb_sentiments_count[item][statistics2] <100){
                type2.push(suburb_sentiments_count[item][statistics2]*10)
            }

            suburb.push(item)
        }
    }
    console.log(type1);
    console.log(type2);
    // var final_stats = {"suburb": suburb, statistics1:type1, statistics2: type2 };
    var data = {
        datasets: [{
            label: statistics1,
            data: type1,
            backgroundColor: "#6a4b86",
            borderColor: "#6a4b86",
            borderWidth: 1,
            // yAxisID: statistics1
        },{
            label: statistics2,
            data: type2,
            backgroundColor: "#6699ff",
            borderColor: "#6699ff",
            borderWidth: 1,
            // yAxisID: statistics2
        }],
        labels: suburb
    }

    showBar(data, statistics1, statistics2);
}

function changeType(){
    var statistics1 = document.getElementById("Type1").value;
    var statistics2 = document.getElementById("Type2").value;
    // console.log(statistics1);
    // console.log(statistics2);
    var chart = document.getElementById("barchart").getContext("2d");
    callServer(extract_unemployment_data_Bar, num, statistics1, statistics2);
}


var x = {"a":1 ,"b":2};
var y = {"a":5, "c":3};

var z = [x,y]
var hehe = {}
function addTwoObjects(object){
    var i;
    var j;
    for (i in object){
        for (j in object[i]){
            console.log(object[i][j]);
            if (j in hehe){
                hehe[j]+=object[i][j];
            }else{
                hehe[j]=object[i][j];
            }
        }
    }
}

var list = 	{"taxavoidance": 5, "wagetheft": 1, "lnp": 1, "gippsnews": 16, "covid": 4, "testing": 2, "genderequality": 5, "deferit": 1};
keysSorted = Object.keys(list).sort(function(a,b){return list[a]-list[b]})
console.log(keysSorted);
let entries = Object.entries(list);
console.log(Object.values(list));
let sorted = entries.sort((a, b) => b[1] - a[1]);
console.log(sorted.slice(0,2));

callServer(extract_unemployment_data_Bar, 1, "total_unemployed", "1");