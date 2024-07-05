import React, { useState, useEffect } from 'react';
import { getServices, createBooking } from '../api';
import axios from 'axios';
import { Container, Typography, TextField, MenuItem, Button } from '@mui/material';

const Booking = () => {
  const [services, setServices] = useState([]);
  const [barbers, setBarbers] = useState([]);
  const [bookingData, setBookingData] = useState({
    service: '',
    barber: '',
    time_slot: '',
  });

  useEffect(() => {
    getServices().then(response => {
      setServices(response.data);
    });
    axios.get('http://127.0.0.1:8000/api/barbers/').then(response => {
      setBarbers(response.data);
    });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    createBooking(bookingData).then(response => {
      alert('Booking created!');
    });
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Book an Appointment
      </Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          select
          label="Select Service"
          value={bookingData.service}
          onChange={(e) => setBookingData({ ...bookingData, service: e.target.value })}
          fullWidth
          margin="normal"
        >
          {services.map(service => (
            <MenuItem key={service.id} value={service.id}>
              {service.name}
            </MenuItem>
          ))}
        </TextField>
        <TextField
          select
          label="Select Barber"
          value={bookingData.barber}
          onChange={(e) => setBookingData({ ...bookingData, barber: e.target.value })}
          fullWidth
          margin="normal"
        >
          {barbers.map(barber => (
            <MenuItem key={barber.id} value={barber.id}>
              {barber.name}
            </MenuItem>
          ))}
        </TextField>
        <TextField
          label="Select Time Slot"
          type="datetime-local"
          value={bookingData.time_slot}
          onChange={(e) => setBookingData({ ...bookingData, time_slot: e.target.value })}
          fullWidth
          margin="normal"
          InputLabelProps={{
            shrink: true,
          }}
        />
        <Button type="submit" variant="contained" color="primary">
          Book Appointment
        </Button>
      </form>
    </Container>
  );
};

export default Booking;
