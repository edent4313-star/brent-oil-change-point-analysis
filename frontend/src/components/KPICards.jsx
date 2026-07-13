import React from "react";


function KPICards({data}){


return (

<div className="kpi-container">


<div className="kpi-card">

<h3>
Current Price
</h3>

<h2>
${data.current_price || 0}
</h2>

</div>



<div className="kpi-card">

<h3>
Percentage Change
</h3>

<h2>
{data.percentage_change || 0}%
</h2>

</div>




<div className="kpi-card">

<h3>
Volatility
</h3>

<h2>
{data.volatility || 0}%
</h2>

</div>




<div className="kpi-card">

<h3>
Total Records
</h3>

<h2>
{data.total_records || 0}
</h2>

</div>


</div>


)

}


export default KPICards;