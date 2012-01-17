var drawingCanvas = document.getElementById('myDrawing');

// Check the element is in the DOM and the browser supports canvas
if (drawingCanvas.getContext) {
    // Initaliase a 2-dimensional drawing context
    var context = drawingCanvas.getContext('2d');
    
    // Set the coin fill and stroke.
    context.strokeStyle = "#000000";
    context.fillStyle = "#FFFF00";
    
    // Max Y values for coins in the jar depending on the x value.
    var maxYs = new Object();
    maxYs[12] = 212;
    maxYs[22] = 222;
    maxYs[32] = 227;
    maxYs[42] = 232;
    maxYs[52] = 234;
    maxYs[62] = 234;
    maxYs[72] = 234;
    maxYs[82] = 234;
    maxYs[92] = 234;
    maxYs[102] = 232;
    maxYs[112] = 227;
    maxYs[122] = 222;
    maxYs[132] = 212;
    
    var dollars = 0;
    // Use AJAX to get the number of dollars in the swear jar.
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange  = function() { 
        if (xhr.readyState == 4) {
            dollars = parseInt(xhr.responseText);
            // Draw a coin for each dollar in the swear jar.
            for (var i = 0; i < dollars; i++) {
                x = generateX();
                drawCoin(context, x, generateY(x, maxYs));
            }
            
            // Draw the jar on top of the coins.
            var myImage = new Image();
                myImage.onload = function() {
                context.drawImage(myImage, 0, 0, 175, 256);
            }
            myImage.src = "http://roboswearjar.ep.io/static/img/jar.png";
        }
    }; 
    xhr.open("GET", "http://roboswearjar.ep.io/total/", true);
    xhr.send();
}

/**
 * Generates a random number from a number to another number at a certain interval.
 */
function random(from, to, interval) {
    return Math.floor(Math.random() * (to / interval - from / interval + 1) + from / interval) * interval;
}

/**
 * Generates a random pixel value between 12 and 132 at an interval of 10.
 */
function generateX() {
    return random(10, 130, 10) + 2;
}

/**
 * Generates the y value for the coin. Subtracting from the array of stored
 * y values per x-value allows for a stacking effect to be created.
 */
function generateY(x, maxYs) {
    y = maxYs[x];
    if (maxYs[x] > 62) {
        maxYs[x] -= 10;
    }
    return y;
}

/**
 * Canvas function to actually draw the coin.
 */
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
