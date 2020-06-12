package main

import (
	"fmt"
	"math"
	"os"
	"io"
	"image"
	"gocv.io/x/gocv"
)

func getIMG(filename string) (gocv.Mat, int, int) {

	var maxPX float64 = 200000

	img := gocv.IMRead(filename, gocv.IMReadGrayScale)
	var w int = img.Size()[1]
	var h int = img.Size()[0]
	pixelCount := float64(w * h)

	if pixelCount > maxPX {
		rescaleFactor := maxPX / pixelCount
		h = int(float64(h) * math.Sqrt(rescaleFactor))
		w = int(float64(w) * math.Sqrt(rescaleFactor))
		newDim := image.Point{h, w}
		gocv.Resize(img, &img, newDim, 0, 0, gocv.InterpolationLinear)
		fmt.Printf("rescaled to: (%d, %d)\n", w, h)

	} else {
		fmt.Printf("dimensions maintained: (%d, %d)\n", w, h)
	}
	return img, w, h
}

func main() {

	path, _ := os.Getwd()
	readFile := path + "\\images\\" + "sun.jpg"
	writeFile := path + "\\results\\" + "sun.obj"

	var img gocv.Mat
	var w, h int
	img, w, h = getIMG(readFile)

	f, _ := os.Create(writeFile)

	// reading all values
	var i, j int
	var k uint8
	var v float64
	for j = 0; j < h; j++ {
		for i = 0; i < w; i++ {
			// get type of gocv.Mat - CV8U -> GetUCharAt
			// fmt.Println(img.Type())
			k = img.GetUCharAt(j, i)
			v = math.Sqrt(float64(k))
			io.WriteString(f, fmt.Sprintf("v %d %d %.3f\n", i, j, v))
		}
	}

	var a, b, c, d int
	for j = 0; j < h-1; j++ {
		for i = 0; i < w-1; i++ {
			a = i + 1 + w*j
			b = a + 1
			c = b + w
			d = c - 1
			io.WriteString(f, fmt.Sprintf("f %d %d %d\n", a, b, c))
			io.WriteString(f, fmt.Sprintf("f %d %d %d\n", c, d, a))
		}
	}


	//to show 'img' if necessary
	// window := gocv.NewWindow("Hello")
	// for {
	// 	window.IMShow(img)
	// 	if window.WaitKey(1) >= 0 {
	// 		break
	// 	}
	// }

}