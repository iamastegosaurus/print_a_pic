package main

import (
	"fmt"
	"os/exec"
	"sync"
)

func main() {

	var images = [4] string {"snow-removal.jpg", "sitting.jpg", "sun.jpg", "gnome.jpg"}
	var wg sync.WaitGroup
	wg.Add(4)

	for _, v := range images {

		go func() {
			printapic(v)
			wg.Done()
		}()
	}

	wg.Wait()
	fmt.Println("all groups done")

}

func printapic(img_name string) {

	cmd := exec.Command("python",  "pyprocessing.py", img_name)
    // fmt.Println(cmd.Args)
    _, err := cmd.CombinedOutput()
    if err != nil { fmt.Println(err); }
    // fmt.Println(string(out))

}