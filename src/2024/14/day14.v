import os
import regex
import math

struct Position {
pub mut:
	x int @[required]
	y int @[required]
}

struct Velocity {
pub mut:
	x int @[required]
	y int @[required]
}

struct Robot {
pub mut:
	position Position @[required]
	velocity Velocity @[required]
}

pub const width = 101
pub const height = 103

fn parse_input() []Robot {
	contents := os.read_file('input.txt') or { panic(err) }

	return contents.split_into_lines().map(fn (line string) Robot {
		mut pattern := regex.regex_opt(r'-?\d+') or { panic(err) }
		values := pattern.find_all_str(line).map(it.int())

		return Robot{
			position: Position{
				x: values[0]
				y: values[1]
			}
			velocity: Velocity{
				x: values[2]
				y: values[3]
			}
		}
	})
}

fn calculate_robot_change(mut robot Robot, ticks int) {
	robot.position.x = math.modulo_floored((robot.position.x + (robot.velocity.x * ticks)),
		width)
	robot.position.y = math.modulo_floored((robot.position.y + (robot.velocity.y * ticks)),
		height)
}

fn part01() {
	mut robots := parse_input()

	// Tick 100
	for mut robot in robots {
		calculate_robot_change(mut robot, 100)
	}

	// Determine robots in each quadrant
	mut quadrants := [0, 0, 0, 0]
	midx := width / 2
	midy := height / 2

	for robot in robots {
		// In no counting zone
		if robot.position.x == midx || robot.position.y == midy {
			continue
		}

		// Count
		if robot.position.x < midx && robot.position.y < midy {
			quadrants[0] += 1
		} else if robot.position.x > midx && robot.position.y < midy {
			quadrants[1] += 1
		} else if robot.position.x < midx && robot.position.y > midy {
			quadrants[2] += 1
		} else if robot.position.x > midx && robot.position.y > midy {
			quadrants[3] += 1
		}
	}

	// Result
	mut tlt := quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
	println('Part 01: ${tlt}')
}

fn part02() {
	mut tlt := 0

	robots := parse_input()
	for tick in 0 .. 10_000 {
		mut robots_change := robots.clone()

		// Tick
		mut position_map := map[string]int{}
		for mut robot in robots_change {
			calculate_robot_change(mut robot, tick)
			position_map['x${robot.position.x}y${robot.position.y}'] += 1
		}

		mut found_tree := true
		for cnt in position_map.values() {
			if cnt != 1 {
				found_tree = false
				break
			}
		}

		if found_tree {
			tlt = tick
			break
		}
	}

	println('Part 02: ${tlt}')
}

fn main() {
	// Part 01
	part01()

	// Part 02
	part02()
}
