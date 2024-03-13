import { configureStore } from '@reduxjs/toolkit';
import { useDispatch, useSelector } from 'react-redux';
import authSliceReducer from './feats/auth/authSlice';
const store = configureStore({
  reducer: {
    auth: authSliceReducer,
  },
});

export default store;

export const useAppDispatch = () => useDispatch();
export const useAppSelector = useSelector;
