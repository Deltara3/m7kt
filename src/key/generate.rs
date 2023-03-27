use crate::util;
use super::validate;
use rand::Rng;

pub fn cd10() -> String {
    let mut blk_one = util::rand(3);
    while validate::three_block(blk_one.try_into().unwrap()) == false {
        blk_one = util::rand(3);
    }

    let mut blk_two = util::rand(7);
    while validate::seven_block(blk_two) == false {
        blk_two = util::rand(7);
    }

    return vec![blk_one.to_string(), blk_two.to_string()].join("-");
}

pub fn cd11() -> String {
    let blk_one = util::rand(3);
    let mut buffer: u8 = util::split(&blk_one.to_string())[2].to_owned().to_string().parse().expect("Error");
    buffer += rand::thread_rng().gen_range(1..3);

    if buffer > 9 {
        buffer = buffer.to_string().chars().last().unwrap().to_string().parse().expect("Error");
    }

    let mut blk_two = util::rand(7);
    while validate::seven_block(blk_two) == false {
        blk_two = util::rand(7);
    }
    
    return vec![vec![blk_one.to_string(), buffer.to_string()].join(""), blk_two.to_string()].join("-");
}

pub fn oem20() -> String {
    let mut date = rand::thread_rng().gen_range(1..366).to_string();
    if date.chars().count() != 3 {
        date = vec!["0".repeat(3 - date.chars().count()), date].join("");
    }

    let mut year = rand::thread_rng().gen_range(95..103).to_string();

    if year.chars().count() == 3 {
        let buffer = util::split(&year);
        year = vec![buffer[1].to_string(), buffer[2].to_string()].join("");
    }

    let blk_one = vec![date, year].join("");

    let mut blk_three = util::rand(6);
    while validate::seven_block(blk_three) == false {
        blk_three = util::rand(6);
    }

    let blk_four = util::rand(5);
    
    return vec![blk_one, "OEM".to_string(), vec!["0".to_string(), blk_three.to_string()].join(""), blk_four.to_string()].join("-");
}
