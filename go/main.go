package main

import (
	"fmt"
	"math"

	"github.com/sirupsen/logrus"
)

type Vertex struct {
	X, Y int
}

type Coord struct {
	Lat, Long float64
}

var m map[string]Coord

var (
	v1 = Vertex{1, 2}  // has type Vertex
	v2 = Vertex{X: 1}  // Y:0 is implicit
	v3 = Vertex{}      // X:0 and Y:0
	p  = &Vertex{1, 2} // has type *Vertex
)

func Sqrt(x float64) float64 {
	z := 1.0
	for i := 0; i < 100; i++ {
		z -= (z*z - x) / (2 * z)
	}

	return z
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}

func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

type Vert struct {
	X, Y float64
}

// the Abs method has a receiver of type Vertex named v
func (v Vert) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// Pointer receivers
func (v *Vert) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func Index[T comparable](s []T, x T) int {
	for i, v := range s {
		// v and x are type T, which has the comparable
		// constraint, so we can use == here.
		if v == x {
			return i
		}
	}
	return -1
}

// Generic types
// List represents a singly-linked list that holds
// values of any type.
type List[T any] struct {
	next *List[T]
	val  T
}

func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum // send sum to c
}

func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func main() {
	logrus.Info("hello from Nhat-Vu Nguyen!")

	channel := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-channel)
		}
		quit <- 0
	}()
	fibonacci(channel, quit)

	// 	ch <- v    // Send v to channel ch.
	//  v := <-ch  // Receive from ch, and assign value to v.
	// ch := make(chan int)
	s := []int{7, 2, 8, -9, 4, 0}

	c := make(chan int)
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c // receive from c

	fmt.Println(x, y, x+y)

	// Type parameters
	// Index works on a slice of ints
	si := []int{10, 20, 15, -10}
	fmt.Println(Index(si, 15))

	// Index also works on a slice of strings
	ss := []string{"foo", "bar", "baz"}
	fmt.Println(Index(ss, "hello"))

	// Methods, Go does not have classes. However, you can define methods on types.
	vert := Vert{3, 4}
	vert.Scale(10)
	fmt.Println(vert.Abs())

	// Function closures
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}

	// Function values
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(hypot(5, 12))

	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))

	mp := make(map[string]int)

	mp["Answer"] = 42
	fmt.Println("The value:", m["Answer"])

	mp["Answer"] = 48
	fmt.Println("The value:", m["Answer"])

	delete(mp, "Answer")
	fmt.Println("The value:", m["Answer"])

	v, ok := mp["Answer"]
	fmt.Println("The value:", v, "Present?", ok)

	m = make(map[string]Coord)
	m["Bell Labs"] = Coord{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])

	var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}

	b := make([]int, 0, 5)
	printSlice("b", b)

	fmt.Println(v1, p, v2, v3)

	pointers()
	access_pointer()

	fmt.Println(Sqrt(2))

	defer fmt.Println("world")
	fmt.Println("hello")

	fmt.Println("counting")
	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("done")
}

func access_pointer() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)
}

func pointers() {
	i, j := 42, 2701

	// var p *int
	p := &i         // point to i
	fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see the new value of j
}
