<canvas width="300" height="200"></canvas>
canvas {
  border: 1px solid black;
}

let img = new Image();
img.src = 'https://opengameart.org/content/green-cap-character-16x18'
img.onload = function() {
  init();
};

let canvas = document.querySelector('canvas');
let ctx + canvas.getContext('2d');

function init() {
  //animation code will be pasted here eventually
}

drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth,dHeight)
