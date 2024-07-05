import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Typography, List, ListItem, ListItemText } from '@mui/material';

const Dashboard = () => {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/bookings/').then(response => {
      setBookings(response.data);
    });
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Welcome to your Dashboard!
      </Typography>
      <List>
        {bookings.map(booking => (
          <ListItem key={booking.id}>
            <ListItemText primary={`${booking.service} with ${booking.barber}`} secondary={booking.time_slot} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default Dashboard;
