// function page(){
//    $.ajax({
//        url: "go_to_chart/",
//        type:"post",
//        async: false,
//        success: function(result){
//            alert(result);
//        }
//    })
// }

var sentiment = 5;
console.log(1)
$.ajax({
    url:'../get_sentiments/',
    methods:'get',
    async:false,
    data:{},
    success: (data) =>{
        console.log(2);
        sentiment = data;
    }
})

var Happydata = JSON.parse(sentiment)

// console.log(3)


function initMap() {
    map = new google.maps.Map(document.getElementById('startMap'), {
        center: {lat: -37.8, lng: 144.9},
        zoom: 12,
        styles: mapStyle2,
        mapTypeControl: false,

    });
    map.data.loadGeoJson('/static/JSON/vic_geo.json');
    map.data.setStyle((feature) => {
        let name = feature.getProperty('vic_loca_2')
        let total = 0

        // if (aurin[`${name}`]){
        //     if (aurin[`${name}`][`${'econ'}`][`${'unemployment_num'}`]){
        //         total = aurin[`${name}`][`${'econ'}`][`${'unemployment_num'}`]
        //     }
        // }
        if (Happydata[`${name}`]){
            if (Happydata[`${name}`][`${'1_percent'}`]){
                total= Happydata[`${name}`][`${'1_percent'}`]
            }
        }

        let color = '#0098ff08'
        if (total>0)
            color='#7585e3'
        if (total>0.3)
            color='#9e68d1'
        if (total>0.6)
            color='#c241b8'
        if (total>0.9)
            color='#e10071'





        return {
            fillColor: color,
            fillOpacity: 0.6,
            strokeWeight: 1,
            strokeColor:"white"
        }
    })




    var infowindow = new google.maps.InfoWindow;
    map.data.addListener('click', function(event) {
        // prepare data

        let name = event.feature.getProperty('vic_loca_2')
        let unemploy = 0

        if (Happydata[`${name}`]){
            if (Happydata[`${name}`][`${'1_percent'}`]){
                happyScore= Happydata[`${name}`][`${'1_percent'}`]
                subname = name
            }
        }

        infowindow.setContent('<h5 class="font-weight-bold">'+ name +'</h5>'+'<p>Positive Score:'+happyScore+'</p>'+'<canvas id="myChart" width="40" height="40"></canvas>'+
            '<button class="btn" onclick="happyTag(subname)">Positive</button>'+
            '<style>' + 'h5{font-size:15px; text-align: center}'+
            '.btn{background-color: grey; color: white; height:30px;  width:100px; text-align: center; font-size: 15px; align-items: left;}'
            + '</style>')




        infowindow.setPosition(event.latLng)

        infowindow.open(map)
        console.log(document.getElementById('chart'))
    })


    // map.data.addListener('click', function(event) {
    //     test();
    // });


    map.data.addListener('click', function(event) {
        event.feature.setProperty('isColorful', true);
    });

// When the user hovers, tempt them to click by outlining the letters.
// Call revertStyle() to remove all overrides. This will use the style rules
// defined in the function passed to setStyle()
    map.data.addListener('mouseover', function(event) {
        map.data.revertStyle();
        map.data.overrideStyle(event.feature, {

            fillOpacity: 0,
            // fillColor: '#6e502b',
            strokeWeight: 1,
            strokeColor: '#bf935a',
        });
    });

    map.data.addListener('mouseout', function(event) {
        map.data.revertStyle();
    });


}

function happyTag(name) {

    console.log(document.getElementById('chart'))
    var ctx = document.getElementById('myChart');
    // var chartdata = {
    //     datasets: [{
    //         data: [10, 20, 30]
    //     }]
    // }
    ctx.height = 100;
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Happydata[`${name}`][`${"1_hastags"}`].slice(0,5),
            datasets: [{
                // label: "Population (millions)",
                backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                data: Happydata[`${name}`][`${"1_hastags_num"}`].slice(0,5),
            }]
        },
    });
}


// var can = document.createElement('canvas')
// can.id = "myChart"
// document.body.appendChild(can);





function incomeMap(type) {
    map = new google.maps.Map(document.getElementById('startMap'), {
        center: {lat: -37.8, lng: 144.9},
        zoom: 12,
        styles: mapStyle2,
        mapTypeControl: false,

    });
    map.data.loadGeoJson('/static/JSON/vic_geo.json');
    map.data.setStyle((feature) => {
        let name = feature.getProperty('vic_loca_2')
        let total = 0

        // if (aurin[`${name}`]){
        //     if (aurin[`${name}`][`${'econ'}`][`${'unemployment_num'}`]){
        //         total = aurin[`${name}`][`${'econ'}`][`${'unemployment_num'}`]
        //     }
        // }
        if (aurin[`${name}`]){
            if (aurin[`${name}`][`${type[0]}`]){
                total= aurin[`${name}`][`${type[0]}`]
            }
        }
// # https://www.w3schools.com/colors/colors_picker.asp
//         let color = '#ecc6c6'
//         if (total>0)
//             color='#d98c8c'
//         if (total>20)
//             color='#c65353'
//         if (total>40)
//             color='#993333'
//         if (total>60)
//             color='#602020'
//         if (total>80)
//             color='#391313'

        // let color = '#d11c9ad1'
        // if (total>0)
        //     color='#ae59c6'
        // if (total>30)
        //     color='#7e88df'
        // if (total>60)
        //     color='#009fff'
        // if (total>90)
        //     color='#0062ff'

        // let color = '#0098ff08'
        let color = '#0098ff'
        if (total>0)
            color='#7585e3'
        if (total>30)
            color='#9e68d1'
        if (total>60)
            color='#c241b8'
        if (total>90)
            color='#e10071'


        //https://www.w3schools.com/colors/colors_picker.asp



        return {
            fillColor: color,
            fillOpacity: 0.6,
            strokeWeight: 1,
            strokeColor:"white"
        }
    })




    var infowindow = new google.maps.InfoWindow;
    map.data.addListener('click', function(event) {
        // prepare data

        let name = event.feature.getProperty('vic_loca_2')
        let unemploy = 0

        if (aurin[`${name}`]){
            if (aurin[`${name}`][`${type[0]}`]){
                unemploy= aurin[`${name}`][`${type[0]}`]
            }
        }

        infowindow.setContent('<h5 class="font-weight-bold">'+ name +'</h5>'+'<p>unemployed number:'+unemploy+'</p>'+'<canvas id="myChart" width="40" height="40"></canvas>'+
            // '<button class="btn" onclick="test()">unemployee</button>'+
            '<style>' + 'h5{font-size:15px; text-align: center}'+
            '.btn{background-color: grey; color: white; height:30px;  width:100px; text-align: center; font-size: 15px; align-items: left;}'
            + '</style>')




        infowindow.setPosition(event.latLng)

        infowindow.open(map)
        console.log(document.getElementById('chart'))
    })


    map.data.addListener('click', function(event) {
        test();
    });


    map.data.addListener('click', function(event) {
        event.feature.setProperty('isColorful', true);
    });

// When the user hovers, tempt them to click by outlining the letters.
// Call revertStyle() to remove all overrides. This will use the style rules
// defined in the function passed to setStyle()
    map.data.addListener('mouseover', function(event) {
        map.data.revertStyle();
        map.data.overrideStyle(event.feature, {

            fillOpacity: 0,
            // fillColor: '#6e502b',
            strokeWeight: 1,
            strokeColor: '#bf935a',
        });
    });

    map.data.addListener('mouseout', function(event) {
        map.data.revertStyle();
    });


}






