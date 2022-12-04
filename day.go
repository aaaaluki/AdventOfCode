package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)


func partOne(filename string) {
    fmt.Println("Part One ####################")

    // Read file
    file, err := os.Open(filename)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // Init result
    var result int32 = 0

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        // Code goes here

    }

    fmt.Printf("Result: %d\n", result)
}

func partTwo(filename string) {
    fmt.Println("Part Two ####################")

    // Read file
    file, err := os.Open(filename)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // Init result
    var result int32 = 0

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        // Code goes here

    }

    fmt.Printf("Result: %d\n", result)
}


func main() {
    if len(os.Args[1:]) < 1 {
        log.Fatal("Not enough arguments given!")
    }

    filename := os.Args[1]
    partOne(filename)
    partTwo(filename)
}
