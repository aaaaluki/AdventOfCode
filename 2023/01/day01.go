package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"unicode"
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
	var first int = -1
	var last int = -1

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		// Code goes here
		first = -1
		last = -1

		for _, c := range line {
			if unicode.IsDigit(c) {
				if first == -1 {
					first = int(c - '0')
				} else {
					last = int(c - '0')
				}
			}
		}
		_ = line

		if last == -1 {
			last = first
		}

		result += 10*first + last
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

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		// Code goes here
		_ = line

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
