var suburb = [];
var total_unemployed = [];
var unemployed_family = [];
var imcome_support_percentage = []
var color = []

function callServer(callback, num){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(this.responseText, num);
        };
    }
    xmlhttp.open("GET", "../static/JSON/submit.json", true);
    xmlhttp.send();
}

function extract_unemployment_data_Bar(responseText, num){
    var myArr = JSON.parse(responseText);
    var item;
    for (item in myArr){
        suburb.push(item);
        total_unemployed.push(myArr[item]["total_unemployed"]);
        unemployed_family.push(myArr[item]["unemployed_family"]);
    }

    var final_stats = {"suburb": suburb,"total_unemployed":total_unemployed, "unemployed_family": unemployed_family };

    var data = {
        datasets: [{
            label: "total unemployment",
            data: final_stats["total_unemployed"].splice((num-1)*10, num*10),
            backgroundColor: "#ecc6c6",
            borderColor: "#ecc6c6",
            borderWidth: 1
        },{
            label: "unemployment family",
            data: final_stats["unemployed_family"].splice((num-1)*10, num*10),
            backgroundColor: "#ff4d4d",
            borderColor: "#ff4d4d",
            borderWidth: 1
        }],
        labels: final_stats["suburb"].splice((num-1)*10, num*10)
    }

    showBar(data);
}

function extract_unemployment_data_Line(responseText, num){
    var myArr = JSON.parse(responseText);
    var item;
    var dataset = [];
    for (item in myArr){
        suburb.push(item);
        unemployed_family.push(myArr[item]["unemployed_family"]);
        dataset.push({x:item, y:myArr[item]["unemployed_family"]})
    }
    var final_stats = {"suburb": suburb,"unemployed_family":unemployed_family };
    var data = {
        datasets: [{
            label: "unemployment_family",
            data: unemployed_family.splice((num-1)*10, num*10),
            backgroundColor: "#ecc6c6",
            borderColor: "#ecc6c6",
            borderWidth: 1,
            fill: false
        }],
        labels: suburb.splice((num-1)*10, num*10)
    };
    console.log(data);
    showLine(data);
}

data1 = {
    datasets: [{
        label: 'Unemployment situation of suburbs in Melbourne',
        data: [10, 20, 30],

        backgroundColor: '#ecc6c6',

        borderColor: '#ecc6c6',

        borderWidth: 1
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: ["a", "b", "c"]
};


function showPie(data){
    var chart = document.getElementById("piechart").getContext("2d");

    var myPieChart = new Chart(chart, {
        type: 'pie',
        data: data
    });
}

function showLine(data){
    var chart = document.getElementById("linechart").getContext("2d");
    var myLineChart = new Chart(chart, {
        type: "line",
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
    })

}

function  showBar(data) {
    var chart = document.getElementById("barchart").getContext("2d");
    var myBarChart = new Chart(chart, {
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

callServer(extract_unemployment_data_Bar, 1);
callServer(extract_unemployment_data_Line, 1);