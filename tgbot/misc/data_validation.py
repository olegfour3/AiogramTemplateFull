import re


async def only_latin_letters(string: str) -> bool:
    if re.search(r'[^a-zA-Z]', string):
        return False
    else:
        return True


async def phone_number_is_valid(phone_number: str) -> str:
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
    return True if re.match(validate_phone_number_pattern, phone_number) is not None and phone_number[0:2] == '48' else False
