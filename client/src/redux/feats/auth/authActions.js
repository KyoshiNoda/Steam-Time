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
  'api/auth/google',
  async (code, { rejectWithValue }) => {
    try {
      const tokens = await Axios.post(`${BASE_URL}/steam_auth`, { code });
      return tokens;
    } catch (error) {
      return rejectWithValue(error);
    }
  }
);
