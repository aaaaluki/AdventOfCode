package hashset

import (
    "fmt"
    "strings"
)

// var to know if an element is present on the set
var present = struct{}{}

// Set is just a map wrapper
type Set struct {
	items map[interface{}]struct{}
}

/// General container-like functions
func New(elements ...interface{}) (* Set) {
    set := &Set{items: make(map[interface{}]struct{})}

    if len(elements) > 0 {
        set.Add(elements)
    }

    return set
}

func (set *Set) Add(elements ...interface{}) {
    for _, e := range elements {
        set.items[e] = present
    }
}

func (set *Set) Remove(elements ...interface{}) {
    for _, e := range elements {
        delete(set.items, e)
    }
}

func (set *Set) Contains(elements ...interface{}) bool {
    for _, e := range elements {
        if _, v := set.items[e]; !v {
            return false
        }
    }

    return true
}

func (set *Set) Size() int {
    return len(set.items)
}

func (set *Set) Empty() bool {
    return set.Size() == 0
}

func (set *Set) Clear() {
    set.items = make(map[interface{}]struct{})
}

func (set *Set) Values() []interface{} {
    values := make([]interface{}, set.Size())

    i := 0
    for element := range set.items {
        values[i] = element
        i++
    }

    return values
}

func (set *Set) String() string {
    stringElements := []string{}
    for element := range set.items {
        stringElements = append(stringElements, fmt.Sprintf("%v", element))
    }

    return "{" + strings.Join(stringElements, ", ") + "}"
}

/// Set-like methods
func (set *Set) Difference(another *Set) *Set {
    result := New()

    for element := range set.items {
        if !another.Contains(element) {
            result.Add(element)
        }
    }

    return result
}

func (set *Set) Intersection(another *Set) *Set {
    result := New()

    if set.Size() <= another.Size() {
        for element := range set.items {
            if another.Contains(element) {
                result.Add(element)
            }
        }
    } else {
        for element := range another.items {
            if set.Contains(element) {
                result.Add(element)
            }
        }
    }

    return result
}

func (set *Set) IsSubset(another *Set) bool {
    for element := range set.items {
        if !another.Contains(element) {
            return false
        }
    }

    return true
}

func (set *Set) SymmetricDifference(another *Set) *Set {
    diff1 := set.Difference(another)
    diff2 := another.Difference(set)

    return diff1.Union(diff2)
}

func (set *Set) Union(another *Set) *Set {
    result := New()

    for element := range set.items {
        result.Add(element)
    }

    for element := range another.items {
        result.Add(element)
    }

    return result
}

