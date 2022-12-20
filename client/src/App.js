import React from 'react';
import {Routes,Route} from 'react-router-dom';
import Homepage from './pages/Homepage';
import Account from './pages/Account';
function App() {
  return (
    <>
      <Routes>
        <Route path = '/' element = {<Homepage/>}/>
        <Route path = '/account' element = {<Account/>}/>
      </Routes>
    </>
  );
}

export default App;
