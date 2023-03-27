use crate::util;

const THREE_BLOCK_BLACKLIST: [u16; 7] = [333, 444, 555, 666, 777, 888, 999];
const YEAR_WHITELIST: [u8; 8] = [95, 96, 97, 98, 99, 00, 01, 02];
const OEM_BLOCK: &str = "OEM";

pub fn three_block(block: u16) -> bool {
    if THREE_BLOCK_BLACKLIST.contains(&block) {
        return false;
    } else {
        return true;
    }
}

pub fn four_block(block: u16) -> bool {
    let split = util::split(&block.to_string());
    let third: u8 = split[2].to_string().parse().expect("Error");
    let mut fourth: u8 = split[3].to_string().parse().expect("Error");

    if fourth - third == 1 || fourth - third == 2 {
        return true;
    } else {
        if fourth == 0 {
            fourth = 10;
        } else if fourth == 1 {
            fourth = 11;
        } else {
            return false;
        }
        if fourth - third == 1 || fourth - third == 2 {
            return true;
        } else {
            return false;
        }
    }
}

pub fn seven_block(block: u32) -> bool {
    let split = util::split(&block.to_string());
    
    if util::multiple(util::sum(split)) == false {
        return false
    } else {
        return true;
    }
}

pub fn date_block(block: u32) -> bool {
    let days = 1..366;

    let split = util::split(&block.to_string());
    let day = vec![split[0].to_string(), split[1].to_string(), split[2].to_string()].join("").parse().expect("Error");
    let year = vec![split[3].to_string(), split[4].to_string()].join("").parse().expect("Error");

    if days.contains(&day) {
        if YEAR_WHITELIST.contains(&year) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

pub fn oem_block(block: &str) -> bool {
    if block == OEM_BLOCK {
        return true;
    } else {
        return false;
    }
}

pub fn key(key: &String) -> bool {
    match key.chars().count() {
        11 => {
            let blocks = key.split("-").collect::<Vec<&str>>();

            if three_block(blocks[0].parse().expect("Error")) {
                if seven_block(blocks[1].parse().expect("Error")) {
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        },
        12 => {
            let blocks = key.split("-").collect::<Vec<&str>>();

            if four_block(blocks[0].parse().expect("Error")) {
                if seven_block(blocks[1].parse().expect("Error")) {
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        },
        23 => {
            let blocks = key.split("-").collect::<Vec<&str>>();

            if date_block(blocks[0].parse().expect("Error")) {
                if oem_block(blocks[1]) {
                    if seven_block(blocks[2].parse().expect("Error")) {
                        if blocks[3].to_string().parse::<f64>().is_ok() {
                            if blocks[3].to_string().chars().count() == 5 {
                                if util::split(blocks[2])[0] == '0' {
                                    return true;
                                } else {
                                    return false;
                                }
                            } else {
                                return false;
                            }
                        } else {
                            return false;
                        }
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            } else {
                return false;
            }
        },
        _ => {
            return false;
        }
    }
}
