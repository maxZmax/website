var x = new XMLHttpRequest();
path = "http://" + document.location.host + "/logo"
x.open("GET", path, false);
x.send(null);
imageOut = document.querySelector('.image-out');
img = document.createElement('img');
img.src = "http://" + document.location.host + x.responseText;
imageOut.append(img);