use rand::Rng;

pub fn rand(length: u8) -> u32 {
    let length_usize = length.into();
    let mut range_max: u32 = "9".repeat(length_usize).parse().expect("Error");
    let mut initial = rand::thread_rng().gen_range(0..range_max + 1);
    let mut count = initial.to_string().chars().count();
    
    while count != length_usize {
        range_max = "9".repeat(length_usize - count).parse().expect("Error");
        let add = rand::thread_rng().gen_range(0..range_max + 1);
        initial = vec![initial.to_string(), add.to_string()].join("").parse().expect("Error");
        count = initial.to_string().chars().count();
    }

    return initial;
}

pub fn split(content: &str) -> Vec<char> {
    return content.chars().collect();
}

pub fn multiple(number: u8) -> bool {
    if number % 7 == 0 {
        return true;
    } else {
        return false;
    }
}

pub fn sum(list: Vec<char>) -> u8 {
    let mut sum = 0;
    for number in list.iter() {
        let test: u8 = number.to_owned().to_string().parse().expect("Error");
        sum += test;
    }
    return sum;
}
