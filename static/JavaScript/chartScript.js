data = {
    datasets: [{
        label: '# of Votes',
        data: [10, 20, 30],
        backgroundColor: [
            '#ecc6c6',
            '#d98c8c',
            '#bf4040',
        ],
        borderColor: [
            '#ecc6c6',
            '#d98c8c',
            '#bf4040',
        ],
        borderWidth: 1
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: [
        'Red',
        'Yellow',
        'Blue'
    ]
};

var i;
var list1 = document.getElementsByClassName("flex-cell flex-cell-l");
console.log(list1.length);
for (i = 0; i < list1.length; i++) {
    console.log(list1[i]);
    console.log(list1[i].style.width);
}

var myPie =  document.getElementById("piechart").getContext("2d");
var myPieChart = new Chart(myPie, {
    type: "pie",
    data: data,
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

var myBar =  document.getElementById("barchart").getContext("2d");
var myPieChart = new Chart(myBar, {
    type: "bar",
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

var myLine =  document.getElementById("linechart").getContext("2d");
var myPieChart = new Chart(myLine, {
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
});

// var chart = document.getElementById("chart").getContext("2d");

function showPie(){
    document.getElementById("pieIcon").src = "../static/image/color-pie-chart.svg";
    document.getElementById("lineIcon").src = "../static/image/line-chart.svg";
    document.getElementById("barIcon").src = "../static/image/bar-chart.svg";
    document.getElementById("chart").getContext("2d").clearRect(0, 0, chart.width, chart.height);

    var myPieChart = new Chart(chart, {
        type: 'pie',
        data: data
    });
}

function showLine(){
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

function  showBar() {
    document.getElementById("pieIcon").src = "../static/image/graph.svg";
    document.getElementById("lineIcon").src = "../static/image/line-chart.svg";
    document.getElementById("barIcon").src = "../static/image/color-bar.svg";
    document.getElementById("chart").getContext("2d").clearRect(0, 0, chart.width, chart.height);

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

function openNav() {
    document.getElementById("mySidenav").style.width = "200px";
    document.getElementById("container").style.marginLeft = "200px";
    document.getElementById("myTopnav").style.marginLeft = "200px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("container").style.marginLeft= "0";
    document.getElementById("myTopnav").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
}