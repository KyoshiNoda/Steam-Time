import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Homepage from './pages/Homepage';
import Statistics from './pages/Statistics';
import Timer from './pages/Timer';
import SignIn from './pages/SignIn';
import Settings from './pages/Settings';
import SignUp from './pages/SignUp';
function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/Settings" element={<Settings />} />
        <Route path="/statistics" element={<Statistics />} />
        <Route path="/timer" element={<Timer />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        {/* <Route path="/wizard" element={<Wizard />} /> */}
      </Routes>
    </>
  );
}

export default App;
