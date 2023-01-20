import React,{useState} from 'react';
import NavBar from '../components/NavBar/NavBar';
import { UserData,BarData, PieData } from '../Utils/Data';
import BarChart from '../components/Statistics/BarChart';
import PieChart from '../components/Statistics/PieChart';
import RadarChart from '../components/Statistics/RadarChart';
import LineChart from '../components/Statistics/LineChart';
function Statistics() {
  const [userData,setUserData] = useState({
    labels: UserData.map((data) => data.year),
    datasets : [{
      label : 'Users Gained',
      backgroundColor: [
        "rgba(75,192,192,1)",
        "#264653",
        "#2a9d8f",
        "#f3ba2f",
        "#2a71d0",
      ],
      data: UserData.map((data) => data.userGain),
    }]
  });
  const [barChartData,setBarData] = useState({
    labels: BarData.map((data) => data.day),
    datasets : [{
      label : 'Weekly Report',
      backgroundColor: [
        '#b87a44',
        "#eeb111",
        "#8cc63f",
        "#569bbe",
        '#247ba0',
        '#34b233',
        '#dc4cdc'
      ],
      data: BarData.map((data) => data.mins),
    }]
  });
  const [pieChartData,setPieChartData] = useState({
    labels: PieData.map((data) => data.action),
    datasets : [{
      label : 'Activities Break Down',
      backgroundColor: [
        '#b87a44',
        "#eeb111",
        "#8cc63f",
        "#569bbe",
        '#247ba0',
        '#34b233',
        '#dc4cdc'
      ],
      data: PieData.map((data) => data.mins),
    }]
  });
  return (
    <>
      <NavBar />
      <div>
        <div className='flex justify-evenly items-center bg-slate-50'>
          <div className='w-1/3 flex justify-center'>
            <BarChart chartData={barChartData}/>
          </div>
          <div className='w-1/4 flex justify-center'>
            <PieChart chartData={pieChartData}/>
          </div>
        </div>

        <div className='flex justify-evenly items-center bg-slate-50'>
          <div className='w-1/3 flex justify-center'>
            <RadarChart chartData={userData}/>
          </div>
          <div className='w-1/3 flex justify-center'>
            <LineChart chartData={userData}/>
          </div>
        </div>
      </div>
    </>
  );
}

export default Statistics;
