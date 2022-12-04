package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "sort"
    "strconv"
)


func partOne(filename string) {
}

func partTwo(filename string) {
}


func main() {
    if len(os.Args[1:]) < 1 {
        log.Fatal("Not enough arguments given!")
    }

    filename := os.Args[1]

    fmt.Println("Part One ####################")

    // Read file
    file, err := os.Open(filename)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // Init result
    var result int = 0

    calories := []int{0}
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()

        if line == "" {
            calories = append(calories, 0)
            continue
        }

        lineInt, err := strconv.Atoi(line)
        if err != nil {
            log.Fatal(err)
        }
        
        calories[len(calories) - 1] += lineInt;
    }

    sort.Sort(sort.Reverse(sort.IntSlice(calories)))
    result = calories[0]
    fmt.Printf("Result: %d\n", result)

    fmt.Println("Part Two ####################")
    result = calories[0] + calories[1] + calories[2]
    fmt.Printf("Result: %d\n", result)
}
