import React from "react";
import { TiTick } from "react-icons/ti";
import "./Stepper.css";

const Stepper = ({ currentStep, handleNextStep, complete }) => {
  const steps = ["login", "API key"];

  return (
    <>
      <div className="flex justify-between">
        {steps?.map((step, i) => (
          <div
            key={i}
            className={`step-item ${currentStep === i + 1 && "active"} ${(i + 1 < currentStep || complete) && "complete"
              } `}
          >
            <div className="step">
              {i + 1 < currentStep || complete ? <TiTick size={24} /> : i + 1}
            </div>
            <p className="text-gray-500">{step}</p>
          </div>
        ))}
      </div>
      {!complete && (
        <button
          className="btn"
          onClick={() => {
            currentStep === steps.length ? handleNextStep() : handleNextStep();
          }}
        >
          {currentStep === steps.length ? "Finish" : "Next"}
        </button>
      )}
    </>
  );
};

export default Stepper;
