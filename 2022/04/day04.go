package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)


func main() {
    if len(os.Args[1:]) < 1 {
        log.Fatal("Not enough arguments given!")
    }

    // Read file
    filename := os.Args[1]
    file, err := os.Open(filename)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // Init result
    var result1, result2 int = 0, 0
    var s1, e1, s2, e2 uint
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()

        _, err := fmt.Sscanf(line, "%d-%d,%d-%d", &s1, &e1, &s2, &e2)
        if err != nil {
            log.Fatal(err)
        }

        // Part one
        if (s1 <= s2 && e2 <= e1) || (s2 <= s1 && e1 <= e2) {
            // fmt.Printf("[Part 1] set1 %d-%d; set2 %d-%d\n", s1, e1, s2, e2)
            result1++
        }

        // Part two
        if (s2 <= s1 && s1 <= e2) || (s1 <= s2 && s2 <= e1) {
            // fmt.Printf("[Part 2] set1 %d-%d; set2 %d-%d\n", s1, e1, s2, e2)
            result2++
        }
    }

    fmt.Println("Part One ####################")
    fmt.Printf("Result: %d\n", result1)

    fmt.Println("Part Two ####################")
    fmt.Printf("Result: %d\n", result2)
}
