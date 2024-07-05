import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Typography, List, ListItem, ListItemText, Avatar } from '@mui/material';

const Barbers = () => {
  const [barbers, setBarbers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/barbers/').then(response => {
      setBarbers(response.data);
    });
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Our Barbers
      </Typography>
      <List>
        {barbers.map(barber => (
          <ListItem key={barber.id}>
            <Avatar src={barber.image} />
            <ListItemText primary={barber.name} secondary={barber.bio} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default Barbers;
