import dayjs from 'dayjs';

export function getTimeLeftMS(timeMS) {
    const currentTime = dayjs();
    const timeDayJS = dayjs(timeMS);
    if (timeDayJS.isBefore(currentTime)){
        return {
            hours: '00',
            mins : '00',
            secs : '00'
        }
    }
    return {
        hours : getHours(currentTime,timeDayJS),
        mins : getMins(currentTime,timeDayJS),
        secs : getSeconds(currentTime,timeDayJS)
    };
};

const getSeconds = (currentTime,timeDayJS) =>{
    const secs = timeDayJS.diff(currentTime, 'seconds') % 60;
    return secs;
}
const getMins = (currentTime,timeDayJS) =>{
    const mins = timeDayJS.diff(currentTime, 'minutes') % 60;
    return mins;
}
const getHours = (currentTime,timeDayJS) =>{
    const hours = timeDayJS.diff(currentTime, 'hours') % 24;
}