import React from "react";


const EventTable = ({ events }) => {


return (

<div className="card">

<h3>
Detected Market Events
</h3>


<table>

<thead>

<tr>
<th>Date</th>
<th>Event</th>
<th>Impact</th>
<th>Change %</th>
</tr>

</thead>


<tbody>

{
events.map((event,index)=>(

<tr key={index}>

<td>
{event.date}
</td>

<td>
{event.event}
</td>


<td>
{event.impact}
</td>


<td>
{event.change}
</td>


</tr>

))
}

</tbody>

</table>


</div>

)

}


export default EventTable;