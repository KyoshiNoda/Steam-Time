import React from 'react';
import SettingForm from './SettingForm';

function SettingBox() {
  return (
    <div className="bg-slate-100 w-1/2 justify-evenly font-bold p-10 rounded-xl space-y-5">
      <h1 className="text-3xl text-black">John Doe</h1>
      <SettingForm/>
    </div>
  );
}

export default SettingBox;
