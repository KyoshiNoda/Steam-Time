import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  user: null,
  isLoading: false,
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    login: (state, action) => {
      state.isLoading = false;
      state.user = action.payload;
    },
    logout: (state) => {
      state.isLoading = false;
      state.user = null;
    },
  },
});

export default authSlice.reducer;
export const { logout } = authSlice.actions;
