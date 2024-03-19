import { createSlice } from '@reduxjs/toolkit';
import { loginUser, registerUser, steamLogin } from './authActions';

const userFromStorage = localStorage.getItem('steam');
const tokenFromStorage = localStorage.getItem('token');

const initialState = {
  user: userFromStorage ? JSON.parse(userFromStorage) : {},
  token: tokenFromStorage || '',
  loading: false,
  error: null,
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    logout: (state) => {
      state.user = null;
      state.token = '';
      state.loading = false;
      state.error = null;
      localStorage.removeItem('token');
      localStorage.removeItem('user');
    },
    updateUserDetails: (state, action) => {
      state.user = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(loginUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(loginUser.fulfilled, (state, { payload }) => {
        state.loading = false;
        state.user = payload.data.user;
        state.token = payload.data.token;
        localStorage.setItem('user', JSON.stringify(payload.data.user));
        localStorage.setItem('token', payload.data.token);
      })
      .addCase(loginUser.rejected, (state, { payload }) => {
        state.loading = false;
        state.error = payload;
      })
      .addCase(registerUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(registerUser.fulfilled, (state, { payload }) => {
        state.loading = false;
        state.user = payload.data.user;
        localStorage.setItem('user', JSON.stringify(payload.data.user));
        localStorage.setItem('token', payload.data.token);
      })
      .addCase(registerUser.rejected, (state, { payload }) => {
        state.loading = false;
        state.error = payload;
      });
  },
});

export default authSlice.reducer;
export const { logout, updateUserDetails } = authSlice.actions;
