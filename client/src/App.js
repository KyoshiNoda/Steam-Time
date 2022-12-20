import React from 'react';
import {Routes,Route} from 'react-router-dom';
import Homepage from './pages/Homepage';
import Account from './pages/Account';
import Statistics from './pages/Statistics';
import Timer from './pages/Timer';
import Signout from './pages/Signout';
import Settings from './pages/Settings';
function App() {
  return (
    <>
      <Routes>
        <Route path = '/' element = {<Homepage/>}/>
        <Route path = '/account' element = {<Account/>}/>
        <Route path = '/Settings' element = {<Settings/>}/>
        <Route path = '/statistics' element = {<Statistics/>}/>
        <Route path = '/timer' element = {<Timer/>}/>
        <Route path = '/signout' element = {<Signout/>}/>
      </Routes>
    </>
  );
}

export default App;
