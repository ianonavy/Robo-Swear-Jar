var drawingCanvas = document.getElementById('myDrawing');

// Check the element is in the DOM and the browser supports canvas
if (drawingCanvas.getContext) {
    // Initaliase a 2-dimensional drawing context
    var context = drawingCanvas.getContext('2d');

    // Create the yellow face
    context.strokeStyle = "#000000";
    context.fillStyle = "#FFFF00";
    var myImage = new Image();
        myImage.onload = function() {
        context.drawImage(myImage, 128, 128, 175, 256);
    }
    myImage.src = "http://roboswearjar.ep.io/static/img/jar.png";
    
    var maxYs = new Object();
    maxYs[140] = 340;
    maxYs[150] = 350;
    maxYs[160] = 355;
    maxYs[170] = 360;
    maxYs[180] = 362;
    maxYs[190] = 362;
    maxYs[200] = 362;
    maxYs[210] = 362;
    maxYs[220] = 362;
    maxYs[230] = 360;
    maxYs[240] = 355;
    maxYs[250] = 350;
    maxYs[260] = 340;
    
    var dollars = 10;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange  = function() { 
        if (xhr.readyState == 4) {
            dollars = parseInt(xhr.responseText);
            for (var i = 0; i < dollars; i++) {
                x = generateX();
                drawCoin(context, x, generateY(x, i, maxYs));
            }
         }
    }; 
    xhr.open("GET", "http://roboswearjar.ep.io/total/", true);
    xhr.send();
}

function random(from, to, interval) {
    return Math.floor(Math.random() * (to / interval - from / interval + 1) + from / interval) * interval;
}

function generateX() {
    return random(140, 260, 10);
}

function generateY(x, h, maxYs) {
    y = maxYs[x];
    if (maxYs[x] > 190) {
        maxYs[x] -= 10;
    }
    return y;
}

function drawCoin(ctx, x, y) {
  var kappa = .5522848,
      w = 30,
      h = 15,
      k = h / 2.5;
      ox = (w / 2) * kappa, // offset horizontal
      oy = (h / 2) * kappa, // offset vertical
      xe = x + w,           // x-end
      ye = y + h,           // y-end
      xm = x + w / 2,       // x-middle
      ym = y + h / 2;       // y-middle
      yt = y - k;
      yet = ye - k;
      ymt = ym - k

  ctx.beginPath();
  ctx.moveTo(xe, ym);
  ctx.bezierCurveTo(xe, ym + oy, xm + ox, ye, xm, ye);
  ctx.bezierCurveTo(xm - ox, ye, x, ym + oy, x, ym);
  ctx.lineTo(x, ymt);
  ctx.bezierCurveTo(x, ymt - oy, xm - ox, yt, xm, yt);
  ctx.bezierCurveTo(xm + ox, yt, xe, ymt - oy, xe, ymt);
  ctx.fill();
  ctx.bezierCurveTo(xe, ymt + oy, xm + ox, yet, xm, yet);
  ctx.bezierCurveTo(xm - ox, yet, x, ymt + oy, x, ymt);
  ctx.moveTo(xe, ymt);
  ctx.lineTo(xe, ym);
  ctx.stroke();
  ctx.closePath();
}
