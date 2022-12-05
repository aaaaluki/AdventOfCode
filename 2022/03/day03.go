package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strings"
)


func contains(s []rune, e rune) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}

func partOne(filename string) {
    fmt.Println("Part One ####################")

    // Read file
    file, err := os.Open(filename)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // Init result
    intersection := []rune{}

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        n := len(line) / 2
        part1 := line[:n]
        part2 := line[n:]

        for _, e := range part1 {
            if strings.ContainsRune(part2, e) {
                intersection = append(intersection, e)
                break
            }
        }
    }

    result := 0
    for _, r := range intersection {
        foo := r - 0x60

        if foo < 0 {
            foo += 29*2
        }

        result += int(foo)
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
    intersection := []rune{}

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line1 := scanner.Text()
        scanner.Scan()
        line2 := scanner.Text()
        scanner.Scan()
        line3 := scanner.Text()

        foo := []rune{}
        for _, e1 := range line1 {
            if strings.ContainsRune(line2, e1) {
                foo = append(foo, e1)
            }
        }

        bar := []rune{}
        for _, e3 := range line3 {
            if contains(foo, e3) && !contains(bar, e3) {
                bar = append(bar, e3)
            }
        }

        for _, r := range bar {
            intersection = append(intersection, r)
        }
    }

    result := 0
    for _, r := range intersection {
        foo := r - 0x60

        if foo < 0 {
            foo += 29*2
        }

        result += int(foo)
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

