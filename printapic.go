package main

import (
	"fmt"
	"math"
	"os"
	"io"
	"image"
	"gocv.io/x/gocv"
)


func getIMG(filename string) (gocv.Mat) {

	var maxPX float64 = 300000

	img := gocv.IMRead(filename, gocv.IMReadGrayScale)
	var w int = img.Size()[1]
	var h int = img.Size()[0]
	pixelCount := float64(w * h)

	if pixelCount > maxPX {
		w = int(float64(w) * math.Sqrt(maxPX / pixelCount))
		h = int(float64(h) * math.Sqrt(maxPX / pixelCount))
		newDim := image.Point{w, h}
		gocv.Resize(img, &img, newDim, 0, 0, gocv.InterpolationLinear)
		fmt.Printf("rescaled to: (%d, %d)\n", w, h)
	} else {
		fmt.Printf("dimensions maintained: (%d, %d)\n", w, h)
	}
	return img
}

func main() {

	name := "dnd"
	path, _ := os.Getwd()
	readFile := path + "\\images\\" + name + ".png"
	writeFile := path + "\\results\\" + name + ".obj"

	var img gocv.Mat = getIMG(readFile)
	var w int = img.Size()[1]
	var h int = img.Size()[0]

	f, _ := os.Create(writeFile)

	var i, j int
	var px_val uint8
	var k float64

	var a, b, c, d int

	for j = 0; j < h; j++ {
		for i = 0; i < w; i++ {
			// get type of gocv.Mat - CV8U -> GetUCharAt
			// fmt.Println(img.Type())
			px_val = img.GetUCharAt(j, i)
			k = math.Sqrt(float64(px_val / 4))
			io.WriteString(f, fmt.Sprintf("v %d %d %.3f\n", i, -j, 16-k))

			if (i < w-1 && j < h-1) {
				a = i + 1 + w*j
				b = a + 1
				c = b + w
				d = c - 1
				defer io.WriteString(f, fmt.Sprintf("f %d %d %d\n", a, b, c))
				defer io.WriteString(f, fmt.Sprintf("f %d %d %d\n", c, d, a))

				// if j == 0 { // connect top edges
				// 	defer io.WriteString(f, fmt.Sprintf("f %d %d %d %d\n", b, a, w*h+1, w*h+2))
				// }
				// if j == w-2 { // bottom edges
				// 	defer io.WriteString(f, fmt.Sprintf("f %d %d %d %d\n", c, d, w*h+3, w*h+4))
				// }
				// if i == 0 { // left edges
				// 	defer io.WriteString(f, fmt.Sprintf("f %d %d %d %d\n", a, d, w*h+4, w*h+1))
				// }
				// if i == h-2 { //right edges
				// 	defer io.WriteString(f, fmt.Sprintf("f %d %d %d %d\n", c, b, w*h+2, w*h+3))
				// }

			}
		}
	}

	var depth int = 0 // make negative
	io.WriteString(f, fmt.Sprintf("v %d %d %d\n", 0, 0, depth))
	io.WriteString(f, fmt.Sprintf("v %d %d %d\n", w-1, 0, depth))
	io.WriteString(f, fmt.Sprintf("v %d %d %d\n", w-1, -h+1, depth))
	io.WriteString(f, fmt.Sprintf("v %d %d %d\n", 0, -h+1, depth))

	defer io.WriteString(f, fmt.Sprintf("f %d %d %d %d\n", w*h+1, w*h+2, w*h+3, w*h+4))

}
