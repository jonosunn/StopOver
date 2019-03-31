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
  mapLink.textContent = '';

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
    mapLink.textContent = `Longitude: ${longitude}°, Latitude: ${latitude}°`;
// setting the longitute and latitude into cookies to be accessed in views.py
    setCookie("longitude",position.coords.longitude);
    setCookie("latitude",position.coords.latitude);

    // loading marker for the users Location
    var geojson_user = {
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
    geojson_user.features.forEach(function(marker) {
      // create a HTML element for each feature
      var el = document.createElement('div');
      el.className = 'marker';
      // make a marker for each feature and add to the map
      new mapboxgl.Marker(el)
        .setLngLat(marker.geometry.coordinates)
        .addTo(map);
    });


    // add car markers to map
    geojson_carlist.features.forEach(function(marker) {
      // create a HTML element for each feature
      var el = document.createElement('div');
      el.className = 'marker';
      // make a marker for each feature and add to the map
      new mapboxgl.Marker(el)
        .setLngLat(marker.geometry.coordinates)
        .addTo(map);
    });


    // loading marker for the car Location
        var geojson_carlist = {
          type: 'FeatureCollection',
          features: [
            (% for car in cars %)
            {
            type: 'Feature',
            geometry: {
              type: 'Point',
              coordinates: [{{ car.longitude }}, {{ car.latitude }}]
            },
            properties: {
              title: 'Mapbox',
              description: 'Car Locations'
            }
          },
        {% endfor %}
        ]
        };
  }

  function error() {
    status.textContent = 'Unable to retrieve your location';
  }

  if (!navigator.geolocation) {
    status.textContent = 'Geolocation is not supported by your browser';
  } else {
    status.textContent = 'Locating…';
    navigator.geolocation.getCurrentPosition(success, error);
  }
}
