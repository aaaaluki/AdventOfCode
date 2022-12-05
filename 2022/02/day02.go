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
    var result int = 0

    game_result := map[string]int{
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        // Code goes here

        result += game_result[line]
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
    var result int = 0

    game_result := map[string]int{
        "A X": 0 + 3,
        "A Y": 3 + 1,
        "A Z": 6 + 2,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 0 + 2,
        "C Y": 3 + 3,
        "C Z": 6 + 1,
    }

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        // Code goes here

        result += game_result[line]
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
