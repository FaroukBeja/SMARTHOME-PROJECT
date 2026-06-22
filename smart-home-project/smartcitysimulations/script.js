//////////////////////////////////////////////////
// SHOW MODULES
//////////////////////////////////////////////////

function showSection(id){

    let sections =
        document.querySelectorAll(".section");

    sections.forEach(section=>{
        section.style.display="none";
    });

    document.getElementById(id).style.display="block";
}

//////////////////////////////////////////////////
// SMART WATER MONITORING
//////////////////////////////////////////////////

function monitorWater(){

    let capacity =
        Number(document.getElementById("capacity").value);

    let current =
        Number(document.getElementById("currentLevel").value);

    let threshold =
        Number(document.getElementById("threshold").value);

    let result =
        document.getElementById("waterResult");

    if(capacity <= 0){

        result.innerHTML =
            "❌ Capacity must be greater than zero";

        return;
    }

    let percentage =
        (current / capacity) * 100;

    let message = "";

    if(percentage <= threshold){

        message =
            `⚠ Alert: Water level is low
            (${percentage.toFixed(1)}%)`;

    }else{

        message =
            `✅ Water level is sufficient
            (${percentage.toFixed(1)}%)`;
    }

    result.innerHTML = `
        <h3>Water Monitoring Report</h3>

        <p><strong>Capacity:</strong>
        ${capacity} L</p>

        <p><strong>Current Level:</strong>
        ${current} L</p>

        <p><strong>Percentage:</strong>
        ${percentage.toFixed(1)}%</p>

        <p>${message}</p>
    `;
}

//////////////////////////////////////////////////
// SMART WASTE MANAGEMENT
//////////////////////////////////////////////////

function checkBin(){

    let level =
        Number(document.getElementById("binLevel").value);

    let result =
        document.getElementById("wasteResult");

    if(level >= 80){

        result.innerHTML =
            `⚠ Alert: Bin is ${level}% full
            and needs collection`;

    }else{

        result.innerHTML =
            `✅ Bin is ${level}% full
            and does not require collection`;
    }
}

//////////////////////////////////////////////////
// SMART VISITOR MANAGEMENT
//////////////////////////////////////////////////

function registerVisitor(){

    let name =
        document.getElementById("visitorName").value;

    let purpose =
        document.getElementById("visitorPurpose").value;

    let passID =
        Math.floor(Math.random()*100000);

    document.getElementById("visitorPass").innerHTML = `

        <h3>Visitor Entry Pass</h3>

        <p><strong>Pass ID:</strong>
        ${passID}</p>

        <p><strong>Name:</strong>
        ${name}</p>

        <p><strong>Purpose:</strong>
        ${purpose}</p>

        <p><strong>Check-In:</strong>
        ${new Date().toLocaleString()}</p>

    `;
}

//////////////////////////////////////////////////
// SMART ENERGY MONITORING
//////////////////////////////////////////////////

function calculateEnergy(){

    let hours =
        Number(document.getElementById("energyHours").value);

    let wattage = 1200;

    let kwh =
        (wattage * hours)/1000;

    let cost =
        (kwh * 0.16).toFixed(2);

    document.getElementById("energyResult")
        .innerHTML =

        `
        <h3>Energy Report</h3>

        Consumption:
        ${kwh.toFixed(2)} kWh

        <br><br>

        Estimated Cost:
        ${cost}
        currency units
        `;
}

//////////////////////////////////////////////////
// SMART RENT REMINDER
//////////////////////////////////////////////////

function checkRent(){

    let tenant =
        document.getElementById("tenantName").value;

    let due =
        new Date(
            document.getElementById("dueDate").value
        );

    let today =
        new Date();

    let diff =
        Math.ceil(
            (due - today)
            /(1000*60*60*24)
        );

    let status = "";

    if(diff < 0){

        status = "❌ Overdue";

    }else if(diff === 0){

        status = "⚠ Due Today";

    }else{

        status =
            `✅ Due in ${diff} day(s)`;
    }

    document.getElementById("rentResult")
        .innerHTML =

        `
        <h3>Rent Reminder</h3>

        Tenant:
        ${tenant}

        <br><br>

        Status:
        ${status}
        `;
}