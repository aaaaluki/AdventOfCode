package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
    "math"
)


func calculations(filename string) {
    // Read file
    file, err := os.Open(filename)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // Init result
    var result1 int = 0
    var result2 int = 0
    locationID1 := []int {}
    locationID2 := []int {}

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        // Code goes here
        parts := strings.Split(line, "   ")

        num1, err := strconv.Atoi(parts[0])
        if err != nil {
            log.Fatal(err)
        }
        locationID1 = append(locationID1, num1)

        num2, err := strconv.Atoi(parts[1])
        if err != nil {
            log.Fatal(err)
        }
        locationID2 = append(locationID2, num2)
    }

    fmt.Println("Part One ####################")
    sort.Slice(locationID1, func(i, j int) bool {
        return locationID1[i] < locationID1[j]
    })
    sort.Slice(locationID2, func(i, j int) bool {
        return locationID2[i] < locationID2[j]
    })

    for i := range locationID1 {
        result1 += int(math.Abs(float64(locationID1[i] - locationID2[i])))
    }

    fmt.Printf("Result: %d\n", result1)

    fmt.Println("Part Two ####################")
    freqs := make(map[int]int)
    for _, v := range locationID2 {
        freqs[v]++
    }

    for _, v := range locationID1 {
        mult, exists := freqs[v]
        if !exists {
            mult = 0
        }
        result2 += v*mult
    }

    fmt.Printf("Result: %d\n", result2)
}

func main() {
    if len(os.Args[1:]) < 1 {
        log.Fatal("Not enough arguments given!")
    }

    filename := os.Args[1]
    calculations(filename)
}
