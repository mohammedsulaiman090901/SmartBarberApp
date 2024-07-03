import React, { useState, useEffect } from 'react';
import axios from 'axios';

function CustomerDashboard() {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/bookings/')
      .then(response => {
        setBookings(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the bookings!', error);
      });
  }, []);

  return (
    <div>
      <h1>Customer Dashboard</h1>
      <ul>
        {bookings.map(booking => (
          <li key={booking.id}>{booking.time_slot}</li>
        ))}
      </ul>
    </div>
  );
}

export default CustomerDashboard;
