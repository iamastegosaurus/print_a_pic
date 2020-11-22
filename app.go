package main

import (
	"fmt"
	"os"
	"io"
	"net/http"
	"html/template"
	//"sync"
)

func index_handler(w http.ResponseWriter, r *http.Request) {
	path, _ := os.Getwd()

	t, _ := template.ParseFiles("index.html")
	t.ExecuteTemplate(w, "index.html", t)

	if r.Method != http.MethodPost { return }

	err := r.ParseMultipartForm(200000)
	if err != nil {	fmt.Println(err) }

	file, handler, err := r.FormFile("file")
	if err != nil { fmt.Println(err) }

	createfile := path + "\\images\\" + handler.Filename

	resFile, err := os.Create(createfile)
	if err != nil { fmt.Println(err) }

	io.Copy(resFile, file)
	fmt.Println("successfully uploaded " + handler.Filename)

	defer resFile.Close()

	go printapic(handler.Filename)
}

func printapic(img_name string) {

	for i:= 0; i < 10; i++ {
		fmt.Println(i)
	}
	fmt.Println("ok")



}


func main() {

	http.HandleFunc("/", index_handler)
	http.ListenAndServe(":8000", nil)

}