from tests.models import BookingResponse

def test_create_booking(api_context):
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-01",
            "checkout": "2026-11-05"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_context.post("/booking",data=payload)
    assert response.status == 200
    
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == 'Jim'
    assert body["booking"]["totalprice"] == 150
    assert response.status == 200
    
def test_get_booking_by_id(api_context):
    # Arrange: create a booking first, since we can't assume any ID already exists
    create_response = api_context.post("/booking", data={
        "firstname": "Alice",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Late checkout"
    })
    booking_id = create_response.json()["bookingid"]

    # Act: fetch it back by that ID
    get_response = api_context.get(f"/booking/{booking_id}")

    # Assert
    assert get_response.status == 200
    body = get_response.json()
    assert body["firstname"] == "Alice"
    assert body["lastname"] == "Smith"

def test_get_all_bookings(api_context):
    response = api_context.get("/booking")

    assert response.status == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0
    assert "bookingid" in body[0]
   
def test_get_booking_matches_schema(api_context):
    payload = {
        "firstname": "Sam",
        "lastname": "Lee",
        "totalprice": "300",
        "depositpaid": True,
        "additionalneeds": "Parking",
        "bookingdates": {"checkin": "2026-11-10", "checkout": "2026-11-12"},
    }
    create_response = api_context.post("/booking", data=payload)
    assert create_response.status == 200
    booking_id = create_response.json()["bookingid"]

    get_response = api_context.get(f"/booking/{booking_id}")
    assert get_response.status == 200

    booking = BookingResponse.model_validate(get_response.json())
    assert booking.firstname == "Sam"
    assert booking.bookingdates.checkin.isoformat() == "2026-11-10"