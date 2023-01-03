import React from 'react';
import NavBar from '../components/NavBar/NavBar';
import SettingBox from '../components/Settings/SettingBox';
function Settings() {
  return (
    <>
      <NavBar />
      <div className="flex justify-center">
        <SettingBox/>
      </div>
    </>
  );
}

export default Settings;
