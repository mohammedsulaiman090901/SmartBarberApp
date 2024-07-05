import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Typography, Button, Box } from '@mui/material';

const Home = () => (
  <Container>
    <Typography variant="h2" gutterBottom>
      Welcome to the Smart Barber App!
    </Typography>
    <Box display="flex" flexDirection="column" alignItems="center">
      <Button variant="contained" color="primary" component={Link} to="/services">
        Explore Services
      </Button>
      <Button variant="contained" color="secondary" component={Link} to="/barbers">
        Meet Our Barbers
      </Button>
      <Button variant="contained" color="success" component={Link} to="/booking">
        Book an Appointment
      </Button>
    </Box>
  </Container>
);

export default Home;
