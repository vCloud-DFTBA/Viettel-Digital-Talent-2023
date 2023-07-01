fetch("/attendees")
.then(res => {
    return res.json();
})
.then(attendees => {
    let placeholder = document.querySelector("#attData");
    let out = "";
    attendees.forEach(attendee => {
        if(attendee["Chuyên ngành"] == "NULL") attendee["Chuyên ngành"] = 'Không xác định';
        out += `
            <tr>
                <td> ${attendee.STT}</td>
                <td> ${attendee["Họ và tên"]}</td>
                <td> ${attendee["Năm sinh"]}</td>
                <td> ${attendee["Giới tính"]}</td>
                <td> ${attendee["Trường"]}</td>
                <td> ${attendee["Chuyên ngành"]}</td>
            </tr>
        `
    })
    placeholder.innerHTML = out;
})
.catch(error => console.log(error));

