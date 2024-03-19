import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  toast: {},
  isApiKeyModalOpen: false,
};

const globalSlice = createSlice({
  name: 'global',
  initialState,
  reducers: {
    toast: (state, action) => {
      state.toast = action.payload;
    },
    openAPIKeyModal: (state) => {
      state.isApiKeyModalOpen = true;
    },
    closeAPIKeyModal: (state) => {
      state.isApiKeyModalOpen = false;
    },
  },
});

export default globalSlice.reducer;
export const { logout, openAPIKeyModal, closeAPIKeyModal } =
  globalSlice.actions;
