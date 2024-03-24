import Axios from 'axios';
import { createAsyncThunk } from '@reduxjs/toolkit';

let BASE_URL = 'http://localhost:8000/api/auth';

export const loginUser = createAsyncThunk(
  '/login',
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
  '/register',
  async (user, { rejectWithValue }) => {
    try {
      const result = await Axios.post(`${BASE_URL}/register`, user);
      return result;
    } catch (error) {
      return rejectWithValue(error);
    }
  }
);
