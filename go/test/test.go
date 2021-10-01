package main

import (
  "fmt"
  "os"
  tm "github.com/buger/goterm"
  "time"
)

func check(e error) {
  if e != nil {
    panic(e)
  }
}

func main() {
  logo_dat, err := os.ReadFile("data/gui/0000-logo.txt")
  body_dat, err := os.ReadFile("data/gui/0000-titlescreen.txt")

  check(err)
  var logo = string(logo_dat)
  var body = string(body_dat)

  tm.Clear()
  
  box := tm.NewBox(50|tm.PCT, 8, 0)
  fmt.Fprint(box, logo)
  
  tm.Print(tm.MoveTo(box.String(), 1, 1))
  tm.Flush()
  fmt.Println("")
  fmt.Println(body)

  time.Sleep(time.Second)
}

