function getColor() {
  var red = (Math.floor((256 - 199) * Math.random()) + 200);
  var green = (Math.floor((256 - 199) * Math.random()) + 200);
  var blue = (Math.floor((256 - 199) * Math.random()) + 200);
  // var hue = 'rgb(' + red + ',' + green + ',' + blue + ')';
  var color = "#"+red.toString(16) + green.toString(16) + blue.toString(16);
  return color;
}
