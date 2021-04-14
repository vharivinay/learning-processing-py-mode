//for each pixel (Px, Py) on the screen do
//    x0 := scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.5, 1))
//    y0 := scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1, 1))
//    x := 0.0
//    y := 0.0
//    iteration := 0
//    max_iteration := 1000
//    while (x*x + y*y ≤ 2*2 AND iteration < max_iteration) do
//        xtemp := x*x - y*y + x0
//        y := 2*x*y + y0
//        x := xtemp
//        iteration := iteration + 1
    
//    color := palette[iteration]
//    plot(Px, Py, color)

void setup(){
  size(640, 360);
  colorMode(RGB,1);
  
}

float pos = 0;

void draw(){
  background(255);

  float w = 3.5;
  float h = (w * height) / width;

  float xmin = -w/2;
  float ymin = -h/2;

  loadPixels();
  
  int maxiterations = 100;

  float xmax = xmin + w;

  float ymax = ymin + h;

  float dx = (xmax - xmin) / (width);
  float dy = (ymax - ymin) / (height);

  float y = ymin;
  for (int j = 0; j < height; j++) {

    float x = xmin;
    for (int i = 0; i < width; i++) {

      float a = x;
      float b = y;
      int n = 0;
      while (n < maxiterations) {
        float aa = a * a;
        float bb = b * b;
        float twoab = 2.0 * a * b;
        a = aa - bb + 0.7885 * cos(pos); //0.7885 * exp(-pos);
        b = twoab + 0.7885 * sin(pos);
        
        if (a*a + b*b > 16.0) {
          break; 
        }
        n++;
      }

      if (n == maxiterations) {
        pixels[i+j*width] = color(0);
      } else { 
        // float hue = (255 * n)/maxiterations;
        pixels[i+j*width] = color(sqrt(float(n) / maxiterations)); //color(hue, 255, 255);//
      }
      x += dx;
    }
    y += dy;
  }
  pos = pos + 0.01;
        
  if (pos > TWO_PI){
     noLoop();
  }
  updatePixels();
  println(frameRate);
  //rec();
}
