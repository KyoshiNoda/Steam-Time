import { configureStore } from '@reduxjs/toolkit';
import { useDispatch, useSelector } from 'react-redux';
import authSliceReducer from './feats/auth/authSlice';
import globalSliceReducer from './feats/globalSlice/globalSlice';
const store = configureStore({
  reducer: {
    auth: authSliceReducer,
    global: globalSliceReducer,
  },
});

export default store;

export const useAppDispatch = () => useDispatch();
export const useAppSelector = useSelector;
