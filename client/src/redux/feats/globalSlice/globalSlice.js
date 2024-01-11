import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  toast: {},
};

const globalSlice = createSlice({
  name: 'global',
  initialState,
  reducers: {
    toast: (state, action) => {
      state.toast = action.payload;
    },
  },
});

export default globalSlice.reducer;
export const { logout } = globalSlice.actions;
