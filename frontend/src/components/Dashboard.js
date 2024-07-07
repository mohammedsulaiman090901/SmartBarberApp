import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        const fetchMessage = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/customer-dashboard/', {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                    }
                });
                setMessage(response.data.message);
            } catch (error) {
                console.error('Dashboard error', error);
                alert('You need to log in to access this page.');
                window.location.href = '/login';
            }
        };
        fetchMessage();
    }, []);

    return (
        <div>
            <h2>Dashboard</h2>
            <p>{message}</p>
            <nav>
                <ul>
                    <li><Link to="/login">Login</Link></li>
                    <li><Link to="/register">Register</Link></li>
                    <li><Link to="/services">Explore Services</Link></li>
                    <li><Link to="/barbers">Meet Our Barbers</Link></li>
                    <li><Link to="/booking">Book an Appointment</Link></li>
                </ul>
            </nav>
        </div>
    );
};

export default Dashboard;
