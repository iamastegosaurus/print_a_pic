package main

import (
	"fmt"
	"os"
	"io"
	"net/http"
	"html/template"

)

func index_handler(w http.ResponseWriter, r *http.Request) {
	path, _ := os.Getwd()
	// fmt.Fprintf(w, path)

	t, _ := template.ParseFiles("index.html")
	t.ExecuteTemplate(w, "index.html", t)

	if r.Method != http.MethodPost {
		fmt.Println("not post")
		return
	}

	err := r.ParseMultipartForm(200000)
	if err != nil {
		fmt.Println(err)
	}

	file, handler, err := r.FormFile("file")
	if err != nil {
		fmt.Println(err)
	}

	createfile := path + "\\images\\" + handler.Filename
	fmt.Println(createfile)

	resFile, err := os.Create(createfile)
	if err != nil {
		fmt.Println(err)
	}

	io.Copy(resFile, file)
	fmt.Println("successfully uploaded")

}


func main() {

	http.HandleFunc("/", index_handler)
	http.ListenAndServe(":8000", nil)

}