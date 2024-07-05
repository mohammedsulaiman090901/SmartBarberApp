import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
});

export const getServices = () => api.get('services/');
export const createService = (data) => api.post('services/', data);
export const getBookings = () => api.get('bookings/');
export const createBooking = (data) => api.post('bookings/', data);
export const updateBooking = (id, data) => api.put(`bookings/${id}/`, data);
export const deleteBooking = (id) => api.delete(`bookings/${id}/`);
