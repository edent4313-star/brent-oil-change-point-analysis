import React, {useEffect, useState} from "react";


import Navbar from "../components/Navbar";

import KPICards from "../components/KPICards";

import HistoricalChart from "../components/HistoricalChart";

import VolatilityChart from "../components/VolatilityChart";

import EventTable from "../components/EventTable";

import Footer from "../components/Footer";


import {
getHistoricalData,
getKPIs,
getVolatility,
getEvents

} from "../services/api";



const Dashboard =()=>{


const [prices,setPrices]=useState([]);

const [kpis,setKpis]=useState({});

const [volatility,setVolatility]=useState([]);

const [events,setEvents]=useState([]);



useEffect(()=>{


loadDashboard();


},[]);



const loadDashboard=async()=>{


try{


const priceData =
await getHistoricalData();


const kpiData =
await getKPIs();


const volatilityData =
await getVolatility();


const eventData =
await getEvents();



setPrices(priceData.data);

setKpis(kpiData.data);

setVolatility(volatilityData.data);

setEvents(eventData.data);



}

catch(error){

console.log(
"Dashboard loading error",
error
);

}


};



return (

<div>


<Navbar />


<div className="container">


<h1>
Brent Oil Market Intelligence Dashboard
</h1>



<KPICards 
data={kpis}
/>



<div className="row">


<div className="col">

<HistoricalChart
data={prices}
/>


</div>


<div className="col">


<VolatilityChart
data={volatility}
/>


</div>



</div>



<EventTable
events={events}
/>



</div>



<Footer />



</div>


)


}



export default Dashboard;