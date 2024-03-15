import React, { useState } from 'react';
import Stepper from './Stepper';
import SteamLogin from '../SignIn/SteamLogin';

function SteamBox() {
  const [currentStep, setCurrentStep] = useState(1);
  const [complete, setComplete] = useState(false);

  const handleNextStep = () => {
    if (currentStep < 2) {
      setCurrentStep((prevStep) => prevStep + 1);
    } else {
      setComplete(true);
    }
  };

  return (
    <div className='bg-white rounded p-4 flex flex-col items-center'>
      {currentStep === 1 && (
        <div>
          <SteamLogin />
        </div>
      )}
      {currentStep === 2 && (
        <div className="mt-4">
          <input type="text" placeholder="API KEY" className="input input-bordered input-primary w-full max-w-xs" />
        </div>
      )}
      <Stepper currentStep={currentStep} handleNextStep={handleNextStep} complete={complete} />
    </div>
  );
}

export default SteamBox;
