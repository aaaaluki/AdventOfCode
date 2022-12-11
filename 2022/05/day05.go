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

    // Problem vars
    var stackNum int
    var quantity, origin, destination int

    switch filename {
    case "test":
        stackNum = 3
    default:
        stackNum = 9
    }

    stacks := make([][]byte, stackNum)
    for i := 0; i < stackNum; i++ {
        stacks[i] = make([]byte, 0)
    }

    // Parse input
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        if line == "" {
            break
        }

        for i := 0; i < stackNum; i++ {
            box := line[1 + 4*i]
            if box == ' ' {
                continue
            }

            stacks[i] = append(stacks[i], 0)
            copy(stacks[i][1:], stacks[i][0:])
            stacks[i][0] = box
        }
    }

    // Remove last row for each stack (the numbers)
    for i := 0; i < stackNum; i++ {
        stacks[i] = stacks[i][1:]
    }

    // Execute commands
    for scanner.Scan() {
        line := scanner.Text()
        if line == "" {
            break
        }

        fmt.Sscanf(line, "move %d from %d to %d", &quantity, &origin, &destination)
        for i := 0; i < quantity; i++ {
            box := stacks[origin - 1][len(stacks[origin - 1]) - 1]
            stacks[origin - 1] = stacks[origin - 1][:len(stacks[origin - 1]) - 1]
            stacks[destination - 1] = append(stacks[destination - 1], box)
        }
    }

    result := ""
    for i := 0; i < stackNum; i++ {
        // fmt.Println(string(stacks[i][:]))
        result += string(stacks[i][len(stacks[i]) - 1])
    }

    fmt.Printf("Result: %s\n", result)
}

func partTwo(filename string) {
    fmt.Println("Part Two ####################")

    // Read file
    file, err := os.Open(filename)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // Problem vars
    var stackNum int
    var quantity, origin, destination int

    switch filename {
    case "test":
        stackNum = 3
    default:
        stackNum = 9
    }

    stacks := make([][]byte, stackNum)
    for i := 0; i < stackNum; i++ {
        stacks[i] = make([]byte, 0)
    }

    // Parse input
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        if line == "" {
            break
        }

        for i := 0; i < stackNum; i++ {
            box := line[1 + 4*i]
            if box == ' ' {
                continue
            }

            stacks[i] = append(stacks[i], 0)
            copy(stacks[i][1:], stacks[i][0:])
            stacks[i][0] = box
        }
    }

    // Remove last row for each stack (the numbers)
    for i := 0; i < stackNum; i++ {
        stacks[i] = stacks[i][1:]
    }

    // Execute commands
    for scanner.Scan() {
        line := scanner.Text()
        if line == "" {
            break
        }

        fmt.Sscanf(line, "move %d from %d to %d", &quantity, &origin, &destination)
        boxes := stacks[origin - 1][len(stacks[origin - 1]) - quantity:]
        stacks[origin - 1] = stacks[origin - 1][:len(stacks[origin - 1]) - quantity]
        stacks[destination - 1] = append(stacks[destination - 1], boxes...)
    }

    result := ""
    for i := 0; i < stackNum; i++ {
        // fmt.Println(string(stacks[i][:]))
        result += string(stacks[i][len(stacks[i]) - 1])
    }

    fmt.Printf("Result: %s\n", result)
}


func main() {
    if len(os.Args[1:]) < 1 {
        log.Fatal("Not enough arguments given!")
    }

    filename := os.Args[1]
    partOne(filename)
    partTwo(filename)
}
