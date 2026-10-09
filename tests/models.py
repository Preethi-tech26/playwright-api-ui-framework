from datetime import date
from typing import Optional
from pydantic import BaseModel


class BookingDates(BaseModel):
    checkin: date
    checkout: date


class BookingResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None