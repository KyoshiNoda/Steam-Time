import React,{useState} from 'react';
import NavBar from '../components/NavBar/NavBar';
import { UserData } from '../Utils/Data';
import BarChart from '../components/Statistics/BarChart';
import PieChart from '../components/Statistics/PieChart';
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
      <div className='flex justify-center'>
        <div className='w-1/2 p-5'>
          <BarChart chartData={userData}/>
        </div>
        <div className='w-1/2 p-5'>
          <PieChart chartData={userData}/>
        </div>
      </div>

      <div className='flex justify-center'>
        <div className='w-1/2 p-5'>
          <BarChart chartData={userData}/>
        </div>
        <div className='w-1/3 p-5'>
          <PieChart chartData={userData}/>
        </div>
      </div>
    </>
  );
}

export default Statistics;
