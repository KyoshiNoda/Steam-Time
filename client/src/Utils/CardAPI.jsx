
export const favGameID = (gameList) =>{
  let maxTime = 0;
  let name = '';
  for (let i = 0; i < gameList.length; i++) {
    if (gameList[i].playtime_forever > maxTime) {
      name = gameList[i].appid;
      maxTime = gameList[i].playtime_forever;
    }
  }
  return name;
}

export const totalMins = (gameList) =>{
  let totalMins = 0;
  for (let i = 0; i < gameList.length; i++) {
    totalMins += gameList[i].playtime_forever;
  }
  return totalMins;
}