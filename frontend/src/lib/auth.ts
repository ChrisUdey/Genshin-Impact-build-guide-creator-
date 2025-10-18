import api from './api';

export const login = async (email: string, password: string) => {
    const response = await api.post('/api/auth/login', { email, password });
    localStorage.setItem('token', response.data.token);
    return response.data;
};

export const logout = () => {
    localStorage.removeItem('token');
};

export const getToken = () => {
    return localStorage.getItem('token');
};

export const isAuthenticated = () => {
    return !!getToken();
};