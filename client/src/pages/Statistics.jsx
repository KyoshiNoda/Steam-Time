import React,{useState} from 'react';
import NavBar from '../components/NavBar/NavBar';
import { UserData } from '../Utils/Data';
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
        "#ecf0f1",
        "#50AF95",
        "#f3ba2f",
        "#2a71d0",
      ],
      data: UserData.map((data) => data.userGain),
    }]
  });
  return (
    <>
      <NavBar />
      <div>
        <div className='flex justify-evenly items-center'>
          <div className='w-1/3 flex justify-center'>
            <BarChart chartData={userData}/>
          </div>
          <div className='w-1/4 flex justify-center'>
            <PieChart chartData={userData}/>
          </div>
        </div>

        <div className='flex justify-evenly items-center'>
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
