var map = new ol.Map({
target: 'map',
layers: [
  new ol.layer.Tile({
    source: new ol.source.OSM()
  })
],
view: new ol.View({
  center: ol.proj.fromLonLat([76.6352,10.0603]),
  zoom: 10
})
});

var container = document.getElementById('popup');
var overlay = new ol.Overlay({
  element: container,
  autoPan: true,
  autoPanAnimation: {
    duration: 250
  }
});
map.addOverlay(overlay);

var cdata = JSON.parse(document.getElementById('data').innerHTML);

Array.prototype.forEach.call(cdata, function(data){

  var marker = new ol.Feature({
    geometry: new ol.geom.Point(
    ol.proj.fromLonLat([data.lon,data.lat])),
    name: [data.vehicleID],
    
  });

  marker.setStyle(new ol.style.Style({
  image: new ol.style.Icon({
     anchor: [1,1],
     anchorXUnits: 'fraction',
     anchorYUnits: 'fraction',
     scale : 100/2000, 
     src: './js/pin.png',
  })
}));


  

  var vectorSource = new ol.source.Vector({
      features: [marker]
    });

  var markerVectorLayer = new ol.layer.Vector({
        source: vectorSource,        
    });
 
  map.addLayer(markerVectorLayer);

});

var hdata = JSON.parse(document.getElementById('Hos_data').innerHTML);

Array.prototype.forEach.call(hdata, function(data){

  var marker = new ol.Feature({
  geometry: new ol.geom.Point(
  ol.proj.fromLonLat([data.lon,data.lat])),
  name: [data.name, data.vehicleID],
  });

  marker.setStyle(new ol.style.Style({
  image: new ol.style.Icon({
     anchor: [1,1],
     anchorXUnits: 'fraction',
     anchorYUnits: 'fraction',
     scale : 100/2000, 
     src: './js/gps.png',
    })
  }));
  var vectorSource = new ol.source.Vector({
      features: [marker]
    });

  var markerVectorLayer = new ol.layer.Vector({
        source: vectorSource,        
    });
 
  map.addLayer(markerVectorLayer);


});

var pdata = JSON.parse(document.getElementById('Pol_data').innerHTML);

Array.prototype.forEach.call(pdata, function(data){

  var marker = new ol.Feature({
  geometry: new ol.geom.Point(
  ol.proj.fromLonLat([data.lon,data.lat])),
  name: [data.name, data.vehicleID],
  });

  marker.setStyle(new ol.style.Style({
  image: new ol.style.Icon({
     anchor: [1,1],
     anchorXUnits: 'fraction',
     anchorYUnits: 'fraction',
     scale : 100/2000, 
     src: './js/badge.png',
    })
  }));
  var vectorSource = new ol.source.Vector({
      features: [marker]
    });

  var markerVectorLayer = new ol.layer.Vector({
        source: vectorSource,        
    });
 
  map.addLayer(markerVectorLayer);


});

var fidata = JSON.parse(document.getElementById('Fir_data').innerHTML);

Array.prototype.forEach.call(fidata, function(data){

  var marker = new ol.Feature({
  geometry: new ol.geom.Point(
  ol.proj.fromLonLat([data.lon,data.lat])),
  name: [data.name, data.vehicleID],
  });

  marker.setStyle(new ol.style.Style({
  image: new ol.style.Icon({
     anchor: [1,1],
     anchorXUnits: 'fraction',
     anchorYUnits: 'fraction',
     scale : 100/2000, 
     src: './js/fire.png',
    })
  }));
  var vectorSource = new ol.source.Vector({
      features: [marker]
    });

  var markerVectorLayer = new ol.layer.Vector({
        source: vectorSource,        
    });
 
  map.addLayer(markerVectorLayer);


});

var Adata = JSON.parse(document.getElementById('Amb_data').innerHTML);

Array.prototype.forEach.call(Adata, function(data){

  var marker = new ol.Feature({
  geometry: new ol.geom.Point(
  ol.proj.fromLonLat([data.lon,data.lat])),
  name: [data.name, data.vehicleID],
  });

  marker.setStyle(new ol.style.Style({
  image: new ol.style.Icon({
     anchor: [1,1],
     anchorXUnits: 'fraction',
     anchorYUnits: 'fraction',
     scale : 100/2000, 
     src: './js/ambulance.png',
    })
  }));
  var vectorSource = new ol.source.Vector({
      features: [marker]
    });

  var markerVectorLayer = new ol.layer.Vector({
        source: vectorSource,        
    });
 
  map.addLayer(markerVectorLayer);


});



var closer = document.getElementById('popup-closer');
closer.onclick = function() {
  overlay.setPosition(undefined);
  closer.blur();
  return false;
};

var content = document.getElementById('popup-content');
map.on('singleclick', function(evt) {
  var name = map.forEachFeatureAtPixel(evt.pixel, function(feature) {
    return feature.get('name');
  });
  var coordinate = evt.coordinate;
  content.innerHTML = name;
  overlay.setPosition(coordinate);
});

map.on('pointermove', function(evt) {
  map.getTargetElement().style.cursor = map.hasFeatureAtPixel(evt.pixel) ? 'pointer' : '';
});