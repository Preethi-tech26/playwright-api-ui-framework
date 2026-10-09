import pytest

BASE_URL="https://restful-booker.herokuapp.com"

def test_health_check(api_context):
    response = api_context.get("/ping")
    assert response.status == 201
    
def test_bookings(api_context):
    payload = {
        "firstname": "Jim",
        "lastname":"Brown",
        "totalprice": 150,
        "depositpaid" : True,
        "additionalneeds": "Breakfast",
        "bookingdates":{
            "checkin": "2026-10-22",
            "checkout":   "2026-10-24"
        }
    }
    response = api_context.post("/booking", data = payload)

    assert response.status == 200
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] =="Jim"
    
    
def test_get_booking_id(api_context):
    payload = {
            "firstname": "Jane",
            "lastname":"Brown",
            "totalprice": 150,
            "depositpaid" : True,
            "additionalneeds": "Late checkout",
            "bookingdates":{
                "checkin": "2026-10-20",
                "checkout":   "2026-10-21"
            }
        }
    create_response = api_context.post("/booking", data = payload)
    
    assert create_response.status == 200
    body = create_response.json()
   
    ##booking_id = create_response.json()["bookingid"]
    booking_id = body["bookingid"]
    get_response = api_context.get(f"/booking/{booking_id}")
    get_body= get_response.json()
    assert get_response.status == 200
    assert get_body["firstname"] =="Jane"
    assert get_body["totalprice"] == 150
    