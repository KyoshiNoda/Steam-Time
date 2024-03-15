import Axios from 'axios';
import { createAsyncThunk } from '@reduxjs/toolkit';

let BASE_URL = 'http://localhost:3001/api/auth';

export const loginUser = createAsyncThunk(
  'api/auth/login',
  async (user, { rejectWithValue }) => {
    try {
      const data = await Axios.post(`${BASE_URL}/login`, user);
      return data;
    } catch (error) {
      return rejectWithValue(error);
    }
  }
);

export const registerUser = createAsyncThunk(
  '/api/auth/register',
  async (user, { rejectWithValue }) => {
    try {
      const result = await Axios.post(`${BASE_URL}/register`, user);
      return result;
    } catch (error) {
      return rejectWithValue(error);
    }
  }
);

export const steamLogin = createAsyncThunk(
  'api/auth/steamLogin',
  async ({ rejectWithValue }) => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/steam_auth/steam-login`
      );
      const data = await response.json();

      // Handle error response from server
      if (!response.ok) {
        throw new Error(data.message || 'Failed to log in with Steam');
      }

      // Return data which includes user and token
      return data;
    } catch (error) {
      return rejectWithValue(error);
    }
  }
);
