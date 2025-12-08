import os
import regex
import math

struct Data {
pub mut:
	x []int
	y []int
}

fn parse_input() Data {
	lines := os.read_lines('input.txt') or { panic(err) }

	mut x := []int{}
	mut y := []int{}

	for line in lines {
		mut pattern := regex.regex_opt(r'\d+') or { panic(err) }
		values := pattern.find_all_str(line).map(it.int())

		x << values[0]
		y << values[1]
	}

	return Data{
		x: x
		y: y
	}
}

fn solve() {
	// Getting data
	mut data := parse_input()
	data.x.sort()
	data.y.sort()

	mut tlt1 := 0
	mut tlt2 := 0

	for indx in 0 .. data.x.len {
		tlt1 += math.abs(data.x[indx] - data.y[indx])
		tlt2 += data.x[indx] * data.y.filter(it == data.x[indx]).len
	}

	println('Part 01: ${tlt1}')
	println('Part 02: ${tlt2}')
}

fn main() {
	// Part 01 and Part 02
	solve()
}
