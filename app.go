package main

import (
	"fmt"
	"os"
	"net/http"
	//"gocv.io/x/gocv"
)

func index_handler(w http.ResponseWriter, r *http.Request) {
	path, _ := os.Getwd()
	fmt.Fprintf(w, path)
}


func main() {

	http.HandleFunc("/", index_handler)
	http.ListenAndServe(":8000", nil)

}