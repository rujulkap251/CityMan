/* ------------- map amchart 6 start ------------ */

/**
 * Create a map
 */
var map = AmCharts.makeChart("mapamchart6", {
  type: "map",
  theme: "light",
  projection: "winkel3",

  /**
   * Data Provider
   * The images contains pie chart information
   * The handler for `positionChanged` event will take care
   * of creating external elements, position them and create
   * Pie chart instances in them
   */
  dataProvider: {
    map: "continentsLow",
    images: [
      {
        title: "North America",
        latitude: 39.563353,
        longitude: -99.316406,
        width: 150,
        height: 150,
        pie: {
          type: "pie",
          pullOutRadius: 0,
          labelRadius: 0,
          dataProvider: [
            {
              category: "Category #1",
              value: 1200
            },
            {
              category: "Category #2",
              value: 500
            },
            {
              category: "Category #3",
              value: 765
            },
            {
              category: "Category #4",
              value: 260
            }
          ],
          labelText: "[[value]]%",
          valueField: "value",
          titleField: "category"
        }
      },
      {
        title: "Europe",
        latitude: 50.896104,
        longitude: 19.160156,
        width: 200,
        height: 200,
        pie: {
          type: "pie",
          pullOutRadius: 0,
          labelRadius: 0,
          radius: "10%",
          dataProvider: [
            {
              category: "Category #1",
              value: 200
            },
            {
              category: "Category #2",
              value: 600
            },
            {
              category: "Category #3",
              value: 350
            }
          ],
          labelText: "",
          valueField: "value",
          titleField: "category"
        }
      },
      {
        title: "Asia",
        latitude: 47.212106,
        longitude: 103.183594,
        width: 200,
        height: 200,
        pie: {
          type: "pie",
          pullOutRadius: 0,
          labelRadius: 0,
          radius: "10%",
          dataProvider: [
            {
              category: "Category #1",
              value: 352
            },
            {
              category: "Category #2",
              value: 266
            },
            {
              category: "Category #3",
              value: 512
            },
            {
              category: "Category #4",
              value: 199
            }
          ],
          labelText: "",
          valueField: "value",
          titleField: "category"
        }
      },
      {
        title: "Africa",
        latitude: 11.081385,
        longitude: 21.621094,
        width: 200,
        height: 200,
        pie: {
          type: "pie",
          pullOutRadius: 0,
          labelRadius: 0,
          radius: "10%",
          dataProvider: [
            {
              category: "Category #1",
              value: 200
            },
            {
              category: "Category #2",
              value: 300
            },
            {
              category: "Category #3",
              value: 599
            },
            {
              category: "Category #4",
              value: 512
            }
          ],
          labelText: "",
          valueField: "value",
          titleField: "category"
        }
      }
    ]
  },

  /**
   * Add event to execute when the map is zoomed/moved
   * It also is executed when the map first loads
   */
  listeners: [
    {
      event: "positionChanged",
      method: updateCustomMarkers
    }
  ]
});

/**
 * Creates and positions custom markers (pie charts)
 */
function updateCustomMarkers(event) {
  // get map object
  var map = event.chart;

  // go through all of the images
  for (var x = 0; x < map.dataProvider.images.length; x++) {
    // get MapImage object
    var image = map.dataProvider.images[x];

    // Is it a Pie?
    if (image.pie === undefined) {
      continue;
    }

    // create id
    if (image.id === undefined) {
      image.id = "amcharts_pie_" + x;
    }
    // Add theme
    if ("undefined" == typeof image.pie.theme) {
      image.pie.theme = map.theme;
    }

    // check if it has corresponding HTML element
    if ("undefined" == typeof image.externalElement) {
      image.externalElement = createCustomMarker(image);
    }

    // reposition the element accoridng to coordinates
    var xy = map.coordinatesToStageXY(image.longitude, image.latitude);
    image.externalElement.style.top = xy.y + "px";
    image.externalElement.style.left = xy.x + "px";
    image.externalElement.style.marginTop =
      Math.round(image.height / -2) + "px";
    image.externalElement.style.marginLeft =
      Math.round(image.width / -2) + "px";
  }
}

/**
 * Creates a custom map marker - a div for container and a
 * pie chart in it
 */
function createCustomMarker(image) {
  // Create chart container
  var holder = document.createElement("div");
  holder.id = image.id;
  holder.title = image.title;
  holder.style.position = "absolute";
  holder.style.width = image.width + "px";
  holder.style.height = image.height + "px";

  // Append the chart container to the map container
  image.chart.chartDiv.appendChild(holder);

  // Create a pie chart
  var chart = AmCharts.makeChart(image.id, image.pie);

  return holder;
}

/* ------------- map amchart 6 END ------------ */

/* ------------- map amchart 7 start ------------ */
var map = AmCharts.makeChart("seomap", {
  type: "map",
  theme: "light",
  projection: "miller",

  imagesSettings: {
    rollOverColor: "#089282",
    rollOverScale: 3,
    selectedScale: 3,
    selectedColor: "#089282",
    color: "#13564e"
  },

  areasSettings: {
    unlistedAreasColor: "#15A892"
  },

  dataProvider: {
    map: "worldLow",
    images: [
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Brussels",
        latitude: 50.8371,
        longitude: 4.3676
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Copenhagen",
        latitude: 55.6763,
        longitude: 12.5681
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Paris",
        latitude: 48.8567,
        longitude: 2.351
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Reykjavik",
        latitude: 64.1353,
        longitude: -21.8952
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Moscow",
        latitude: 55.7558,
        longitude: 37.6176
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Madrid",
        latitude: 40.4167,
        longitude: -3.7033
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "London",
        latitude: 51.5002,
        longitude: -0.1262,
        url: "http://www.google.co.uk"
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Peking",
        latitude: 39.9056,
        longitude: 116.3958
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "New Delhi",
        latitude: 28.6353,
        longitude: 77.225
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Tokyo",
        latitude: 35.6785,
        longitude: 139.6823,
        url: "http://www.google.co.jp"
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Ankara",
        latitude: 39.9439,
        longitude: 32.856
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Buenos Aires",
        latitude: -34.6118,
        longitude: -58.4173
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Brasilia",
        latitude: -15.7801,
        longitude: -47.9292
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Ottawa",
        latitude: 45.4235,
        longitude: -75.6979
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Washington",
        latitude: 38.8921,
        longitude: -77.0241
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Kinshasa",
        latitude: -4.3369,
        longitude: 15.3271
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Cairo",
        latitude: 30.0571,
        longitude: 31.2272
      },
      {
        zoomLevel: 5,
        scale: 0.5,
        title: "Pretoria",
        latitude: -25.7463,
        longitude: 28.1876
      }
    ]
  }
});

// add events to recalculate map position when the map is moved or zoomed
map.addListener("positionChanged", updateCustomMarkers);

// this function will take current images on the map and create HTML elements for them
function updateCustomMarkers(event) {
  // get map object
  var map = event.chart;

  // go through all of the images
  for (var x in map.dataProvider.images) {
    // get MapImage object
    var image = map.dataProvider.images[x];

    // check if it has corresponding HTML element
    if ("undefined" == typeof image.externalElement)
      image.externalElement = createCustomMarker(image);

    // reposition the element accoridng to coordinates
    var xy = map.coordinatesToStageXY(image.longitude, image.latitude);
    image.externalElement.style.top = xy.y + "px";
    image.externalElement.style.left = xy.x + "px";
  }
}

// this function creates and returns a new marker element
function createCustomMarker(image) {
  // create holder
  var holder = document.createElement("div");
  holder.className = "map-marker";
  holder.title = image.title;
  holder.style.position = "absolute";

  // maybe add a link to it?
  if (undefined != image.url) {
    holder.onclick = function() {
      window.location.href = image.url;
    };
    holder.className += " map-clickable";
  }

  // create dot
  var dot = document.createElement("div");
  dot.className = "dot";
  holder.appendChild(dot);

  // create pulse
  var pulse = document.createElement("div");
  pulse.className = "pulse";
  holder.appendChild(pulse);

  // append the marker to the map container
  image.chart.chartDiv.appendChild(holder);

  return holder;
}
/* ------------- map amchart 7 END ------------ */
