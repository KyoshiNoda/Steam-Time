import React from "react";
import TimeForm from "../components/Timer/TimeForm";
import NavBar from "../components/NavBar/NavBar";
import Time from "../components/Timer/Time";
function Timer() {
  return (
    <>
      <NavBar />
      <div className="flex justify-center items-center h-96 bg-base-300">
        <Time />
      </div>
      <TimeForm/>
    </>
  );
}

export default Timer;
