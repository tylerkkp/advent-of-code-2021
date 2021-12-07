extern crate csv;

use std::io;

fn main() {
    // Create a CSV parser that reads data from stdin.
    let mut rdr = csv::Reader::from_reader(io::stdin());

    // create array for counting ones (will just invert for zeroes)
    let mut ones:[ i32 ; 12 ] = [ 0 ; 12 ] ; // cheat here by using known length of 12

    let mut count = 0;

    // Loop over each record.
    for result in rdr.records() {
        // An error may occur, so abort the program in an unfriendly way.
        let record = result.expect("a line");
        let s = record.as_slice();
        let length = s.len();
        count += 1;

        for i in 0..length {
            let chars: Vec<char> = s.chars().collect();
            if chars[i] == '1' {
                ones[i] += 1;
            }
        }
    }
    let output1 = ones.map(|x| if x > count/2 {"1"} else {"0"});
    let output0 = ones.map(|x| if x <= count/2 {"1"} else {"0"});
    let strout1 = output1.concat();
    let strout0 = output0.concat();
    let intout1 = isize::from_str_radix(&strout1, 2).unwrap();
    let intout0 = isize::from_str_radix(&strout0, 2).unwrap();
    println!("{:?} * {:?} = {:?}", intout1, intout0, intout0 * intout1);
}
