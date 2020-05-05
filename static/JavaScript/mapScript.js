

function initMap() {
    // this.visible=true
    var map = new google.maps.Map(document.getElementById('startMap'), {
        center: {lat: -37.8, lng: 144.9},
        zoom: 12,
        mapTypeControl: false,
        styles: mapStyle2,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true

    });


}


var can = document.createElement('canvas')
can.id = "myChart"
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
        let color = '#ecc6c6'
        if (total>0)
            color='#d98c8c'
        if (total>20)
            color='#c65353'
        if (total>40)
            color='#993333'
        if (total>60)
            color='#602020'
        if (total>80)
            color='#391313'

        //https://www.w3schools.com/colors/colors_picker.asp
        //#0033cc
        // let color = '#ccd9ff'
        // if (total>0)
        //     color='#809fff'
        // if (total>20)
        //     color='#3366ff'
        // if (total>40)
        //     color='#0039e6'
        // if (total>60)
        //     color='#002699'
        // if (total>80)
        //     color='#001a66'


        return {
            fillColor: color,
            fillOpacity: 0.7,
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

            fillOpacity: 1,
            // fillColor: '#6e502b',
            strokeWeight: 1,
            strokeColor: '#bf935a',
        });
    });

    map.data.addListener('mouseout', function(event) {
        map.data.revertStyle();
    });


}

function test(){

    console.log(document.getElementById('chart'))
    var ctx = document.getElementById('myChart');
    var chartdata = {
        datasets: [{
            data: [10, 20, 30]
        }]
    }
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: chartdata,
        backgroundColor: [
            '#999999',
            '#808080',
            '#454545',

        ],
        borderWidth: 1
    });
}




