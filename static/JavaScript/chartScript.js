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

function extract_unempolyment_data_Bar(responseText, num){
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

// function extract_unempolyment_data_Bar(responseText){
//     var myArr = JSON.parse(responseText);
//     var item;
//     for (item in myArr){
//         suburb.push(item);
//         imcome_support_percentage.push(myArr[item]["imcome_support_percentage"]);
//     }
//     var final_stats = {"suburb": suburb,"imcome_support_percentage":imcome_support_percentage };
//     var data = {
//         datasets: [{
//             label: "imcome_support_percentage",
//             data: final_stats["imcome_support_percentage"],
//             backgroundColor: "#ecc6c6",
//             borderColor: "#ecc6c6",
//             borderWidth: 1
//         }],
//         labels: final_stats["suburb"].splice((num-1)*10, num*10)
//     }
// }

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

var i;
var list1 = document.getElementsByClassName("flex-cell flex-cell-l");
console.log(list1.length);
for (i = 0; i < list1.length; i++) {
    console.log(list1[i]);
    console.log(list1[i].style.width);
}

var myPie =  document.getElementById("pie chart").getContext("2d");
var myPieChart = new Chart(myPie, {
    type: "pie",
    data: data1,
    options: {
        layout: {
            padding: {
                left: 0,
                right: 0,
                top: 0,
                bottom: 0
            }
        }
    }
});

var myLine =  document.getElementById("linechart").getContext("2d");
var myPieChart = new Chart(myLine, {
    type: "line",
    data: data1,
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

// var chart = document.getElementById("chart").getContext("2d");

function showPie(data){
    var chart = document.getElementById("piechart").getContext("2d");

    var myPieChart = new Chart(chart, {
        type: 'pie',
        data: data
    });
}

function showLine(data){
    document.getElementById("pieIcon").src = "../static/image/graph.svg";
    document.getElementById("lineIcon").src = "../static/image/color-line.svg";
    document.getElementById("barIcon").src = "../static/image/bar-chart.svg";
    document.getElementById("chart").getContext("2d").clearRect(0, 0, chart.width, chart.height);

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

callServer(extract_unempolyment_data_Bar, 1);