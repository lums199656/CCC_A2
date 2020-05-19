var suburb = [];
var type1 = [];
var type2 = [];
var color = [];
var myBarChart;

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

function  showBar(data) {
    if (myBarChart){
        myBarChart.destroy();
    }
    var chart = document.getElementById("barchart").getContext("2d");
    myBarChart = new Chart(chart, {
        type: 'bar',
        data: data,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
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
        suburb.push(item);
        // console.log(statistics1);
        // console.log(statistics2);
        type1.push(myArr[item][statistics1]);
        // console.log(myArr[item][statistics1]);
        // console.log(myArr[item]["total_unemployed"]);
        type2.push(myArr[item][statistics2]);
    }
    console.log(type1);
    console.log(type2);
    // var final_stats = {"suburb": suburb, statistics1:type1, statistics2: type2 };
    var data = {
        datasets: [{
            label: statistics1,
            data: type1.slice((num-1)*10, num*10),
            backgroundColor: "#ecc6c6",
            borderColor: "#ecc6c6",
            borderWidth: 1
        },{
            label: statistics2,
            data: type2.slice((num-1)*10, num*10),
            backgroundColor: "#ff4d4d",
            borderColor: "#ff4d4d",
            borderWidth: 1
        }],
        labels: suburb.slice((num-1)*10, num*10)
    }

    showBar(data);
}

function changeType(){
    var statistics1 = document.getElementById("Type1").value;
    var statistics2 = document.getElementById("Type2").value;
    var num = document.getElementById("City_Group").value;
    // console.log(statistics1);
    // console.log(statistics2);
    var chart = document.getElementById("barchart").getContext("2d");
    callServer(extract_unemployment_data_Bar, num, statistics1, statistics2);
    document.getElementById("Cities").innerHTML = suburb.slice((num-1)*10, num*10);
}

callServer(extract_unemployment_data_Bar, 1, "total_unemployed", "non-school_qualification");