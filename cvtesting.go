package main

import (
	"fmt"
	// "os"

	"gocv.io/x/gocv"
)

func main() {

	filename := "spidy.jpg"
	// read image
	img := gocv.IMRead(filename, gocv.IMReadGrayScale)

	// check size of img
	a := img.Size()


	// downsize if too large (or always downsize?)
	// func Resize(src Mat, dst *Mat, sz image.Point, fx, fy float64, interp InterpolationFlags)
	gocv.Resize(img, img, img.Size(), 0.5, 0.5, "INTER_AREA")

	fmt.Println(a)

	// window := gocv.NewWindow("Hello")
	// for {
	// 	window.IMShow(img)
	// 	if window.WaitKey(1) >= 0 {
	// 		break
	// 	}
	// }

}