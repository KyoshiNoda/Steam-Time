import { configureStore } from '@reduxjs/toolkit';
import authSliceReducer from '../redux/feats/authSlice/authSlice';

const store = configureStore({
  reducer: {
    auth: authSliceReducer,
  },
});

export default store;
