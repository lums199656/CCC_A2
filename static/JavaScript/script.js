
function initMap() {
     // this.visible=true
     var map = new google.maps.Map(document.getElementById('startMap'), {
        center: {lat: -37.8, lng: 144.9},
        zoom: 12,
         mapTypeControl: false,
         styles: mapStyle,
         mapTypeId: google.maps.MapTypeId.ROADMAP,
         disableDefaultUI: true

    });


}


///test
var hello;
console.log(1)
$.ajax({
    url:'get_aurin/',
    methods:'get',
    async: true,
    data:{},

    success:(data)=>{
        console.log(2);
        hello = data
    }

})
console.log(3)
function readValue(){

    console.log(hello);
}



function incomeMap() {
    map = new google.maps.Map(document.getElementById('startMap'), {
        center: {lat: -37.8, lng: 144.9},
        zoom: 12,
        styles: mapStyle,
        mapTypeControl: false,

    });
    map.data.loadGeoJson('/static/JSON/vic_geo.json');
    map.data.setStyle((feature) => {
        let name = feature.getProperty('vic_loca_2')
        let total = 0

        if (aurin[`${name}`]){
            if (aurin[`${name}`][`${'econ'}`][`${'unemployment_num'}`]){
                total = aurin[`${name}`][`${'econ'}`][`${'unemployment_num'}`]
            }
        }

        let color = '#bf935a'
        // if (name =='MELBOURNE')
        //     color='red'
        if (total>100)
            color='red'
        if (total>1000)
            color='purple'


        return {
            fillColor: color,
            fillOpacity: 0.5,
            strokeWeight: 2,
            strokeColor:'#b88547'
        }
    })

    var infowindow = new google.maps.InfoWindow;

    map.data.addListener('click', (event) => {
        // prepare data
        let name = event.feature.getProperty('vic_loca_2')
        infowindow.setContent(name)
        infowindow.setPosition(event.latLng)
        infowindow.open(map)
    })

    // map.data.addListener('mouseover', function(event) {
    //     document.getElementById('info-box').textContent =
    //         event.feature.getProperty('vic_loca_2');
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

            fillOpacity: 0.9,
            fillColor: '#6e502b',
            strokeWeight: 1,
            strokeColor: '#bf935a',
        });
    });

    map.data.addListener('mouseout', function(event) {
        map.data.revertStyle();
    });


}



