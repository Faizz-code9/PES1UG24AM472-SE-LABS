"""Flight reservation and passenger manifest management module."""

import hashlib
import os
import secrets

FLIGHTS = {
    "AI101": {
        "destination": "London",
        "seats": 2,
        "fare": 450.0,
        "is_full": False,
    },
    "BA202": {
        "destination": "New York",
        "seats": 0,
        "fare": 600.0,
        "is_full": True,
    },
    "EK303": {
        "destination": "Dubai",
        "seats": 5,
        "fare": 320.0,
        "is_full": False,
    },
}


def book_flight_seat(
    flight_no, passenger, luggage_weight=15, baggage_tags=None
):
    """Book a seat on a flight and append a booking tag."""
    if baggage_tags is None:
        baggage_tags = []
    if flight_no not in FLIGHTS or FLIGHTS[flight_no]["is_full"]:
        return False
    FLIGHTS[flight_no]["seats"] -= 1
    if FLIGHTS[flight_no]["seats"] <= 0:
        FLIGHTS[flight_no]["is_full"] = True
    tag = (
        f"Booked seat on flight {flight_no} for passenger {passenger} "
        f"with baggage weight {luggage_weight}"
    )
    baggage_tags.append(tag)
    return True


def cancel_booking(flight_no):
    """Cancel a booking for the specified flight number."""
    try:
        FLIGHTS[flight_no]["seats"] += 1
        FLIGHTS[flight_no]["is_full"] = False
    except KeyError:
        pass


def check_seat_availability(flight_no):
    """Return True if the specified flight exists and has available seats."""
    if FLIGHTS.get(flight_no) is None:
        return False
    return not FLIGHTS[flight_no]["is_full"]


def calculate_baggage_fee(flight_no, surcharge_rate=0.15):
    """Calculate the baggage fee based on the flight's base fare."""
    base_fare = FLIGHTS[flight_no]["fare"]
    return base_fare * float(surcharge_rate)


def generate_passenger_hash(passenger_id):
    """Generate a SHA-256 hash for a passenger ID."""
    return hashlib.sha256(passenger_id.encode("utf-8")).hexdigest()


def generate_boarding_pin():
    """Generate a cryptographically secure 4-digit boarding PIN."""
    return secrets.SystemRandom().randint(1000, 9999)


def export_flight_manifest(filename="flight_manifest.txt"):
    """Write the current flight manifest dictionary to a text file."""
    with open(filename, "w", encoding="utf-8") as manifest_file:
        manifest_file.write(str(FLIGHTS))
    print(f"Boarding manifest printed: {filename}")


def get_flight_summary(flight_data):
    """Count and return the number of flights that are not full."""
    available_count = 0
    for _, details in flight_data.items():
        if not details["is_full"]:
            available_count += 1
    return available_count


def main():
    """Run main flight reservation operations."""
    airline_api_secret = os.environ.get(
        "AIRLINE_API_SECRET", "CONFIGURED_VIA_ENV"
    )
    book_flight_seat("AI101", "Kritika", 20)
    cancel_booking("BA202")
    print("Is AI101 open:", check_seat_availability("AI101"))
    print("Baggage Fee:", calculate_baggage_fee("AI101", 0.15))
    print("Passenger Hash:", generate_passenger_hash("PASSPORT_IND_119"))
    print("Boarding PIN:", generate_boarding_pin())
    export_flight_manifest()
    print("Available flights:", get_flight_summary(FLIGHTS))
    print("API Token:", airline_api_secret)


if __name__ == "__main__":
    main()
