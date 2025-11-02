import phonenumbers
import pycountry

def getCountry(phoneNumber, region: str | None = None) -> str:
    """
    Method gets the user's country from their phone number
    """
    try:
        parsed = phonenumbers.parse(phoneNumber, region)
    except phonenumbers.NumberParseException:
        return {"valid": False, "error": "Invalid phone number format"}

    if not phonenumbers.is_valid_number(parsed):
        return {"valid": False, "error": "Not a valid number"}

    region_code = phonenumbers.region_code_for_number(parsed)
    country_name = (
        pycountry.countries.get(alpha_2=region_code).name
        if region_code and pycountry.countries.get(alpha_2=region_code)
        else region_code
    )

    return country_name
