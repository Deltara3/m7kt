pub(crate) mod util;
pub(crate) mod key;

use colored::*;
use clap::{arg, command, ArgAction, Command};

fn main() {
    let matches = command!()
        .subcommand(
            Command::new("generate")
                .about("Generates keys")
                .arg(
                    arg!(-t --type "Key type to generate, must be 10, 11, or 20")
                        .action(ArgAction::Set)
                        .required(true)
                )
        )
        .subcommand(
            Command::new("validate")
                .about("Validates keys")
                .arg(
                    arg!(-k --key "Key to validate")
                        .action(ArgAction::Set)
                        .required(true)
                )
        )
        .get_matches();

        if let Some(matches) = matches.subcommand_matches("generate") {
            let product_type = matches.get_one::<String>("type");
            if product_type.is_some() {
                match product_type.unwrap().to_owned().parse().expect("Error") {
                    10 => println!("{} CD-10 {}", "[+]".green(), key::generate::cd10()),
                    11 => println!("{} CD-11 {}", "[+]".green(), key::generate::cd11()),
                    20 => println!("{} OEM-20 {}", "[+]".green(), key::generate::oem20()),
                    _ => println!("{} Invalid key type.", "[-]".red())
                }
            }
        }

        if let Some(matches) = matches.subcommand_matches("validate") {
            let key = matches.get_one::<String>("key");
            if key.is_some() {
                let unwrapped = key.unwrap();
                if key::validate::key(unwrapped) {
                    println!("{} Key {} is valid.", "[+]".green(), unwrapped);
                } else {
                    println!("{} Key {} is invalid.", "[-]".red(), unwrapped);
                }
            }
        }
}
