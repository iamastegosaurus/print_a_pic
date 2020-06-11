package main

import (
	"fmt"
	"os"
	"io"
)

func main() {

	f, _ := os.Create("asdf.obj")

	// for i float = 0; i < 10; i++ {
	// 	for j float = 0; j < 10; j++ {
	// 		for k float = 0; k < 10; k++ {

	// 		}
	// 	}
	// }
	io.WriteString(f, fmt.Sprintf("v %.3f %.3f %.3f\n", 0, 0, 0))
	f.WriteString("v 1 0 0\n")
	f.WriteString("v 0 1 0\n")
	f.WriteString("f 1 2 3\n")
	

    fmt.Printf("asdf")
}
