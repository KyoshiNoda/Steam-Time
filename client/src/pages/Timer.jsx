import React,{useState} from "react";
import NavBar from '../components/NavBar/NavBar';
import CountDownTimer from "../components/Timer/CountDownTimer";
import TimeForm from "../components/Timer/TimeForm";
function Timer() {
  const [finalTime,setFinalTime] = useState(0);
  const timeHandler = (uHours,uMins) =>{
    const timeMil =(uHours*60*60+uMins*60)*1000;
    setFinalTime(timeMil);
    console.log(finalTime); 
  };
  return (
    <>
      <NavBar/>
      <CountDownTimer timeMS = {finalTime}/>
      <TimeForm getTime = {timeHandler}/>
    </>
  );
}

export default Timer;
