// Fucntion to find current location (geolocation)
function geoFindMe() {

  // document.querySelector('#find-me').addEventListener('click', geoFindMe);

  // Mapbox script to display map, also uses to edit the center and zoom etc
  mapboxgl.accessToken = 'pk.eyJ1Ijoic3RvcG92ZXJhZG1pbiIsImEiOiJjanRtcHY3YXozeW10NGJvM3c2dWlxZ2xvIn0.1WlrGXizCLdOrV5TXPTc0A';
  //set bounds of melbourne
  //format: [south, west], [north, east]
  //follow mapbox's coordinates system
  var bounds = [
   	 [144.70345,-37.91802],
   	 [145.22873,-37.64668]
  ];
    var map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [144.97, -37.81],
      zoom: 12,
      bearing: 0,
      maxBounds: bounds
  });
    


  const status = document.querySelector('#status');
  const mapLink = document.querySelector('#map-link');


  mapLink.href = '';
 // mapLink.textContent = '';

  

// creating a fucntion to set a value into cookie expires in 30s
  function setCookie(name, value) {
    var today = new Date();
    var expiry = new Date(today.getTime() + 30 * 1000);
    document.cookie=name + "=" + escape(value) + "; path=/; expires=" + expiry.toGMTString();
  }

  function success(position) {
    const latitude  = position.coords.latitude;
    const longitude = position.coords.longitude;

    status.textContent = '';
    mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
//    mapLink.textContent = `Longitude: ${longitude}°, Latitude: ${latitude}°`;
// setting the longitute and latitude into cookies to be accessed in views.py
    setCookie("longitude",position.coords.longitude);
    setCookie("latitude",position.coords.latitude);
    
   
    // loading marker for the users Location
    var geojson = {
      type: 'FeatureCollection',
      features: [{
        type: 'Feature',
        geometry: {
          type: 'Point',
          coordinates: [longitude, latitude]
        },
        properties: {
          title: 'Mapbox',
          description: 'Current Users Location'
        }
      }]
    };

    // add markers to map
    geojson.features.forEach(function(marker) {
      // create a HTML element for each feature
      var el = document.createElement('div');
      el.className = 'marker';
      // make a marker for each feature and add to the map
      new mapboxgl.Marker(el)
        .setLngLat(marker.geometry.coordinates)
        .addTo(map);
    });
  }

  function error() {
    status.textContent = 'Unable to retrieve your location';
  }

  if (!navigator.geolocation) {
    status.textContent = 'Geolocation is not supported by your browser';
  } 
  else {
    status.textContent = 'Locating…';
    navigator.geolocation.getCurrentPosition(success, error);
  }	
}


	
function getSpecificCookie(cookieName, valueOnly) {
    //Get original cookie string
    var oCookieArray = document.cookie.split(';'),
        fc,
        cnRE = new RegExp(cookieName + '\=');
    //Loop through cookies
    for (var c = 0; c < oCookieArray.length; c++) {

        //If found save to variable and end loop
        if (cnRE.test(oCookieArray[c])) {
            fc = oCookieArray[c].trim();
            if (valueOnly) {
                fc = fc.replace(cookieName +'=', '');
            }
            break;
        }

    }
    return fc;
}
var i = 0;

function getDistanceFromLatLonInKm(lon1, lat1, lon2, lat2) {
	  var R = 6371; // Radius of the earth in km
	  var dLat = deg2rad(lat2-lat1);  // deg2rad below
	  var dLon = deg2rad(lon2-lon1); 
	  var a = 
	    Math.sin(dLat/2) * Math.sin(dLat/2) +
	    Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
	    Math.sin(dLon/2) * Math.sin(dLon/2)
	    ; 
	  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
	  var d = R * c; // Distance in km
	  
	  return d.toFixed(2);
	}

function deg2rad(deg) {
return deg * (Math.PI/180)
}


