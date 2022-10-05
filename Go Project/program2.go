package main

import ("fmt"
        "os"
        "io/ioutil"
        "strconv"
        "strings"
        "bufio"
      )

func openFile(inFile string)(char []string) {

  fmt.Println("---------------Begin Reading File---------------")
  fb, err := ioutil.ReadFile(inFile)

  if err != nil {
    error()
  }
  //cast to string
  indata := string(fb)
  cd := bufio.NewScanner(strings.NewReader(indata))
  //split by character
  cd.Split(bufio.ScanRunes)

  for cd.Scan() {
    //fmt.Print(cd.Text()) debug
    char = append(char, cd.Text())
  }
  return char

}

func parseFile(char []string)(out []string) {
  fmt.Println("\n---------------Decoding---------------")
  cntr := 0;
  //fmt.Println("len ", len(char)-3) debug
  //runs through next 2 chars (-3 is in order to prevent running out of chars)
  for cntr < len(char)-3{

    a := char[cntr]
    b := char[cntr+1]
    c := char[cntr+2]

    //attempt to convert to ints
    ai, err1 := strconv.Atoi(a);
    bi, err2 := strconv.Atoi(b);
    ci, err3 := strconv.Atoi(c);

    //if all 3 convert
    if err1 == nil && err2 == nil && err3 == nil{
      ascii := (ai*100) + (bi*10) + ci
      out = append(out, string(ascii))


      cntr = cntr + 3

      //if first 2 convert
    }else if err1 == nil && err2 == nil && err3 != nil{
      ascii := (ai*10) + bi
      out = append(out, string(ascii))

      cntr = cntr + 2
      //if only first converts
    }else if err1 == nil && err2 != nil && err3 != nil{
      ascii := ai
      out = append(out, string(ascii))

      cntr++

    }else{
      cntr++
    }

  }
  return out
}

func writeData(out []string){
  fmt.Println("\n---------------Begin Writing to File---------------")

  fmt.Println("\nEnter output file name: ")
  var filename string
  fmt.Scanln(&filename)

  file, err := os.Create(filename)

  if err != nil {
    error()
  }

  defer file.Close()
  for _, outssingle := range out {
    fmt.Fprintf(file, outssingle)
  }

}

func error(){
  panic("error")

  os.Exit(1)

}

func main() {
  args := os.Args[1]

  char := openFile(args)

  //fmt.Printf("%v", char) debug

  //fmt.Println(args) debug

  //fmt.Println("------------------------------")

  out := parseFile(char)

  for j := 0; j < len(out); j++ {
    fmt.Printf(out[j])
  }

  writeData(out)

}
