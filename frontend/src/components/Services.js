import React, { useEffect, useState } from 'react';
import { getServices } from '../api';
import { Container, Typography, List, ListItem, ListItemText } from '@mui/material';

const Services = () => {
  const [services, setServices] = useState([]);

  useEffect(() => {
    getServices().then(response => {
      setServices(response.data);
    });
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Our Services
      </Typography>
      <List>
        {services.map(service => (
          <ListItem key={service.id}>
            <ListItemText primary={service.name} secondary={`${service.duration} minutes`} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default Services;
