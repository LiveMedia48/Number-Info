import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init
import argparse

# Initialize colorama
init(autoreset=True)

def get_number_info(number_str):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(number_str, None)
        
        # Validate the number
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{Fore.RED}[-] Invalid phone number.")
            return

        print(f"{Fore.CYAN}=== Number Information ===")
        print(f"{Fore.YELLOW}[*] Number: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        
        # Get Location
        location = geocoder.description_for_number(parsed_number, "en")
        print(f"{Fore.GREEN}[+] Location: {location if location else 'Unknown'}")
        
        # Get Carrier
        carrier_name = carrier.name_for_number(parsed_number, "en")
        print(f"{Fore.GREEN}[+] Carrier: {carrier_name if carrier_name else 'Unknown'}")
        
        # Get Timezone
        timezones = timezone.time_zones_for_number(parsed_number)
        print(f"{Fore.GREEN}[+] Timezone: {', '.join(timezones) if timezones else 'Unknown'}")
        
    except phonenumbers.NumberParseException as e:
        print(f"{Fore.RED}[-] Error parsing number: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LiveMedia Number Info Tool")
    parser.add_argument("-n", "--number", required=True, help="Phone number with country code (e.g., +919876543210)")
    args = parser.parse_args()
    
    get_number_info(args.number)
